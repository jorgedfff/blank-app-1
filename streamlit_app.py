import streamlit as st

st.set_page_config(page_title="Itinerario de la Posada 🎄", page_icon="🎉")

st.title("🎄 Itinerario Oficial de la Posada 🎄")
st.subheader("Organizado con amor y caos navideño ✨")

st.markdown("---")

# Itinerario
st.header("🕒 Actividades del evento")

st.markdown("""
### **4:00 – 5:00 PM**
📺 *Veremos videos para calentar motores y reírnos un rato.*

### **5:00 – 5:30 PM**
🥂 **Brindis e inauguración** del evento  
✨ A cargo de **La Luli**, nuestra presentadora estrella.

### **5:30 – 7:00 PM**
🎉 *Juegos preparados*  
Competencias, risas y probablemente chismes.

### **7:00 – 8:00 PM**
🌭 **Cena**  
El menú de gala: *dogos aguaje* porque somos finos pero con barrio.

### **8:00 PM en adelante**
💃🕺 **Baile, canto y música**  
Lo que pase después ya no es responsabilidad de la organización.
""")

st.markdown("---")
st.success("🎁 ¡Listo! La posada ya tiene itinerario navideño profesional.")
