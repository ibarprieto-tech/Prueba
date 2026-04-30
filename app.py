import streamlit as st
import random
import time

st.set_page_config(page_title="Ecuaciones de 1er grado", page_icon="➗")

# --------- ESTILOS Y EFECTOS ---------
def snow_effect():
    snowflakes = "❄️" * 50
    placeholder = st.empty()
    for _ in range(10):
        placeholder.markdown(
            f"<h1 style='text-align:center; font-size:40px;'>{snowflakes}</h1>",
            unsafe_allow_html=True
        )
        time.sleep(0.1)
        snowflakes = " " + snowflakes[:-2]
    st.success("¡Correcto! 🎉")

st.markdown("""
    <style>
    .big-title {
        font-size:40px !important;
        text-align:center;
        font-weight:bold;
        color:#4CAF50;
    }
    .equation {
        font-size:28px;
        text-align:center;
        margin:20px 0;
        color:#FFFFFF;
        background-color:#222;
        padding:15px;
        border-radius:10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>➗ Practica ecuaciones de primer grado</div>", unsafe_allow_html=True)

# --------- GENERADOR DE ECUACIONES ---------
def generar_ecuacion():
    x = random.randint(0, 10)

    a = random.randint(1, 5)
    b = random.randint(-10, 10)

    c = a * x + b

    return {
        "a": a,
        "b": b,
        "c": c,
        "sol": x
    }

# --------- ESTADO ---------
if "ejercicio" not in st.session_state:
    st.session_state.ejercicio = generar_ecuacion()
    st.session_state.resultado = None

ej = st.session_state.ejercicio

# --------- MOSTRAR ECUACIÓN ---------
ecuacion_texto = f"{ej['a']}x + ({ej['b']}) = {ej['c']}"
st.markdown(f"<div class='equation'>{ecuacion_texto}</div>", unsafe_allow_html=True)

# --------- INPUT USUARIO ---------
respuesta = st.number_input("¿Cuál es el valor de x?", min_value=0, max_value=10, step=1)

# --------- BOTONES ---------
col1, col2 = st.columns(2)

with col1:
    if st.button("✅ Verificar"):
        if respuesta == ej["sol"]:
            snow_effect()
        else:
            st.error(f"❌ Incorrecto. Intenta de nuevo")

with col2:
    if st.button("🔄 Nuevo ejercicio"):
        st.session_state.ejercicio = generar_ecuacion()
        st.rerun()

# --------- PISTA OPCIONAL ---------
with st.expander("💡 Ver pista"):
    st.write("Despeja x pasando términos al otro lado de la ecuación.")
