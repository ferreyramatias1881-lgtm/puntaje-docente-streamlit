import streamlit as st

st.set_page_config(page_title="PuntajeDoc Pro", page_icon="📊")

st.title("📊 PuntajeDoc Pro")
st.subheader("Inteligencia estratégica para actos públicos")

st.divider()

st.header("1️⃣ Perfil del Docente")

listado = st.selectbox(
    "Listado en el que estás inscripto",
    ["Oficial", "108A", "108B", "Emergencia"]
)

distrito = st.selectbox(
    "Distrito principal",
    ["La Matanza", "Merlo", "Cañuelas", "Otro"]
)

st.header("2️⃣ Áreas habilitadas")

areas = st.multiselect(
    "Seleccioná las áreas donde figurás en tu oblea",
    [
        "Equipo de Orientación Escolar (OE)",
        "Equipo de Orientación Escolar (SOE)",
        "Psicología",
        "CENS",
        "Secundaria Ciencias Sociales",
        "Secundaria Filosofía",
        "Primaria",
    ]
)

st.header("3️⃣ Análisis Estratégico")

if st.button("Analizar oportunidades"):

    st.subheader("Resultados")

    if "Equipo de Orientación Escolar (OE)" in areas or "Equipo de Orientación Escolar (SOE)" in areas:
        if listado == "108A":
            st.success("🟢 Alta probabilidad en Equipos de Orientación (cuando se agota listado oficial).")
        else:
            st.success("🟢 Muy buena posición en Equipos de Orientación.")

    if "CENS" in areas:
        st.warning("🟡 Buena oportunidad en CENS, especialmente en suplencias largas.")

    if "Secundaria Ciencias Sociales" in areas or "Secundaria Filosofía" in areas:
        st.warning("🟡 Oportunidades variables según movimiento del distrito.")

    if "Primaria" in areas:
        st.error("🔴 Competencia alta en Primaria, dependerá del puntaje.")

    st.info(f"📍 Recomendación estratégica para {distrito}: revisar actos públicos diariamente en tus áreas fuertes.")
