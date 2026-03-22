import streamlit as st
import datetime
import time
import base64
import os
from pathlib import Path

# --- FUNCIÓN MAESTRA PARA CARGAR TU IMAGEN ---
def get_image_base64():
    nombres_posibles = ["arbol_bonito", "arbol_bonito.png", "arbol_bonito.jpg", "arbol_bonito.jpeg"]
    for nombre in nombres_posibles:
        if os.path.exists(nombre):
            try:
                with open(nombre, "rb") as image_file:
                    return base64.b64encode(image_file.read()).decode()
            except Exception:
                continue
    return None

st.set_page_config(page_title="Flores Amarillas para Ceci", layout="wide")

# --- CSS DEFINITIVO: GIRASOLES IDÉNTICOS Y ANIMACIÓN DE VIENTO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Dancing+Script:wght@600&display=swap');
    
    .stApp { background-color: #fdf5e6; overflow: hidden; }
    header, footer, .stDeployButton {display: none !important;}
    .block-container {padding: 0px !important;}
    
    /* --- ANIMACIÓN DE VIENTO PARA GIRASOLES --- */
    .girasol-viento {
        position: fixed;
        z-index: 1000;
        pointer-events: none;
        opacity: 0;
        /* Usando el girasol exacto de tu imagen */
        color: #fbc02d; /* Amarillo principal */
        text-shadow: 
            0 0 1px #000, /* Delineado negro */
            2px 2px 4px rgba(230, 126, 34, 0.7); /* Pétalos naranja difuminados */
    }

    @keyframes volar {
        0% { transform: translate(0, 0) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translate(var(--dx), 90vh) rotate(var(--dr)); opacity: 0; }
    }

    /* --- CLASES PARA DIFERENTES GIRASOLES Y MOVIMIENTOS --- */
    /* Pequeño, cae a la izquierda y gira rápido */
    .girasol-s { font-size: 20px; animation: volar var(--at) linear infinite; }
    /* Mediano, cae con menos dispersión */
    .girasol-m { font-size: 30px; animation: volar var(--at) linear infinite; }
    /* Grande, cae más lento y recto */
    .girasol-l { font-size: 40px; animation: volar var(--at) linear infinite; }

    .hoja { height: 100vh; display: flex; flex-direction: column; justify-content: center; padding: 0 8%; font-family: 'Montserrat', sans-serif; }
    .texto { font-size: 32px; color: #5d4037; line-height: 1.6; flex: 1; margin-top: 40px;}
    .firma { font-family: 'Dancing Script', cursive; font-size: 60px; color: #d32f2f; margin-top: 20px; }
    .arbol-imagen { width: 450px; filter: drop-shadow(10px 10px 20px rgba(0,0,0,0.1)); }
    
    .reloj-box { border-top: 2px solid #e0d7c0; margin-top: 20px; padding-top: 20px; padding-bottom: 50px;}
    .n { font-size: 50px; font-weight: 700; color: #3e2723; }
    .l { font-size: 22px; color: #a1887f; margin-right: 30px; }
    </style>
    
    <div class="girasol-viento girasol-m" style="top:25%; right:10%; --at: 9s; --dx: -75vw; --dr: 720deg;">🌻</div>
    <div class="girasol-viento girasol-s" style="top:15%; right:20%; --at: 7s; --dx: -60vw; --dr: -360deg;">🌻</div>
    <div class="girasol-vuelo girasol-l" style="top:35%; right:15%; --at: 11s; --dx: -50vw; --dr: 180deg;">🌻</div>
    <div class="girasol-viento girasol-s" style="top:20%; right:5%;  --at: 8s; --dx: -70vw; --dr: 450deg;">🌻</div>
    <div class="girasol-viento girasol-m" style="top:10%; right:25%; --at: 10s; --dx: -85vw; --dr: 360deg;">🌻</div>
    <div class="girasol-vuelo girasol-l" style="top:40%; right:30%; --at: 12s; --dx: -45vw; --dr: -180deg;">🌻</div>
    """, unsafe_allow_html=True)

# Tu fecha especial
fecha_inicio = datetime.datetime(2025, 11, 9, 0, 0, 0)
img_b64 = get_image_base64()

if img_b64:
    img_tag = f'<img src="data:image/png;base64,{img_b64}" class="arbol-imagen">'
else:
    img_tag = '<p style="color:red;">⚠️ No se pudo cargar el archivo "arbol_bonito".</p>'

ph = st.empty()

while True:
    ahora = datetime.datetime.now()
    diff = ahora - fecha_inicio
    d, h, m, s = diff.days, diff.seconds//3600, (diff.seconds//60)%60, diff.seconds%60
    
    ph.markdown(f"""
    <div class="hoja">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div class="texto">
                Flores Amarillas para el<br>amor de mi vida:<br><br>
                Si pudiera elegir un lugar<br>seguro, sería a tu lado.<br><br>
                Cuanto más tiempo estoy<br>contigo más te amo.
                <p class="firma">— I Love You Ceci!</p>
            </div>
            <div>{img_tag}</div>
        </div>
        <div class="reloj-box">
            <div style="color:#8d6e63; font-size:24px; margin-bottom:10px;">Nuestro amor comenzó hace...</div>
            <span class="n">{d}</span> <span class="l">días</span>
            <span class="n">{h:02}</span> <span class="l">h</span>
            <span class="n">{m:02}</span> <span class="l">m</span>
            <span class="n">{s:02}</span> <span class="l">s</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(1)