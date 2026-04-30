import streamlit as st

# Configuración inicial de la base de conocimientos (Árbol binario)
# Cada nodo tiene una 'pregunta'. Si es un 'personaje', es un nodo hoja.
def iniciar_arbol():
    return {
        "pregunta": "¿Tu personaje es real?",
        "si": {
            "pregunta": "¿Es un deportista?",
            "si": {"personaje": "Lionel Messi"},
            "no": {"personaje": "Albert Einstein"}
        },
        "no": {
            "pregunta": "¿Tiene superpoderes?",
            "si": {"personaje": "Spider-Man"},
            "no": {"personaje": "Sherlock Holmes"}
        }
    }

st.title("🧙‍♂️ El Adivino de Personajes")
st.write("Piensa en un personaje y responderé con honestidad.")

# Inicializar el estado del juego
if 'nodo_actual' not in st.session_state:
    st.session_state.arbol = iniciar_arbol()
    st.session_state.nodo_actual = st.session_state.arbol
    st.session_state.juego_terminado = False

def reiniciar_juego():
    st.session_state.nodo_actual = st.session_state.arbol
    st.session_state.juego_terminado = False

# Lógica del juego
if not st.session_state.juego_terminado:
    nodo = st.session_state.nodo_actual
    
    if "pregunta" in nodo:
        st.subheader(nodo["pregunta"])
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Sí", use_container_width=True):
                st.session_state.nodo_actual = nodo["si"]
                st.rerun()
        
        with col2:
            if st.button("No", use_container_width=True):
                st.session_state.nodo_actual = nodo["no"]
                st.rerun()
    else:
        # Hemos llegado a un personaje
        st.success(f"¡Tu personaje es: **{nodo['personaje']}**!")
        st.session_state.juego_terminado = True
        st.balloons()

if st.session_state.juego_terminado:
    if st.button("Jugar de nuevo"):
        reiniciar_juego()
        st.rerun()
