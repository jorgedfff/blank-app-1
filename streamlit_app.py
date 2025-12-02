import streamlit as st
import py3Dmol

# Configuración de la página
st.set_page_config(page_title="Proteínas Interactivas", page_icon="🧬", layout="wide")

# --- Sidebar ---
st.sidebar.title("Menú")
page = st.sidebar.radio("Ir a:", ["Inicio", "Tipos de Proteínas", "Modelo 3D"])

# --- Páginas ---
if page == "Inicio":
    st.title("🏠 Introducción a las Proteínas")
    st.markdown("""
    Las proteínas son macromoléculas formadas por cadenas de aminoácidos y desempeñan funciones esenciales en los seres vivos:
    - Estructurales
    - Catalíticas (enzimas)
    - De transporte
    - De señalización
    - De defensa
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Protein_structure.png/640px-Protein_structure.png",
             caption="Estructura general de una proteína", use_column_width=True)

elif page == "Tipos de Proteínas":
    st.title("🧬 Tipos de Proteínas")
    
    st.subheader("1️⃣ Proteínas Fibrosas")
    st.write("Ejemplos: Colágeno, Queratina, Fibrina")
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/70/Collagen.png", caption="Colágeno", use_column_width=True)
    
    st.subheader("2️⃣ Proteínas Globulares")
    st.write("Ejemplos: Hemoglobina, Mioglobina, Enzimas")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/37/Hemoglobin_3D_model.png", caption="Hemoglobina", use_column_width=True)
    
    st.subheader("3️⃣ Proteínas de Membrana")
    st.write("Ejemplos: Canales iónicos, GPCR, Bombas ATPasa")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Cell_membrane_3D.png/640px-Cell_membrane_3D.png", caption="Proteína de membrana", use_column_width=True)

    st.subheader("4️⃣ Proteínas Motoras")
    st.write("Ejemplos: Actina, Miosina, Dineína, Kinesina")
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5b/Myosin_Actin.png", caption="Miosina", use_column_width=True)

    st.subheader("5️⃣ Proteínas de Almacenamiento")
    st.write("Ejemplos: Ferritina, Caseína")
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/12/Ferritin.png", caption="Ferritina", use_column_width=True)

    st.subheader("6️⃣ Proteínas Reguladoras")
    st.write("Ejemplos: Factores de transcripción, Represores, Activadores")
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2b/Transcription_factor.png", caption="Factor de transcripción", use_column_width=True)

elif page == "Modelo 3D":
    st.title("🧬 Modelo 3D Interactivo")

    # Dropdown para elegir proteína
    proteina = st.selectbox("Elige una proteína:", ["Hemoglobina", "Colágeno", "Mioglobina", "Actina"])

    # Dropdown para elegir estilo
    estilo = st.selectbox("Estilo de visualización:", ["cartoon", "sticks", "surface"])

    # IDs de proteínas en PDB
    pdb_ids = {
        "Hemoglobina": "1A3N",
        "Colágeno": "1CAG",
        "Mioglobina": "1MBO",
        "Actina": "1J6Z"
    }

    # Crear visor 3D
    view = py3Dmol.view(query=f'pdb:{pdb_ids[proteina]}', width=700, height=500)

    # Aplicar estilo seleccionado
    if estilo == "cartoon":
        view.setStyle({'cartoon': {'color': 'spectrum'}})
    elif estilo == "sticks":
        view.setStyle({'stick': {}})
    elif estilo == "surface":
        view.setStyle({'surface': {'colorscheme':'spectrum'}})

    view.zoomTo()

    # Mostrar en Streamlit
    st.components.v1.html(view.render(), height=500)
    
