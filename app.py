import streamlit as st

st.set_page_config(page_title="Calculadora Puntaje Docente", page_icon="📚")

st.title("📚 Calculadora de Puntaje Docente")
st.write("Simulador básico para Provincia de Buenos Aires")

st.divider()

st.subheader("Antigüedad")

anios_antiguedad = st.number_input("Años de antigüedad", min_value=0, max_value=50, value=0)
puntaje_antiguedad = anios_antiguedad * 0.50

st.subheader("Cursos")

cantidad_cursos = st.number_input("Cantidad de cursos aprobados", min_value=0, max_value=100, value=0)
puntaje_cursos = cantidad_cursos * 0.20

st.subheader("Títulos")

titulo_extra = st.checkbox("Posee título adicional")
puntaje_titulo = 1.0 if titulo_extra else 0

st.divider()

total = puntaje_antiguedad + puntaje_cursos + puntaje_titulo

st.subheader("Resultado")

st.write(f"Puntaje por antigüedad: {puntaje_antiguedad:.2f}")
st.write(f"Puntaje por cursos: {puntaje_cursos:.2f}")
st.write(f"Puntaje por título adicional: {puntaje_titulo:.2f}")

st.success(f"Puntaje Total: {total:.2f}")
