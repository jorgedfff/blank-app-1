import streamlit as st
import py3Dmol

st.title("Modelo 3D Interactivo de Proteínas 🧬")

# Selección de proteína
proteina = st.selectbox("Elige una proteína:", ["Hemoglobina", "Colágeno", "Mioglobina", "Actina"])

# IDs correspondientes
pdb_ids = {
    "Hemoglobina": "1A3N",
    "Colágeno": "1CAG",
    "Mioglobina": "1MBO",
    "Actina": "1J6Z"
}

# Crear visor 3D
view = py3Dmol.view(query=f'pdb:{pdb_ids[proteina]}', width=600, height=500)
view.setStyle({'cartoon': {'color': 'spectrum'}})
view.zoomTo()

# Mostrar en Streamlit
st.components.v1.html(view.render(), height=500)
