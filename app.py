import streamlit as st

st.set_page_config(page_title="Cargos Posibles 108A", page_icon="📋")

st.title("📋 ¿A qué cargos puedo postularme?")
st.write("Basado en Oblea 108A 2026 - Ferreyra Matías")

st.divider()

# Puntajes relevantes
cargos = {
    "Equipo de Orientación Escolar (OE)": 28.00,
    "Equipo de Orientación Escolar (SOE)": 28.00,
    "Psicología GP/MR": 27.50,
    "Profesor CENS (CMS/CNA)": 26.00,
    "Profesor Adultos PR": 25.75,
    "Secundaria CCD/PIC": 25.50,
    "Secundaria SAT/SST/STY": 23.50
}

st.subheader("Análisis de Competitividad")

for cargo, puntaje in cargos.items():
    if puntaje >= 27:
        st.success(f"🟢 ALTA PROBABILIDAD → {cargo} ({puntaje})")
    elif 25 <= puntaje < 27:
        st.warning(f"🟡 PROBABILIDAD MEDIA → {cargo} ({puntaje})")
    else:
        st.error(f"🔴 PROBABILIDAD BAJA → {cargo} ({puntaje})")
