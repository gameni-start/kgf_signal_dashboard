import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="kgfsignalCraft Bot | Vitrine",
    layout="wide",
    page_icon="⚡"
)

# === BANNIÈRE STRATÉGIQUE ===
st.markdown("""
<div style="
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    padding: 40px 25px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 0 15px rgba(0,0,0,0.3);
">
  <h1 style="color: #FFD700; font-size: 3em; margin-bottom: 0;">⚡ kgfsignalCraft Bot</h1>
  <p style="color: #DDDDDD; font-size: 1.1em;">Optimisation stratégique des signaux binaires</p>
  <p style="color: #AAAAAA; font-size: 0.9em; font-style: italic;">Par François | KGF Empire Digital</p>
</div>
""", unsafe_allow_html=True)

# === LOGO CENTRAL INTÉGRÉ ===
st.markdown("<center><img src='kgf_logo.png' width='130'></center>", unsafe_allow_html=True)

# === SECTION STATISTIQUES ===
st.markdown("## 📊 Statistiques de performance")
try:
    df = pd.read_csv("performance.csv")
    st.dataframe(df, use_container_width=True)
    if "ratio" in df.columns:
        st.line_chart(df["ratio"])
        st.success("✅ Statistiques mises à jour automatiquement.")
except Exception as e:
    st.warning(f"⚠️ Données non disponibles : {e}")

# === VALEUR AJOUTÉE KGF ===
st.markdown("## 💡 Ce que kgfsignalCraft vous apporte")
st.markdown("""
- 📌 Analyse multi-indicateurs CALL/PUT (non-automatisée)
- 📈 Fiabilité IA testée en environnement réel
- 🧠 Dashboard orienté précision et transparence
- 🛰️ Orienté scalabilité et branding visuel
""")

# === TÉMOIGNAGES CLIENTS ===
st.markdown("## 🗣️ Témoignages")
st.markdown("""
> “Ce projet sort du lot. On sent le travail derrière chaque signal.”  
— **Khalid M.**, trader francophone 🇲🇦

> “KGF c’est une vraie stratégie, pas juste un bot.”  
— **Cindy F.**, analyste en binaires 📊

> “La clarté des tableaux et l’approche Telegram sont top.”  
— **Jean-Michel**, utilisateur actif 🧠
""")

# === ÉQUIPE KGF ===
st.markdown("## 👥 Équipe KGF")
cols = st.columns(3)
with cols[0]:
    st.markdown("### François")
    st.markdown("🧠 Fondateur, IA Strategist")
    st.markdown("📍 Douala, Cameroun")

with cols[1]:
    st.markdown("### KGF Bot")
    st.markdown("🔹 Outil d’analyse multi-modèle")
    st.markdown("🔹 Moteur de scoring adaptatif")

with cols[2]:
    st.markdown("### Communauté")
    st.markdown("🔹 Testeurs et Traders")
    st.markdown("🔹 Groupe Telegram privé")

# === CALL TO ACTION ===
st.markdown("## 📩 Rejoignez le QG Telegram")
st.markdown("""
<div style="
    background-color: #111;
    padding: 30px;
    border-radius: 12px;
    color: #EEE;
    text-align: center;
    box-shadow: 0 0 10px rgba(255,215,0,0.2);
">
  <h2 style="color: #FFD700;">Commencez maintenant</h2>
  <p>Recevez les résultats & signaux en direct via notre channel Telegram :</p>
  <a href='https://t.me/kgfempiredigital' target='_blank' style="
      background-color: #FFD700;
      color: black;
      padding: 10px 20px;
      border-radius: 5px;
      font-weight: bold;
      text-decoration: none;
      box-shadow: 0 2px 5px rgba(0,0,0,0.3);
  ">📲 Rejoindre le Telegram</a>
</div>
""", unsafe_allow_html=True)

# === SIGNATURE FINALE ===
st.markdown("---")
st.markdown("""
<div style="text-align:center; font-size:0.9em; color:gray; font-style:italic;">
Site vitrine propulsé par <strong>KGF Empire Digital</strong><br>
Designed by François | Vision & Code stratégique 💼📈
</div>
""", unsafe_allow_html=True)
