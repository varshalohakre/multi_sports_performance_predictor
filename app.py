import streamlit as st
import joblib
import plotly.graph_objects as go
import pandas as pd

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Multi-Sport Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# LOAD MODELS
# =========================

cricket_model = joblib.load("cricket_model.pkl")
basketball_model = joblib.load("basketball_model.pkl")
football_model = joblib.load("football_model.pkl")

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>
:root {
    --primary: #7c3aed;
    --secondary: #06b6d4;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

.title {
    font-size: 3rem;
    font-weight: 700;
    letter-spacing: -1px;
    margin-bottom: 0.5rem;
}

.subtitle {
    color: #9ca3af;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

.card {
    border-radius: 20px;
    padding: 1.5rem;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 1.5rem;
}

.gradient-text {
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.metric-card {
    padding: 1.2rem;
    border-radius: 18px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    text-align: center;
}

.metric-card h1 {
    font-size: 2rem;
}

section[data-testid="stSidebar"] {
    border-right: 1px solid rgba(255,255,255,0.08);
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
<div class="title">
   <span class="gradient-text">
     Multi-Sport Performance Predictor
   </span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Predict fantasy-style athlete performance using sport-specific machine learning models.
</div>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.markdown("""
    <h2 style='margin-bottom: 0.5rem;'>
    Select Sport
    </h2>
    """, unsafe_allow_html=True)

    st.caption("Choose a sport to predict athlete performance.")

    sport = st.selectbox(
        "",
        ["Cricket", "Basketball", "Football"]
    )

# =========================
# INPUT SECTION
# =========================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader(f"{sport} Performance Metrics")

if sport == "Cricket":

    col1, col2, col3 = st.columns(3)

    with col1:
        balls = st.number_input(
            "Balls Faced",
            min_value=0,
            step=1
        )

    with col2:
        fours = st.number_input(
            "Fours",
            min_value=0,
            step=1
        )

    with col3:
        sixes = st.number_input(
            "Sixes",
            min_value=0,
            step=1
        )

elif sport == "Basketball":

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        past_avg_pts = st.number_input(
            "Average Points",
            min_value=0.0,
            step=1.0
        )

    with col2:
        past_avg_ast = st.number_input(
            "Average Assists",
            min_value=0.0,
            step=1.0
        )

    with col3:
        past_avg_trb = st.number_input(
            "Average Rebounds",
            min_value=0.0,
            step=1.0
        )

    with col4:
        past_avg_mp = st.number_input(
            "Average Minutes",
            min_value=0.0,
            step=1.0
        )

elif sport == "Football":

    col1, col2, col3 = st.columns(3)

    with col1:
        minutes = st.number_input(
            "Minutes Played",
            min_value=0.0,
            step=10.0
        )

        xg = st.number_input(
            "Expected Goals (xG)",
            min_value=0.0,
            step=0.5
        )

        xag = st.number_input(
            "Expected Assisted Goals (xAG)",
            min_value=0.0,
            step=0.5
        )

    with col2:
        sot = st.number_input(
            "Shots on Target",
            min_value=0.0,
            step=1.0
        )

        kp = st.number_input(
            "Key Passes",
            min_value=0.0,
            step=1.0
        )

        sca = st.number_input(
            "Shot-Creating Actions",
            min_value=0.0,
            step=1.0
        )

    with col3:
        prgc = st.number_input(
            "Progressive Carries",
            min_value=0.0,
            step=1.0
        )

        prgp = st.number_input(
            "Progressive Passes",
            min_value=0.0,
            step=1.0
        )

        prgr = st.number_input(
            "Progressive Receptions",
            min_value=0.0,
            step=1.0
        )

    col4, col5, col6, col7 = st.columns(4)

    with col4:
        tackles = st.number_input(
            "Tackles",
            min_value=0.0,
            step=1.0
        )

    with col5:
        interceptions = st.number_input(
            "Interceptions",
            min_value=0.0,
            step=1.0
        )

    with col6:
        yellow_cards = st.number_input(
            "Yellow Cards",
            min_value=0.0,
            step=1.0
        )

    with col7:
        red_cards = st.number_input(
            "Red Cards",
            min_value=0.0,
            step=1.0
        )

predict = st.button(
    "Predict Performance",
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# PREDICTION SECTION
# =========================

if predict:

    if sport == "Cricket":

        if fours + sixes > balls:
            st.error("Invalid input: Total boundaries cannot exceed balls faced.")
            st.stop()

        input_data = pd.DataFrame(
            [[balls, fours, sixes]],
            columns=[
                "balls",
                "fours",
                "sixes"
            ]
        )

        prediction = cricket_model.predict(input_data)
        score = prediction[0]

        model_accuracy = 82.0
        avg_score = 45
        top_score = 120
        dtick_value = 10
        xaxis_range = [0, max(140, score + 20)]

    elif sport == "Basketball":

        input_data = pd.DataFrame(
            [[
                past_avg_pts,
                past_avg_ast,
                past_avg_trb,
                past_avg_mp
            ]],
            columns=[
                "past_avg_pts",
                "past_avg_ast",
                "past_avg_trb",
                "past_avg_mp"
            ]
        )

        prediction = basketball_model.predict(input_data)
        score = prediction[0]

        model_accuracy = 41.2
        avg_score = 250
        top_score = 450
        dtick_value = 50
        xaxis_range = [0, max(500, score + 50)]

    elif sport == "Football":

        if red_cards > 2:
            st.error("Invalid input: Red cards should not be greater than 2 for a player.")
            st.stop()

        input_data = pd.DataFrame(
            [[
                minutes,
                xg,
                xag,
                sot,
                kp,
                prgc,
                prgp,
                prgr,
                sca,
                tackles,
                interceptions,
                yellow_cards,
                red_cards
            ]],
            columns=[
                "Min",
                "xG",
                "xAG",
                "SoT",
                "KP",
                "PrgC",
                "PrgP",
                "PrgR",
                "SCA",
                "Tkl",
                "Int",
                "CrdY",
                "CrdR"
            ]
        )

        prediction = football_model.predict(input_data)
        score = prediction[0]

        model_accuracy = 96.1
        avg_score = 150
        top_score = 450
        dtick_value = 50
        xaxis_range = [0, max(500, score + 50)]

    lower = score * 0.9
    upper = score * 1.1

    # =========================
    # RESULT CARDS
    # =========================

    st.markdown("## Prediction Results")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Predicted Performance Score</h3>
            <h1>{score:.2f}</h1>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Model R² Score</h3>
            <h1>{model_accuracy:.1f}%</h1>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Expected Range</h3>
            <h1>{lower:.1f} - {upper:.1f}</h1>
        </div>
        """, unsafe_allow_html=True)

    # =========================
    # CHART
    # =========================

    fig = go.Figure()

    fig.add_bar(
        x=[
            score,
            avg_score,
            top_score
        ],
        y=[
            "Predicted Score",
            "Average Player",
            "Top Performance"
        ],
        orientation="h"
    )

    fig.update_layout(
        title=f"{sport} Performance Comparison",
        height=400,
        template="plotly_dark",
        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),
        xaxis=dict(
            title="Fantasy Performance Points",
            tickmode="linear",
            tick0=0,
            dtick=dtick_value,
            range=xaxis_range,
            showgrid=True,
            gridwidth=1,
            showticklabels=True,
            tickfont=dict(
                size=14,
                
            )
        ),
        yaxis=dict(
            tickfont=dict(
                size=14,
                
            )
        )
    )

    st.plotly_chart(
        fig,
        width='stretch',
        key=f"{sport}_performance_chart"
    )