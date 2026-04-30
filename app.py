import streamlit as st
import streamlit as st
import random

st.set_page_config(page_title="Trivia Rock Peruano", page_icon="🎸")

st.title("🎸 Trivia: Rock Peruano")
st.write("Responde correctamente las 5 preguntas sobre cantantes de bandas peruanas.")

# Preguntas (pregunta, opciones, respuesta correcta)
preguntas = [
    {
        "pregunta": "¿Quién fue el vocalista principal de Soda Stereo en sus inicios en Perú?",
        "opciones": ["Pedro Suárez-Vértiz", "Gustavo Cerati", "Miki González", "Daniel F"],
        "respuesta": "Gustavo Cerati"
    },
    {
        "pregunta": "¿Quién es el vocalista de la banda peruana Libido?",
        "opciones": ["Salim Vera", "Julio Andrade", "Pelo Madueño", "Wicho García"],
        "respuesta": "Salim Vera"
    },
    {
        "pregunta": "¿Quién fue el cantante principal de Arena Hash?",
        "opciones": ["Pedro Suárez-Vértiz", "Gian Marco", "Christian Meier", "Raúl Romero"],
        "respuesta": "Pedro Suárez-Vértiz"
    },
    {
        "pregunta": "¿Quién es el vocalista de Mar de Copas?",
        "opciones": ["Wicho García", "Salim Vera", "Pedro Suárez-Vértiz", "Jean Pierre Magnet"],
        "respuesta": "Wicho García"
    },
    {
        "pregunta": "¿Quién es el líder y vocalista de Leusemia?",
        "opciones": ["Daniel F", "Miki González", "Pelo Madueño", "Raúl Romero"],
        "respuesta": "Daniel F"
    }
]

# Mezclar preguntas
random.shuffle(preguntas)

if "respuestas_usuario" not in st.session_state:
    st.session_state.respuestas_usuario = {}

# Mostrar preguntas
for i, q in enumerate(preguntas):
    opciones = q["opciones"].copy()
    random.shuffle(opciones)

    respuesta = st.radio(
        f"{i+1}. {q['pregunta']}",
        opciones,
        key=f"pregunta_{i}"
    )
    st.session_state.respuestas_usuario[i] = respuesta

# Botón para evaluar
if st.button("Ver resultado"):
    puntaje = 0

    for i, q in enumerate(preguntas):
        if st.session_state.respuestas_usuario[i] == q["respuesta"]:
            puntaje += 1

    st.subheader(f"Tu puntaje: {puntaje}/5")

    if puntaje == 5:
        st.success("¡Perfecto! 🎉 Sabes mucho de rock peruano 🤘")
        st.balloons()  # Animación 🎈
    else:
        st.warning("Sigue intentando 😄")
st.write("Hola mundo")
