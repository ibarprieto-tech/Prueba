import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Trivia Rock Peruano", page_icon="🎸")

# Título y estética
st.markdown("""
    <style>
    .main {
        background-color: #121212;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #f04b4c;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎸 Trivia: Vocalistas del Rock Peruano")
st.write("¿Qué tanto sabes sobre las voces que marcaron la historia del rock nacional?")

# Definición de las preguntas
if 'questions' not in st.session_state:
    st.session_state.questions = [
        {
            "id": 1,
            "pregunta": "¿Quién es el vocalista principal de la banda 'Mar de Copas'?",
            "opciones": ["Wicho García", "Salim Vera", "Daniel F", "Jhovan Tomasevich"],
            "correcta": "Wicho García"
        },
        {
            "id": 2,
            "pregunta": "¿Qué cantante lideró la banda 'Arena Hash' junto a su hermano Patricio?",
            "opciones": ["Pedro Suárez-Vértiz", "Christian Meier", "Miki González", "Pelo Madueño"],
            "correcta": "Pedro Suárez-Vértiz"
        },
        {
            "id": 3,
            "pregunta": "Es el líder y voz emblemática de la banda punk 'Leusemia':",
            "opciones": ["Daniel F", "Raúl Montañez", "Cachorro Vial", "Kimba Vilis"],
            "correcta": "Daniel F"
        },
        {
            "id": 4,
            "pregunta": "¿Quién es el vocalista y guitarrista de la banda 'Amén'?",
            "opciones": ["Marcello Motta", "Salim Vera", "Lucho Quequezana", "Andrés Dulude"],
            "correcta": "Marcello Motta"
        },
        {
            "id": 5,
            "pregunta": "¿Quién fue la voz principal de 'Libido' durante su etapa de mayor éxito internacional?",
            "opciones": ["Salim Vera", "Toño Jáuregui", "Jeffry Fischman", "Manolo Hidalgo"],
            "correcta": "Salim Vera"
        }
    ]
    # Aleatorizar el orden de las opciones para cada pregunta al inicio
    for q in st.session_state.questions:
        random.shuffle(q["opciones"])

# Inicialización del estado
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'finished' not in st.session_state:
    st.session_state.finished = False

def restart_game():
    st.session_state.current_step = 0
    st.session_state.score = 0
    st.session_state.finished = False
    # Re-shuffling para un nuevo intento
    for q in st.session_state.questions:
        random.shuffle(q["opciones"])

# Lógica del Juego
if not st.session_state.finished:
    step = st.session_state.current_step
    q_data = st.session_state.questions[step]

    st.subheader(f"Pregunta {step + 1} de 5")
    st.info(q_data["pregunta"])

    # Mostrar opciones como botones
    for opcion in q_data["opciones"]:
        if st.button(opcion, key=f"btn_{step}_{opcion}"):
            if opcion == q_data["correcta"]:
                st.session_state.score += 1
            
            if step + 1 < len(st.session_state.questions):
                st.session_state.current_step += 1
                st.rerun()
            else:
                st.session_state.finished = True
                st.rerun()

else:
    # Pantalla de resultados
    st.success("¡Has completado la trivia!")
    final_score = st.session_state.score
    st.metric("Tu Puntaje", f"{final_score}/5")

    if final_score == 5:
        st.balloons()
        st.markdown("### 🏆 ¡Eres un verdadero conocedor del Rock Peruano! 🏆")
        st.write("Has acertado todas las preguntas. ¡Salud por eso!")
    elif final_score >= 3:
        st.write("¡Nada mal! Conoces bien la escena local.")
    else:
        st.write("Te falta escuchar un poco más de 'Disco Eterno' o 'Libido'. ¡Inténtalo de nuevo!")

    if st.button("Reintentar Trivia"):
        restart_game()
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.write("Hecho con ❤️ para los fans del Rock Peruano")
