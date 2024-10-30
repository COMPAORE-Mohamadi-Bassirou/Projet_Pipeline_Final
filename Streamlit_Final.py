import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import base64

# Configuration de la page
st.set_page_config(
    page_title="Analyse des Facteurs - Mortalité Infantile",
    page_icon="💡",
    layout="wide"
)

# Chemins relatifs
local_file_path = "donnees_imputees_knn_mondial.xlsx"
background_image_accueil = "image3.jpg"
background_image_comparer = "image2.jpg"

# Fonction pour encoder une image en base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Fonction pour définir l’image de fond
def set_background(image_path):
    encoded_image = get_base64_image(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                        url(data:image/png;base64,{encoded_image});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Fonction pour charger les données Excel
@st.cache_data
def load_excel_data():
    try:
        sheets = pd.read_excel(local_file_path, sheet_name=None)
        for key in sheets:
            sheets[key].columns = [col.strip().lower() for col in sheets[key].columns]
        return sheets
    except FileNotFoundError:
        st.error(f"Le fichier '{local_file_path}' est introuvable.")
        return None
    except Exception as e:
        st.error(f"Erreur lors du chargement : {str(e)}")
        return None

# Charger les données
excel_data = load_excel_data()

# Navigation via la barre latérale
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ["Accueil", "Comparer les Indicateurs", "Classement des Pays", "Carte des Pays à Haut Risque"])

# --- PAGE D'ACCUEIL ---
if page == "Accueil":
    set_background(background_image_accueil)
    st.title("Construction d'un Pipeline ETL pour l'Analyse de l'Impact des *Dépenses Publiques de Santé sur la Mortalité Infantile à l’échelle mondiale")
    st.markdown("""
        Ce dashboard interactif est *conçu *pour *éclairer l'impact des dépenses publiques de santé sur la mortalité infantile** à l’échelle mondiale. 
        Dans ce projet,*nous *nous *sommes *penchés sur les *facteurs critiques *influençant la *mortalité *infantile dans les pays du monde.

        Grâce à une approche analytique et visuelle, vous pourrez *exploré :*
        
        - *Les tendances des dépenses de santé* par pays et leur relation avec la mortalité *infantile.
        - *Des classements* qui *mettent* en lumière les pays à haut risque, *facilitant *une *meilleure *compréhension des *dynamiques de santé publique
        - *Des cartes interactives* *vous permettant de visualiser* les données de manière intuitive et informative.

        Plongez dans les données, comparez les indicateurs clés et *participe* à la discussion sur l'amélioration des politiques de santé publique. 
                
        Ensemble,*nous pouvon* contribuer à un avenir où *chaque enfant a la chance de grandir en bonne santé.
    """)

# --- PAGE COMPARER LES INDICATEURS ---
elif page == "Comparer les Indicateurs":
    set_background(background_image_comparer)
    if excel_data:
        st.title("Comparer l'Évolution des Indicateurs entre Deux Pays")

        # Sélection des pays et indicateurs
        country1 = st.selectbox("Sélectionner le premier pays", list(excel_data.keys()), key="country1")
        country2 = st.selectbox("Sélectionner le deuxième pays", list(excel_data.keys()), key="country2")

        df1, df2 = excel_data[country1], excel_data[country2]
        indicator1 = st.selectbox(f"Indicateur pour {country1}", [col for col in df1.columns if col != 'date'], key="indicator1")
        indicator2 = st.selectbox(f"Indicateur pour {country2}", [col for col in df2.columns if col != 'date'], key="indicator2")

        # Comparaison des indicateurs avec un graphique
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df1['date'], df1[indicator1], marker='o', linestyle='-', color='blue', label=f"{country1} - {indicator1}", linewidth=2, markersize=5)
        ax.plot(df2['date'], df2[indicator2], marker='o', linestyle='-', color='red', label=f"{country2} - {indicator2}", linewidth=2, markersize=5)

        ax.set_title("Comparaison des Indicateurs", fontsize=18, fontweight='bold')
        ax.set_xlabel("Date", fontsize=14, fontweight='bold')
        ax.set_ylabel("Valeur", fontsize=14, fontweight='bold')
        ax.legend(fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)

# Afficher des statistiques descriptives sous forme de colonnes
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader(f"Statistiques pour {country1}")
            st.write(f"Moyenne : {df1[indicator1].mean():.2f}")
            st.write(f"Médiane : {df1[indicator1].median():.2f}")
            st.write(f"Mode : {df1[indicator1].mode().values[0] if not df1[indicator1].mode().empty else 'N/A'}")

        with col2:
            st.subheader(f"Statistiques pour {country2}")
            st.write(f"Moyenne : {df2[indicator2].mean():.2f}")
            st.write(f"Médiane : {df2[indicator2].median():.2f}")
            st.write(f"Mode : {df2[indicator2].mode().values[0] if not df2[indicator2].mode().empty else 'N/A'}")

# --- PAGE CLASSEMENT DES PAYS ---
elif page == "Classement des Pays":
    set_background(background_image_comparer)
    if excel_data:
        st.title("Classement des Pays par Indicateur")

        all_indicators = {col for df in excel_data.values() for col in df.columns if col != 'date'}
        selected_indicator = st.selectbox("Choisissez l'indicateur", sorted(all_indicators))

        data = [
            {"Pays": country, "Valeur": df[selected_indicator].iloc[-1]}
            for country, df in excel_data.items() if selected_indicator in df.columns
        ]
        classement_df = pd.DataFrame(data).sort_values(by="Valeur", ascending=False)

        st.dataframe(classement_df)

        fig = px.bar(
            classement_df, x="Pays", y="Valeur",
            title=f"Classement des Pays par {selected_indicator}",
            labels={"Valeur": selected_indicator},
            text_auto=True
        )
        st.plotly_chart(fig)

# --- PAGE CARTE DES PAYS À HAUT RISQUE ---
elif page == "Carte des Pays à Haut Risque":
    set_background(background_image_comparer)
    if excel_data:
        st.title("Carte des Pays à Haut Risque")

        # Récupérer tous les indicateurs disponibles
        all_indicators = {
            "taux de mortalité infantile (pour 1 000 naissances vivantes)": "taux de mortalité infantile (pour 1 000 naissances vivantes)",
            "nombre de médecins pour 1 000 habitants": "nombre de médecins pour 1 000 habitants",
            "dépenses totales de santé (pourcentage du pib)":"dépenses totales de santé (pourcentage du pib)",
            "dépenses de santé publiques (pourcentage des dépenses totales)":"dépenses de santé publiques (pourcentage des dépenses totales)",
            "part des dépenses de santé supportées par les ménages":"part des dépenses de santé supportées par les ménages",
            "dépenses de santé privées (pourcentage des dépenses totales)":"dépenses de santé privées (pourcentage des dépenses totales)",
            
        }

        # Sélection de l'indicateur à afficher sur la carte
        selected_indicator = st.selectbox("Choisissez l'indicateur à visualiser", list(all_indicators.keys()))

        # Préparation des données pour la carte
        data = []
        for country, df in excel_data.items():
            indicator_column = all_indicators[selected_indicator]
            if indicator_column not in df.columns:
                 st.write(f"L'indicateur '{indicator_column}' est manquant pour {country}.")
            else:
                value = df[indicator_column].iloc[-1]
            if pd.isna(value):
                st.write(f"Valeur NaN pour {indicator_column} dans {country}.")
            else:
                data.append({"Pays": country, "Valeur": value})
            
        map_df = pd.DataFrame(data)

        # Afficher la carte avec Plotly
        if not map_df.empty:
            fig = px.choropleth(
                map_df,
                locations="Pays",
                locationmode="country names",
                color="Valeur",
                color_continuous_scale=["lightgray", "red"],
                title=f"Carte des Pays par {selected_indicator}",
                labels={"Valeur": selected_indicator},
            )
            fig.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="lightgray")
            st.plotly_chart(fig)
        else:
            st.warning(f"Aucune donnée valide disponible pour l'indicateur '{selected_indicator}'.")

    else:
        st.error("Erreur : Impossible de charger les données. Vérifiez le fichier Excel.")


