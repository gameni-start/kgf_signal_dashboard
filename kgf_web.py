import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="KGFsignalCraft", layout="centered")

# 💼 Header visuel
st.markdown("<h1 style='text-align:center; color:#F5C518;'>KGFsignalCraft</h1>", unsafe_allow_html=True)
st.image("kgf_banner.jpeg", use_container_width=True)
st.markdown("<h4 style='text-align:center; color:white;'>Du silence des moqueries à la puissance des résultats.</h4>", unsafe_allow_html=True)

try:
    # 📥 Lecture des données
    df = pd.read_csv("performance.csv", header=None, names=["timestamp", "symbol", "direction", "signal_type", "result_usd"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="%Y-%m-%dT%H:%M:%S.%f")
    df["day"] = df["timestamp"].dt.date

    # ⏳ Sélection manuelle d'une date
    target_date = datetime(2025, 7, 22).date()
    today = df[df["day"] == target_date]

    # 📊 Stats globales
    call_count = len(today[today["direction"] == "CALL"])
    put_count  = len(today[today["direction"] == "PUT"])
    wins       = (today["result_usd"].astype(float) >= 0).sum()
    pnl        = today["result_usd"].astype(float).sum()
    ratio      = round((wins / len(today)) * 100, 2) if len(today) else 0

    # 💎 Résumé stylisé
    st.markdown("""
    <div style='border:1px solid #444; border-radius:10px; padding:15px; background-color:#111; color:#eee;'>
        <h4 style='text-align:center;'>📊 Résumé du {} :</h4>
        <ul style='list-style:none; padding-left:0; font-size:16px;'>
            <li>✅ <b>CALL</b> : {}</li>
            <li>🔻 <b>PUT</b> : {}</li>
            <li>⚖️ <b>Ratio victoire</b> : {}%</li>
            <li>💰 <b>P&L</b> : {:.2f} USD</li>
        </ul>
    </div>
    """.format(target_date.strftime("%d %B %Y"), call_count, put_count, ratio, pnl), unsafe_allow_html=True)

    # 📈 Histogramme CALL vs PUT
    fig1 = px.histogram(today, x='direction', color='direction', title='Distribution des signaux',
                        color_discrete_map={"CALL":"#00CC96", "PUT":"#EF553B"})
    st.plotly_chart(fig1, use_container_width=True)

    # 📈 Courbe P&L cumulé
    today["pnl_cumulé"] = today["result_usd"].astype(float).cumsum()
    fig2 = px.line(today, x="timestamp", y="pnl_cumulé", title="Évolution du P&L (cumulé)", markers=True)
    st.plotly_chart(fig2, use_container_width=True)

    # 🏆 Top Pairs du jour
    top_pairs = today.groupby("symbol")["result_usd"].sum().sort_values(ascending=False).head(5)
    st.markdown("### 🏆 Top Pairs du jour")
    st.table(top_pairs.reset_index().rename(columns={"result_usd": "P&L total"}))

    # 📋 Tableau complet des signaux
    st.markdown("### 📋 Détails des signaux")
    st.dataframe(today[["timestamp", "symbol", "direction", "signal_type", "result_usd"]].style.format({
        "result_usd":"{:.2f}"
    }), use_container_width=True)

except Exception as e:
    st.error(f"📛 Erreur chargement des données : {e}")

# 👥 Compteur Telegram (statique ou API futur)
st.markdown("""
<div style='text-align:center; margin-top:40px;'>
    <h4>👥 Membres Telegram : <span style='color:#F5C518;'>+120</span></h4>
</div>
""", unsafe_allow_html=True)

# 📢 Lien Telegram stylisé
st.markdown("""
<div style='text-align:center; margin-top:15px;'>
    <a href='https://t.me/kgfempiredigital' target='_blank'>
        <button style='background-color:#F5C518; color:black; padding:12px 24px; font-size:18px; border:none; border-radius:8px;'>
            📢 Rejoindre le canal Telegram
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# 🔴 WebSocket zone (à venir)
st.markdown("""
<div style='margin-top:50px;'>
    <h4>🔴 Signaux en direct (bientôt disponibles)</h4>
    <p style='color:gray;'>Le bot sera connecté en WebSocket pour affichage live des signaux.</p>
</div>
""", unsafe_allow_html=True)

# 👣 Footer
st.markdown("---")
st.markdown("<div style='text-align:center; font-size:14px;'>© 2025 — KGFsignalCraft par François</div>", unsafe_allow_html=True)
