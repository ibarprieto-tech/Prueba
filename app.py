import streamlit as st
import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Análisis de Sentimiento RS", layout="wide")

st.title("📊 Análisis de Sentimiento en Redes Sociales")
st.markdown("Esta herramienta analiza el tono emocional de los mensajes utilizando NLP.")

# Sidebar para opciones
st.sidebar.header("Configuración")
metodo = st.sidebar.selectbox("Selecciona la librería de análisis:", ["VADER", "TextBlob"])

# Entrada de datos
st.subheader("📝 Ingreso de Datos")
user_input = st.text_area("Escribe un post o comentario aquí:", "¡Me encanta esta nueva tecnología!")

def analizar_sentimiento(texto, herramienta):
    if herramienta == "VADER":
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(texto)
        score = vs['compound']
    else:
        score = TextBlob(texto).sentiment.polarity
    
    if score > 0.05: return "Positivo", score
    elif score < -0.05: return "Negativo", score
    else: return "Neutro", score

if st.button("Analizar Texto"):
    sentimiento, puntaje = analizar_sentimiento(user_input, metodo)
    
    col1, col2 = st.columns(2)
    col1.metric("Sentimiento", sentimiento)
    col2.metric("Puntaje (Score)", f"{puntaje:.2f}")
    
    if sentimiento == "Positivo": st.success("El mensaje es optimista.")
    elif sentimiento == "Negativo": st.error("El mensaje es crítico o negativo.")
    else: st.warning("El mensaje es imparcial.")

# Separador visual correcto
st.markdown("---")

# Sección para carga de archivos masivos
st.subheader("📂 Análisis por Lote (CSV)")
uploaded_file = st.file_uploader("Sube un archivo CSV con una columna llamada 'texto'", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if 'texto' in df.columns:
        df['Resultado'] = df['texto'].apply(lambda x: analizar_sentimiento(str(x), metodo)[0])
        
        st.write(df.head())
        
        # Gráfico de distribución
        fig = px.pie(df, names='Resultado', title='Distribución de Sentimientos', hole=0.4)
        st.plotly_chart(fig)
    else:
        st.error("El CSV debe tener una columna 'texto'.")
