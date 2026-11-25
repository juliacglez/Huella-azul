import os
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components

# ==============================================================================
# 1. PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Huella Azul | Water & Choices in Irapuato",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

URL_HERO_SEA = "https://cdn.pixabay.com/photo/2023/02/15/19/28/sea-7792564_1280.jpg"
URL_RIVERS_NEW = "https://tse1.mm.bing.net/th/id/OIP.oCWIJDRcBQsoYehMrU-G0AHaEK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
URL_SDG6 = "https://espacio-obra.com/wp-content/uploads/2025/08/ODS-6-scaled.png"
URL_SDG12 = "https://www.cooperacionespanola.es/wp-content/uploads/2023/09/recurso-12-1024x1024.png"
URL_VIDEO_HUELLA_AZUL = "https://www.youtube.com/watch?v=AnIR7CY3HxI"

# ==============================================================================
# 2. CUSTOM CSS STYLES (HUELLA AZUL)
# ==============================================================================
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html {{
        scroll-behavior: smooth;
    }}

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #0F172A;
    }}

    .stApp {{
        background-color: #FFFFFF;
    }}

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}

    .block-container {{
        padding-top: 2.2rem !important;
        padding-bottom: 0rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
        max-width: 1280px;
    }}

    /* Top Bar */
    .top-nav-wrap {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.75rem 0 1.1rem 0;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 1rem;
        flex-wrap: wrap;
        gap: 0.75rem;
    }}

    .brand-logo {{
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        font-weight: 800;
        font-size: 1.15rem;
        color: #082F49;
        letter-spacing: 0.4px;
    }}

    .brand-logo span {{
        color: #14B8A6;
    }}

    .nav-subtitle {{
        font-size: 0.84rem;
        font-weight: 600;
        color: #475569;
    }}

    /* Hero with visible sea background + attached SDG badges */
    .hero-section {{
        position: relative;
        background:
            linear-gradient(120deg, rgba(4, 24, 38, 0.84) 0%, rgba(8, 47, 73, 0.68) 58%, rgba(13, 148, 136, 0.38) 100%),
            url("{URL_HERO_SEA}") center center / cover no-repeat;
        background-color: #06283D;
        color: #FFFFFF;
        padding: 3.4rem 3.2rem;
        border-radius: 20px;
        margin-bottom: 3.5rem;
        box-shadow: 0 18px 40px rgba(8, 47, 73, 0.16);
    }}

    .hero-grid {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 2rem;
        flex-wrap: wrap;
    }}

    .hero-main-col {{
        flex: 1.55;
        min-width: 280px;
    }}

    .hero-badges-panel {{
        display: flex;
        gap: 0.9rem;
        flex-wrap: wrap;
    }}

    .hero-side-badge {{
        background: rgba(8, 47, 73, 0.72);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 18px;
        padding: 0.9rem;
        width: 175px;
        text-align: center;
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.22);
    }}

    .hero-side-badge img {{
        width: 100%;
        max-width: 132px;
        border-radius: 12px;
        margin-bottom: 0.55rem;
    }}

    .hero-tag {{
        font-size: 0.74rem;
        text-transform: uppercase;
        letter-spacing: 1.8px;
        color: #5EEAD4;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }}

    .hero-h1 {{
        font-size: 2.85rem;
        font-weight: 800;
        line-height: 1.12;
        color: #FFFFFF;
        max-width: 680px;
        margin-bottom: 1rem;
    }}

    .hero-p {{
        font-size: 1rem;
        color: #F1F5F9;
        max-width: 640px;
        line-height: 1.6;
        margin-bottom: 1.6rem;
    }}

    .hero-stats {{
        display: flex;
        gap: 3rem;
        padding-top: 1.4rem;
        border-top: 1px solid rgba(255, 255, 255, 0.22);
        flex-wrap: wrap;
    }}

    .stat-num {{
        font-size: 1.75rem;
        font-weight: 800;
        color: #FFFFFF;
        line-height: 1.15;
    }}

    .stat-caption {{
        font-size: 0.82rem;
        color: #E2E8F0;
        max-width: 320px;
        margin-top: 0.25rem;
        line-height: 1.45;
    }}

    /* Section Headings */
    .sec-eyebrow {{
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 1.6px;
        color: #0D9488;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }}

    .sec-title {{
        font-size: 2.15rem;
        font-weight: 800;
        color: #082F49;
        line-height: 1.15;
        margin-bottom: 0.55rem;
    }}

    .sec-desc {{
        font-size: 0.98rem;
        color: #475569;
        max-width: 760px;
        line-height: 1.58;
        margin-bottom: 1.8rem;
    }}

    .circular-box {{
        background: #F0FDFA;
        border: 1px solid #99F6E4;
        border-left: 5px solid #0D9488;
        border-radius: 14px;
        padding: 1.1rem 1.35rem;
        margin-bottom: 1.5rem;
        color: #0F172A;
        font-size: 0.92rem;
        line-height: 1.55;
    }}

    .connection-strip {{
        background: #EFF6FF;
        border: 1px solid #BFDBFE;
        border-left: 5px solid #0284C7;
        border-radius: 14px;
        padding: 1.1rem 1.35rem;
        margin-bottom: 1.8rem;
        color: #0F172A;
        font-size: 0.92rem;
        line-height: 1.55;
    }}

    .action-links-strip {{
        background-color: #F0FDFA;
        border: 1px solid #99F6E4;
        border-left: 5px solid #0D9488;
        border-radius: 16px;
        padding: 1.3rem 1.5rem;
        margin-top: 1.6rem;
        color: #0F172A;
        font-size: 0.9rem;
        line-height: 1.6;
    }}

    .action-links-strip a {{
        color: #0369A1;
        font-weight: 700;
        text-decoration: none;
    }}

    .action-links-strip a:hover {{
        text-decoration: underline;
    }}

    .video-section-card {{
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 20px;
        padding: 1.8rem;
        margin-top: 1.8rem;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
    }}

    .ref-note {{
        font-size: 0.78rem;
        color: #64748B;
        margin-top: 0.45rem;
        font-style: italic;
    }}

    .apa-box {{
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #082F49;
        border-radius: 14px;
        padding: 1.3rem 1.5rem;
        margin-top: 1.4rem;
        color: #334155;
        font-size: 0.85rem;
        line-height: 1.65;
    }}

    .apa-entry {{
        padding-left: 2rem;
        text-indent: -2rem;
        margin-bottom: 0.65rem;
    }}

    /* White Cards */
    .info-card {{
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 18px;
        padding: 1.6rem;
        box-shadow: 0 6px 20px rgba(15, 23, 42, 0.04);
    }}

    .card-top-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.8rem;
    }}

    .pill-blue {{
        background-color: #E0F2FE;
        color: #0369A1;
        font-size: 0.72rem;
        font-weight: 700;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
    }}

    .pill-teal {{
        background-color: #CCFBF1;
        color: #0F766E;
        font-size: 0.72rem;
        font-weight: 700;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
    }}

    .card-h3 {{
        font-size: 1.25rem;
        font-weight: 800;
        color: #082F49;
        margin-bottom: 0.45rem;
    }}

    .card-p {{
        font-size: 0.9rem;
        color: #475569;
        line-height: 1.55;
        margin-bottom: 0.8rem;
    }}

    /* Rivers / Processes Section */
    .river-visual-box {{
        position: relative;
        background:
            linear-gradient(180deg, rgba(8, 47, 73, 0.08) 0%, rgba(8, 47, 73, 0.48) 100%),
            url("{URL_RIVERS_NEW}") center center / cover no-repeat;
        border-radius: 20px;
        min-height: 360px;
        padding: 2rem;
        display: flex;
        align-items: flex-end;
        overflow: hidden;
        border: 1px solid #E2E8F0;
    }}

    .floating-mini-card {{
        background-color: #FFFFFF;
        border-radius: 14px;
        padding: 0.95rem 1.2rem;
        box-shadow: 0 12px 28px rgba(8, 47, 73, 0.24);
        max-width: 315px;
        border: 1px solid #E2E8F0;
    }}

    .proc-item {{
        display: flex;
        align-items: flex-start;
        gap: 0.95rem;
        padding: 0.9rem 0;
        border-bottom: 1px solid #F1F5F9;
    }}

    .proc-icon-circle {{
        width: 34px;
        height: 34px;
        min-width: 34px;
        border-radius: 50%;
        background-color: #F0FDFA;
        border: 1px solid #99F6E4;
        color: #0F766E;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.95rem;
        margin-top: 2px;
    }}

    /* Dark Scenarios Section */
    .dark-band {{
        background: radial-gradient(circle at 85% 20%, rgba(20, 184, 166, 0.22), transparent 45%), #06283D;
        color: #FFFFFF;
        padding: 3.2rem 2.8rem;
        border-radius: 22px;
        margin: 3.5rem 0;
    }}

    .scenario-panel {{
        background-color: #FFFFFF;
        color: #0F172A;
        border-radius: 18px;
        padding: 1.8rem;
        margin-top: 1.4rem;
    }}

    .scenario-left-box {{
        background-color: #F0FDFA;
        border: 1px solid #CCFBF1;
        border-radius: 14px;
        padding: 1.4rem;
    }}

    /* Youth Minigame */
    .game-arena {{
        background: linear-gradient(145deg, #F0FDFA 0%, #E0F2FE 100%);
        border: 1px solid #BAE6FD;
        border-radius: 22px;
        padding: 2.2rem;
        margin-top: 3.2rem;
    }}

    /* Questionnaire Dark Block */
    .closing-dark-box {{
        background: linear-gradient(135deg, #06283D 0%, #082F49 100%);
        color: #FFFFFF;
        border-radius: 22px;
        padding: 2.6rem;
        margin-top: 3.2rem;
    }}

    /* Footer */
    .footer-dark {{
        background-color: #041C2C;
        color: #CBD5E1;
        padding: 2.5rem 3rem;
        margin-top: 3.5rem;
        border-radius: 20px 20px 0 0;
        font-size: 0.84rem;
    }}

    div.stButton > button {{
        background-color: #2DD4BF;
        color: #042436;
        font-weight: 700;
        border: none;
        border-radius: 10px;
        padding: 0.55rem 1.2rem;
    }}

    div.stButton > button:hover {{
        background-color: #14B8A6;
        color: #FFFFFF;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 3. LOCAL DATA (CONCRETE HOME, SCHOOL, STREET & POLICY ACTIONS)
# ==============================================================================
@st.cache_data
def load_irapuato_data() -> pd.DataFrame:
    return pd.DataFrame([
        {
            "Name": "Snack Bag = Glasses of Water",
            "Category": "Everyday Connection",
            "Topic": "Snacks & Crops",
            "Scope": "Individual",
            "Impact": "Medium",
            "Description": "Eating a bag of chips is like grabbing a couple of glasses of water—growing crops, frying, and making packaging all use water (Water Footprint Network, 2023).",
        },
        {
            "Name": "Close Tap While Brushing & Soaping",
            "Category": "Home Action",
            "Topic": "Bathroom Sink",
            "Scope": "Individual",
            "Impact": "Positive",
            "Description": "Turn the sink faucet off while brushing your teeth in the morning and at night, and keep showers around 5 minutes (UN-Water, 2023).",
        },
        {
            "Name": "Put a Filled Water Bottle in the Fridge",
            "Category": "Home Action",
            "Topic": "Cold Drinking Water",
            "Scope": "Individual",
            "Impact": "Positive",
            "Description": "Keep a pitcher or bottle cold in the fridge instead of letting the tap run until cold water comes out (UN-Water, 2023).",
        },
        {
            "Name": "Use One Reusable Plate or Cup at Home",
            "Category": "Home Action",
            "Topic": "Kitchen Routine",
            "Scope": "Individual",
            "Impact": "Positive",
            "Description": "Grab one cup or plate for the day instead of using several disposable cups or extra dishes for snacks (UNEP, 2024).",
        },
        {
            "Name": "Pack Only the Food You Will Eat",
            "Category": "School & Home Action",
            "Topic": "Lunchbox & Portions",
            "Scope": "Individual",
            "Impact": "Positive",
            "Description": "Serve smaller portions at home or school and save leftovers in a container so food—and its hidden water—is not thrown away (FAO, 2021).",
        },
        {
            "Name": "Refill Your Bottle at School",
            "Category": "School Action",
            "Topic": "Backpack & Hydration",
            "Scope": "Community",
            "Impact": "Positive",
            "Description": "Bring a reusable bottle to classes in Irapuato and refill it instead of buying single-use plastic bottles every day (UNEP, 2024).",
        },
        {
            "Name": "Report Dripping Taps or Running Toilets",
            "Category": "School & Home Action",
            "Topic": "Leak Check",
            "Scope": "Community",
            "Impact": "High",
            "Description": "Tell your family at home or a teacher/staff member at school right away if a faucet drips or a toilet keeps running (JAPAMI, 2024; UN-Water, 2023).",
        },
        {
            "Name": "Drop Wrappers in Bins, Never Storm Drains",
            "Category": "Street Action",
            "Topic": "Sidewalks & Drains",
            "Scope": "Community",
            "Impact": "Positive",
            "Description": "Hold onto chip bags, straws, and bottle caps until you reach a trash bin so rain in Irapuato does not wash them into drains (UN-Water, 2023).",
        },
        {
            "Name": "Swap Books, Hoodies & Reuse Notebooks",
            "Category": "School Action",
            "Topic": "Class Swap",
            "Scope": "Community",
            "Impact": "Positive",
            "Description": "Reuse blank pages in old notebooks, borrow or trade books and jackets with classmates, and skip buying extra items just for trends (Ellen MacArthur Foundation, 2022).",
        },
        {
            "Name": "Run Washing Machines Only on Full Loads",
            "Category": "Home Action",
            "Topic": "Laundry Day",
            "Scope": "Community",
            "Impact": "Positive",
            "Description": "Wait until the laundry basket has a full load before running a wash cycle at home to save water and electricity (UN-Water, 2023).",
        },
        {
            "Name": "School Recycling & Refill Station Rule",
            "Category": "School Policy Action",
            "Topic": "Campus Rules",
            "Scope": "Public Policy",
            "Impact": "Positive",
            "Description": "Propose clearly labeled recycling bins, refill points, and quick bathroom leak checks with your student council and school administration (United Nations, 2015).",
        },
        {
            "Name": "Municipal Pipe Leak Repair & Pressure Care",
            "Category": "Local Context",
            "Topic": "City Water Network",
            "Scope": "Public Policy",
            "Impact": "High",
            "Description": "Fixing leaks in neighborhood water mains and keeping distribution networks well maintained reduces water lost before it reaches homes in Irapuato (CONAGUA, 2023; JAPAMI, 2024).",
        },
        {
            "Name": "Wastewater Treatment & Clean Discharge",
            "Category": "Local Context",
            "Topic": "Treatment Plants",
            "Scope": "Public Policy",
            "Impact": "High",
            "Description": "Operating effective wastewater treatment plants and preventing chemical or oil dumping keeps local water bodies cleaner in Guanajuato (CONAGUA, 2023; UNESCO, 2024).",
        },
        {
            "Name": "Local Waste Separation & Circular Programs",
            "Category": "Local Context",
            "Topic": "Municipal Waste",
            "Scope": "Public Policy",
            "Impact": "High",
            "Description": "Supporting neighborhood collection schedules, sorting recyclables, and cutting single-use packaging helps Irapuato manage waste and protect water (UNEP, 2024; Ellen MacArthur Foundation, 2022).",
        },
    ])

df = load_irapuato_data()

# ==============================================================================
# 4. TOP BAR & WORKING SECTION JUMP BUTTONS (SAME TAB)
# ==============================================================================
st.markdown('<div id="top"></div>', unsafe_allow_html=True)

logo_html = (
    '<img src="logo.png" alt="Huella Azul" style="height:28px;">'
    if os.path.exists("logo.png")
    else '💧 <div class="brand-logo"><span>Huella Azul</span></div>'
)

st.markdown(
    f"""
    <div class="top-nav-wrap">
        <div class="brand-logo">{logo_html}</div>
        <div class="nav-subtitle">Irapuato • SDG 6 &amp; SDG 12 (United Nations, 2015) • Teen Edition</div>
    </div>
    """,
    unsafe_allow_html=True,
)

scroll_slot = st.empty()


def jump_to_section(section_id: str, nonce: int):
    with scroll_slot:
        components.html(
            f"""
            <script>
            (function() {{
                const doc = window.parent.document;
                const el = doc.getElementById("{section_id}");
                if (el) {{
                    el.scrollIntoView({{ behavior: "smooth", block: "start" }});
                }}
            }})();
            </script>
            <!-- jump nonce: {nonce} -->
            """,
            height=0,
        )


if "jump_nonce" not in st.session_state:
    st.session_state.jump_nonce = 0

nav_items = [
    ("💧 Home", "top", "jump_home"),
    ("🎯 Irapuato & SDGs", "sdgs", "jump_sdgs"),
    ("🌊 Rivers & Habits", "rivers", "jump_rivers"),
    ("📊 Local Scenarios", "scenarios", "jump_scenarios"),
    ("✨ Concrete Actions", "action", "jump_action"),
    ("🎬 Video", "video", "jump_video"),
    ("🎮 Minigame", "minigame", "jump_minigame"),
    ("📋 Quiz & Refs", "quiz", "jump_quiz"),
]

nav_cols = st.columns(len(nav_items))
for col, (label, sec_id, key_name) in zip(nav_cols, nav_items):
    with col:
        if st.button(label, use_container_width=True, key=key_name):
            st.session_state.jump_nonce += 1
            jump_to_section(sec_id, st.session_state.jump_nonce)

# ==============================================================================
# 5. HERO SECTION (IRAPUATO FOCUS + SEA BG + TWO ATTACHED SDG IMAGES)
# ==============================================================================
st.markdown(
    f"""
    <div class="hero-section">
        <div class="hero-grid">
            <div class="hero-main-col">
                <div class="hero-tag">💧 HUELLA AZUL • IRAPUATO WATER &amp; SMART HABITS</div>
                <div class="hero-h1">Your Daily Habits in Irapuato Shape Tomorrow's Water</div>
                <div class="hero-p">
                    Turning off the sink while brushing, refilling your bottle at school, and reporting leaks take seconds—and protect water in Irapuato
                    (UN-Water, 2023; JAPAMI, 2024; United Nations, 2015).
                </div>
            </div>
            <div class="hero-badges-panel">
                <div class="hero-side-badge">
                    <img src="{URL_SDG6}" alt="SDG 6 Clean Water and Sanitation" />
                    <div style="font-size:0.75rem; font-weight:800; color:#5EEAD4;">SDG 6</div>
                    <div style="font-size:0.74rem; color:#E2E8F0; margin-top:0.2rem; line-height:1.3;">
                        Clean Water &amp; Sanitation (UN, 2015)
                    </div>
                </div>
                <div class="hero-side-badge">
                    <img src="{URL_SDG12}" alt="SDG 12 Responsible Consumption and Production" />
                    <div style="font-size:0.75rem; font-weight:800; color:#FBBF24;">SDG 12</div>
                    <div style="font-size:0.74rem; color:#E2E8F0; margin-top:0.2rem; line-height:1.3;">
                        Responsible Consumption (UN, 2015)
                    </div>
                </div>
            </div>
        </div>
        <div class="hero-stats">
            <div>
                <div class="stat-num">78% (Target 100%)</div>
                <div class="stat-caption">Illustrative Irapuato household water-efficiency &amp; leak-reduction goal for teens and families (CONAGUA, 2023; JAPAMI, 2024).</div>
            </div>
            <div>
                <div class="stat-num">~2 glasses+</div>
                <div class="stat-caption">Everyday analogy: eating a bag of chips is like grabbing glasses of water used to grow &amp; make it (Water Footprint Network, 2023).</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 6. SDGS SECTION: IRAPUATO PROGRESS & CIRCULAR ECONOMY
# ==============================================================================
st.markdown('<div id="sdgs"></div>', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">IRAPUATO LOCAL GOALS</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Two Goals. One City: Irapuato.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sec-desc">Local progress in Irapuato depends on keeping water clean and reliable (SDG 6) while cutting everyday waste and over-buying (SDG 12) (United Nations, 2015).</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="circular-box">
        <strong>♻️ Circular Economy in Plain Words:</strong> Instead of <em>buy → use once → toss</em>, circular economy means
        <strong>reusing, fixing, sharing, and recycling</strong> things so we waste less water, energy, and raw materials in Irapuato
        (Ellen MacArthur Foundation, 2022; UNEP, 2024).
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="connection-strip">
        <strong>🥤 Real-Life Connections:</strong> A bag of chips is like grabbing a couple of glasses of water, a disposable drink adds extra bottle and production water,
        and tossing uneaten food wastes the water that grew it (Water Footprint Network, 2023; FAO, 2021).
    </div>
    """,
    unsafe_allow_html=True,
)

col_o1, col_o2 = st.columns(2, gap="large")

with col_o1:
    st.markdown(
        """
        <div class="info-card">
            <div class="card-top-row">
                <span class="pill-blue">IRAPUATO • SDG 06</span>
                <span>💧</span>
            </div>
            <div class="card-h3">Clean Water &amp; Care in Irapuato</div>
            <div class="card-p">
                Protecting water at home and in school keeps local supply steadier and reduces waste in Irapuato (JAPAMI, 2024; United Nations, 2015).
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    fig_6 = go.Figure(
        go.Bar(
            x=["2020", "2023", "2026 (Irapuato)", "2030 Goal"],
            y=[66, 72, 78, 100],
            marker_color=["#5EEAD4", "#2DD4BF", "#0284C7", "#082F49"],
            text=["66%", "72%", "78%", "100%"],
            textposition="auto",
        )
    )
    fig_6.update_layout(
        title=dict(text="Irapuato water-care &amp; efficiency benchmark (%)", font=dict(size=12, color="#475569")),
        height=210,
        margin=dict(l=10, r=10, t=34, b=10),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        yaxis=dict(visible=False, range=[0, 115]),
        xaxis=dict(tickfont=dict(size=11, color="#475569")),
    )
    st.plotly_chart(fig_6, use_container_width=True, config={"displayModeBar": False})
    st.markdown(
        '<div class="ref-note">Illustrative school benchmark grounded in United Nations (2015), CONAGUA (2023), and JAPAMI (2024).</div>',
        unsafe_allow_html=True,
    )

with col_o2:
    st.markdown(
        """
        <div class="info-card">
            <div class="card-top-row">
                <span class="pill-teal">IRAPUATO • SDG 12</span>
                <span>♻️</span>
            </div>
            <div class="card-h3">Smart Consumption in Irapuato</div>
            <div class="card-p">
                Less impulse buying, less wasted food, and more reuse mean less trash and less hidden water wasted around town (UNEP, 2024; United Nations, 2015).
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    fig_12 = go.Figure(
        go.Bar(
            x=["2020", "2023", "2026 (Irapuato)", "2030 Goal"],
            y=[88, 76, 62, 35],
            marker_color=["#2DD4BF", "#14B8A6", "#0284C7", "#082F49"],
            text=["88", "76", "62", "35"],
            textposition="auto",
        )
    )
    fig_12.update_layout(
        title=dict(text="Irapuato waste &amp; resource pressure index (lower is better)", font=dict(size=12, color="#475569")),
        height=210,
        margin=dict(l=10, r=10, t=34, b=10),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        yaxis=dict(visible=False, range=[0, 115]),
        xaxis=dict(tickfont=dict(size=11, color="#475569")),
    )
    st.plotly_chart(fig_12, use_container_width=True, config={"displayModeBar": False})
    st.markdown(
        '<div class="ref-note">Illustrative school benchmark grounded in United Nations (2015), UNEP (2024), and Ellen MacArthur Foundation (2022).</div>',
        unsafe_allow_html=True,
    )

st.markdown("<div style='height: 36px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# 7. RIVERS & HABITS SECTION (4TH SECTION WITH NEW IMAGE)
# ==============================================================================
st.markdown('<div id="rivers"></div>', unsafe_allow_html=True)
col_r_left, col_r_right = st.columns([1.05, 1.15], gap="large")

with col_r_left:
    st.markdown(
        """
        <div class="river-visual-box">
            <div class="floating-mini-card">
                <div style="font-size:0.72rem; font-weight:700; color:#0D9488; text-transform:uppercase;">
                    Irapuato &amp; Beyond
                </div>
                <div style="font-size:0.95rem; font-weight:800; color:#082F49; margin-top:0.2rem;">
                    Everyday choices connect to local water (Water Footprint Network, 2023).
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="ref-note">Sources: Water Footprint Network (2023), FAO (2021), and UN-Water (2023).</div>',
        unsafe_allow_html=True,
    )

with col_r_right:
    st.markdown('<div class="sec-eyebrow">EVERYDAY CONNECTIONS</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">What you buy, eat, and toss connects to water.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sec-desc">Spot simple connections in your routine—snacks, drinks, clothes, and street litter in Irapuato all link back to water and resources (Water Footprint Network, 2023).</div>',
        unsafe_allow_html=True,
    )

    processes_list = [
        (
            "🥔",
            "Snacks &amp; Drinks",
            "Hidden Water",
            "Eating a bag of chips is like grabbing a couple of glasses of water, and single-use bottles add extra production water (Water Footprint Network, 2023; UNEP, 2024).",
        ),
        (
            "👕",
            "Clothes &amp; Leftover Food",
            "Circular vs. Waste",
            "Buying extra clothes you barely wear or tossing leftover food wastes the water used to grow and make them (Ellen MacArthur Foundation, 2022; FAO, 2021).",
        ),
        (
            "🌧️",
            "Trash &amp; Runoff in Irapuato",
            "Drains &amp; Waterways",
            "Wrappers and trash left on sidewalks or streets wash into drains when it rains, making water cleanup harder (UN-Water, 2023).",
        ),
    ]

    for ic, name_p, topic_p, desc_p in processes_list:
        st.markdown(
            f"""
            <div class="proc-item">
                <div class="proc-icon-circle">{ic}</div>
                <div>
                    <div style="font-weight:700; color:#082F49; font-size:0.95rem;">
                        {name_p} <span style="font-weight:500; color:#64748B;">• {topic_p}</span>
                    </div>
                    <div style="font-size:0.88rem; color:#475569; margin-top:0.2rem;">
                        {desc_p}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ==============================================================================
# 8. DARK SCENARIOS SECTION: IRAPUATO FUTURES
# ==============================================================================
st.markdown('<div id="scenarios"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="dark-band">
        <div style="font-size:0.72rem; text-transform:uppercase; letter-spacing:1.6px; color:#5EEAD4; font-weight:700;">
            IRAPUATO PATHWAYS
        </div>
        <div style="font-size:2.15rem; font-weight:800; color:#FFFFFF; margin-top:0.3rem;">
            The future is not written.
        </div>
        <div style="font-size:0.96rem; color:#CBD5E1; max-width:680px; margin-top:0.45rem;">
            See how Irapuato looks under two different habit paths: ignoring waste and leaks vs. circular habits and water care (UNESCO, 2024; Ellen MacArthur Foundation, 2022).
        </div>
    """,
    unsafe_allow_html=True,
)

scenario_choice = st.radio(
    "Select a scenario for Irapuato:",
    ["Scenario 1: High Waste & Unchecked Leaks", "Scenario 2: Circular Teens & Water Care"],
    horizontal=True,
)

is_pos = "2" in scenario_choice or "Circular" in scenario_choice
st.markdown('<div class="scenario-panel">', unsafe_allow_html=True)
col_e_izq, col_e_der = st.columns([1, 1.3], gap="large")

with col_e_izq:
    badge_label = "CIRCULAR IRAPUATO PATH" if is_pos else "HIGH STRAIN PATH"
    badge_color = "#0F766E" if is_pos else "#B91C1C"
    scen_desc = (
        "When teens refill bottles, skip food waste, fix leaks early, and reuse items, Irapuato saves water and cuts street trash (Ellen MacArthur Foundation, 2022; JAPAMI, 2024)."
        if is_pos
        else "When leaks stay unfixed, trash piles up, and food or single-use items go to waste, water stress and cleanup costs climb (CONAGUA, 2023; UNESCO, 2024)."
    )
    st.markdown(
        f"""
        <div class="scenario-left-box">
            <div style="font-size:0.72rem; font-weight:800; color:{badge_color}; letter-spacing:0.8px;">
                {badge_label}
            </div>
            <div style="font-size:1.3rem; font-weight:800; color:#082F49; margin:0.45rem 0;">
                {scenario_choice}
            </div>
            <div style="font-size:0.92rem; color:#334155; line-height:1.55;">
                {scen_desc}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_e_der:
    labels_p = ["Water Strain in Irapuato", "Household Water Care", "Street & Snack Waste"]
    vals_p = [24, 90, 28] if is_pos else [80, 48, 86]
    cols_p = ["#2DD4BF", "#0284C7", "#14B8A6"] if is_pos else ["#0284C7", "#94A3B8", "#082F49"]

    fig_e = go.Figure(
        go.Bar(
            x=vals_p,
            y=labels_p,
            orientation="h",
            marker_color=cols_p,
            text=[f"{v}%" for v in vals_p],
            textposition="outside",
        )
    )
    fig_e.update_layout(
        title=dict(text="Illustrative Irapuato scenario percentages", font=dict(size=13, color="#082F49")),
        height=210,
        margin=dict(l=10, r=35, t=34, b=10),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        xaxis=dict(range=[0, 105], visible=False),
        yaxis=dict(tickfont=dict(size=12, color="#334155")),
    )
    st.plotly_chart(fig_e, use_container_width=True, config={"displayModeBar": False})
    st.markdown(
        '<div class="ref-note">Illustrative local scenario percentages grounded in CONAGUA (2023), UNESCO (2024), and Ellen MacArthur Foundation (2022).</div>',
        unsafe_allow_html=True,
    )

st.markdown("</div></div>", unsafe_allow_html=True)

# ==============================================================================
# 9. ACTION SECTION: CONCRETE ACTIONS + ACTION LINKS
# ==============================================================================
st.markdown('<div id="action"></div>', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">CONCRETE ACTIONS</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Specific actions at home, school, and around town.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sec-desc">Clear, step-by-step habits for students in Irapuato across daily routines, classrooms, and neighborhood spaces (UN-Water, 2023; UNEP, 2024).</div>',
    unsafe_allow_html=True,
)

action_cards = [
    (
        "At Home",
        "🏠",
        "Sink, shower, kitchen &amp; laundry",
        [
            "<b>Brush &amp; soap with tap off:</b> Close the faucet while brushing teeth or soaping up, and keep showers around 5 minutes (UN-Water, 2023).",
            "<b>Fridge bottle &amp; full loads:</b> Chill a water bottle in the fridge instead of running the tap cold, and run laundry only on full loads (UN-Water, 2023).",
            "<b>Small portions &amp; leak check:</b> Serve what you finish so food is not wasted, and report dripping taps or running toilets right away (FAO, 2021; JAPAMI, 2024).",
        ],
    ),
    (
        "At School",
        "🏫",
        "Classroom, breaks &amp; supplies",
        [
            "<b>Bring &amp; refill one bottle:</b> Carry a reusable bottle to school every day instead of buying disposable drinks (UNEP, 2024).",
            "<b>Reuse notebooks &amp; swap items:</b> Finish blank pages in existing notebooks and trade books, hoodies, or supplies with classmates (Ellen MacArthur Foundation, 2022).",
            "<b>Report school leaks &amp; sort bins:</b> Tell staff if a school sink or toilet leaks, and put recyclables and trash in the right bins (JAPAMI, 2024; United Nations, 2015).",
        ],
    ),
    (
        "Streets &amp; City",
        "🛣️",
        "Sidewalks, drains &amp; local rules",
        [
            "<b>Keep wrappers out of storm drains:</b> Toss snack bags, cups, and lids in bins—never on sidewalks or drains—so rain does not wash litter into waterways (UN-Water, 2023).",
            "<b>Pitch a campus refill &amp; recycling check:</b> Work with classmates and student leaders to add clear bin labels and water-care reminders (United Nations, 2015).",
            "<b>Support clean pipes &amp; treatment:</b> Back local water care, leak repairs, and wastewater treatment efforts in Irapuato (CONAGUA, 2023; UNESCO, 2024).",
        ],
    ),
]

c_amb1, c_amb2, c_amb3 = st.columns(3, gap="medium")
for col_box, (amb_name, amb_icon, amb_sub, bullets) in zip([c_amb1, c_amb2, c_amb3], action_cards):
    lis_html = "".join([f"<li style='margin-bottom:0.5rem;'>{b}</li>" for b in bullets])
    with col_box:
        st.markdown(
            f"""
            <div class="info-card">
                <div style="font-size:1.35rem; margin-bottom:0.35rem;">{amb_icon}</div>
                <div class="card-h3">{amb_name}</div>
                <div style="font-size:0.82rem; font-weight:700; color:#0D9488; margin-bottom:0.7rem;">
                    {amb_sub}
                </div>
                <ul style="padding-left:1.1rem; font-size:0.88rem; color:#475569; line-height:1.45;">
                    {lis_html}
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="action-links-strip">
        <div style="font-weight:800; font-size:0.98rem; color:#082F49; margin-bottom:0.45rem;">
            🔗 Pages Where You Can Take Action &amp; Explore More
        </div>
        <ul style="padding-left:1.2rem; margin-bottom:0;">
            <li style="margin-bottom:0.35rem;">
                <strong>JAPAMI (Irapuato):</strong> <a href="https://www.japami.gob.mx" target="_blank">japami.gob.mx</a> — Check local water services and water-care resources in Irapuato.
            </li>
            <li style="margin-bottom:0.35rem;">
                <strong>Water Footprint Network:</strong> <a href="https://www.waterfootprint.org" target="_blank">waterfootprint.org</a> — Check water footprints of everyday foods and products.
            </li>
            <li style="margin-bottom:0.35rem;">
                <strong>Ellen MacArthur Foundation:</strong> <a href="https://www.ellenmacarthurfoundation.org/topics/circular-economy-introduction/overview" target="_blank">ellenmacarthurfoundation.org</a> — Learn practical circular-economy habits like reusing, repairing, and sharing.
            </li>
            <li style="margin-bottom:0.35rem;">
                <strong>UN-Water:</strong> <a href="https://www.unwater.org/water-facts" target="_blank">unwater.org/water-facts</a> — Explore water and hygiene facts and habits.
            </li>
            <li style="margin-bottom:0;">
                <strong>United Nations SDGs:</strong> <a href="https://sdgs.un.org/goals" target="_blank">sdgs.un.org/goals</a> — Review SDG 6 and SDG 12 goals and targets.
            </li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 9.2 VIDEO SECTION: HUELLA AZUL ONLY
# ==============================================================================
st.markdown('<div id="video"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="video-section-card">
        <div class="sec-eyebrow">PROJECT VIDEO • HUELLA AZUL</div>
        <div class="card-h3">Huella Azul: Think About Our Actions in the World</div>
        <div class="card-p" style="margin-bottom:1rem;">
            Watch our project video on how everyday decisions shape our water footprint and environment (Julia, 2026).
        </div>
    """,
    unsafe_allow_html=True,
)

st.video(URL_VIDEO_HUELLA_AZUL)

st.markdown(
    """
        <div class="ref-note" style="margin-top:0.75rem;">
            <strong>Video Reference (APA):</strong> Julia. (2026, November 23). <em>HUELLA AZUL - a page to think about the actions about we do in the world</em> [Video]. YouTube. https://www.youtube.com/watch?v=AnIR7CY3HxI
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 9.5 KEYBOARD ARCADE MINIGAME: RIVER RESCUE
# ==============================================================================
st.markdown('<div id="minigame"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="game-arena">
        <div class="sec-eyebrow">ARCADE MINIGAME • KEYBOARD CONTROLS</div>
        <div class="sec-title">🎮 River Rescue: Move Your Guardian</div>
        <div class="sec-desc" style="margin-bottom:0.8rem;">
            Use your <strong>Arrow Keys</strong> or <strong>WASD</strong> to move your character.
            Catch <strong>💧 clean drops</strong> and <strong>♻️ circular items</strong>, and dodge <strong>🚱 leaks and trash</strong>.
            Click inside the game box first so keyboard inputs focus cleanly.
        </div>
    """,
    unsafe_allow_html=True,
)

game_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Plus Jakarta Sans', system-ui, sans-serif; }
  body { background: transparent; color: #082F49; }
  .shell {
    background: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 18px;
    padding: 16px;
    box-shadow: 0 10px 25px rgba(8, 47, 73, 0.08);
  }
  .hud {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 12px;
  }
  .hud-group { display: flex; gap: 10px; flex-wrap: wrap; }
  .pill {
    background: #F0FDFA;
    border: 1px solid #99F6E4;
    color: #082F49;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
  }
  .btn {
    background: #2DD4BF;
    color: #042436;
    border: none;
    border-radius: 10px;
    padding: 8px 14px;
    font-weight: 800;
    font-size: 13px;
    cursor: pointer;
  }
  .btn:hover { background: #14B8A6; color: #FFFFFF; }
  canvas {
    display: block;
    width: 100%;
    max-width: 100%;
    height: 390px;
    border-radius: 14px;
    background: linear-gradient(180deg, #06283D 0%, #0C4A6E 65%, #0F766E 100%);
    border: 2px solid #082F49;
    outline: none;
  }
  .touch-pad {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-top: 10px;
    flex-wrap: wrap;
  }
  .t-btn {
    background: #E0F2FE;
    color: #082F49;
    border: 1px solid #7DD3FC;
    border-radius: 8px;
    padding: 6px 12px;
    font-weight: 700;
    font-size: 12px;
    cursor: pointer;
  }
  .help {
    margin-top: 8px;
    font-size: 12px;
    color: #475569;
    text-align: center;
  }
</style>
</head>
<body>
  <div class="shell">
    <div class="hud">
      <div class="hud-group">
        <div class="pill" id="scorePill">⭐ Score: 0</div>
        <div class="pill" id="litersPill">💧 Water Saved: 0 L</div>
        <div class="pill" id="livesPill">❤️❤️❤️</div>
        <div class="pill" id="timePill">⏱️ Time: 35s</div>
      </div>
      <button class="btn" id="restartBtn" type="button">Restart Run</button>
    </div>

    <canvas id="gameCanvas" width="920" height="390" tabindex="0"></canvas>

    <div class="touch-pad">
      <button class="t-btn" type="button" id="btnLeft">⬅️ Left (A)</button>
      <button class="t-btn" type="button" id="btnUp">⬆️ Up (W)</button>
      <button class="t-btn" type="button" id="btnDown">⬇️ Down (S)</button>
      <button class="t-btn" type="button" id="btnRight">➡️ Right (D)</button>
    </div>
    <div class="help">Tip: Click the game canvas and use Arrow Keys or WASD. Press <strong>Space</strong> to play again when finished.</div>
  </div>

<script>
(() => {
  const canvas = document.getElementById("gameCanvas");
  const ctx = canvas.getContext("2d");

  const scorePill = document.getElementById("scorePill");
  const litersPill = document.getElementById("litersPill");
  const livesPill = document.getElementById("livesPill");
  const timePill = document.getElementById("timePill");
  const restartBtn = document.getElementById("restartBtn");

  const keys = {};
  let score = 0;
  let liters = 0;
  let lives = 3;
  let timeLeft = 35;
  let gameOver = false;
  let spawnTimer = 0;
  let lastTimestamp = performance.now();
  let timerAccum = 0;
  let flashMessage = "";
  let flashTimer = 0;

  const player = {
    x: canvas.width / 2,
    y: canvas.height - 65,
    r: 22,
    speed: 340
  };

  let items = [];

  const goodTypes = [
    { emoji: "💧", pts: 15, water: 120, label: "+15 pts • Clean Drop" },
    { emoji: "♻️", pts: 25, water: 250, label: "+25 pts • Circular Loop" }
  ];

  const badTypes = [
    { emoji: "🚱", pts: -15, water: 0, label: "-15 pts • Unfixed Leak" },
    { emoji: "🗑️", pts: -10, water: 0, label: "-10 pts • Snack Litter" }
  ];

  function resetGame() {
    score = 0;
    liters = 0;
    lives = 3;
    timeLeft = 35;
    gameOver = false;
    spawnTimer = 0;
    timerAccum = 0;
    flashMessage = "Catch clean water & circular loops!";
    flashTimer = 1.4;
    player.x = canvas.width / 2;
    player.y = canvas.height - 65;
    items = [];
    updateHud();
    canvas.focus();
  }

  function updateHud() {
    scorePill.textContent = `⭐ Score: ${score}`;
    litersPill.textContent = `💧 Water Saved: ${liters.toLocaleString()} L`;
    const hearts = "❤️".repeat(Math.max(0, lives)) + "🖤".repeat(Math.max(0, 3 - lives));
    livesPill.textContent = hearts || "💔";
    timePill.textContent = `⏱️ Time: ${Math.max(0, Math.ceil(timeLeft))}s`;
  }

  function spawnItem() {
    const isGood = Math.random() < 0.68;
    const pool = isGood ? goodTypes : badTypes;
    const spec = pool[Math.floor(Math.random() * pool.length)];
    const speedBase = 115 + Math.random() * 95 + (35 - timeLeft) * 2.2;

    items.push({
      x: 36 + Math.random() * (canvas.width - 72),
      y: -24,
      r: 20,
      vy: speedBase,
      good: isGood,
      ...spec
    });
  }

  function drawPlayer() {
    ctx.save();
    ctx.beginPath();
    ctx.arc(player.x, player.y, player.r + 6, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(45, 212, 191, 0.22)";
    ctx.fill();

    ctx.beginPath();
    ctx.arc(player.x, player.y, player.r, 0, Math.PI * 2);
    ctx.fillStyle = "#2DD4BF";
    ctx.fill();
    ctx.lineWidth = 3;
    ctx.strokeStyle = "#FFFFFF";
    ctx.stroke();

    ctx.font = "22px sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("🧢", player.x, player.y - 18);

    ctx.fillStyle = "#042436";
    ctx.beginPath();
    ctx.arc(player.x - 7, player.y - 2, 3, 0, Math.PI * 2);
    ctx.arc(player.x + 7, player.y - 2, 3, 0, Math.PI * 2);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(player.x, player.y + 4, 7, 0.15 * Math.PI, 0.85 * Math.PI);
    ctx.lineWidth = 2.4;
    ctx.strokeStyle = "#042436";
    ctx.stroke();
    ctx.restore();
  }

  function drawBackgroundWaves() {
    ctx.save();
    ctx.strokeStyle = "rgba(153, 246, 228, 0.12)";
    ctx.lineWidth = 2;
    for (let row = 0; row < 4; row++) {
      const yBase = 75 + row * 85;
      ctx.beginPath();
      for (let x = 0; x <= canvas.width; x += 28) {
        const y = yBase + Math.sin(x * 0.02 + performance.now() * 0.002 + row) * 6;
        if (x === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();
    }
    ctx.restore();
  }

  function step(now) {
    const dt = Math.min(0.05, (now - lastTimestamp) / 1000);
    lastTimestamp = now;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBackgroundWaves();

    if (!gameOver) {
      timeLeft -= dt;
      timerAccum += dt;
      if (timerAccum >= 0.25) {
        timerAccum = 0;
        updateHud();
      }
      if (timeLeft <= 0 || lives <= 0) {
        gameOver = true;
        updateHud();
      }

      let dx = 0, dy = 0;
      if (keys["ArrowLeft"] || keys["KeyA"]) dx -= 1;
      if (keys["ArrowRight"] || keys["KeyD"]) dx += 1;
      if (keys["ArrowUp"] || keys["KeyW"]) dy -= 1;
      if (keys["ArrowDown"] || keys["KeyS"]) dy += 1;

      if (dx !== 0 && dy !== 0) {
        dx *= 0.7071;
        dy *= 0.7071;
      }

      player.x = Math.max(player.r + 10, Math.min(canvas.width - player.r - 10, player.x + dx * player.speed * dt));
      player.y = Math.max(player.r + 24, Math.min(canvas.height - player.r - 10, player.y + dy * player.speed * dt));

      spawnTimer -= dt;
      if (spawnTimer <= 0) {
        spawnItem();
        spawnTimer = Math.max(0.38, 0.85 - (35 - timeLeft) * 0.012);
      }

      for (let i = items.length - 1; i >= 0; i--) {
        const it = items[i];
        it.y += it.vy * dt;

        ctx.font = "28px sans-serif";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(it.emoji, it.x, it.y);

        const dist = Math.hypot(player.x - it.x, player.y - it.y);
        if (dist < player.r + it.r - 4) {
          score = Math.max(0, score + it.pts);
          liters += it.water;
          if (!it.good) lives = Math.max(0, lives - 1);
          flashMessage = it.label;
          flashTimer = 1.0;
          items.splice(i, 1);
          updateHud();
          continue;
        }

        if (it.y > canvas.height + 30) {
          items.splice(i, 1);
        }
      }
    }

    drawPlayer();

    if (flashTimer > 0 && !gameOver) {
      flashTimer -= dt;
      ctx.save();
      ctx.fillStyle = "rgba(8, 47, 73, 0.78)";
      ctx.beginPath();
      ctx.roundRect(canvas.width / 2 - 140, 14, 280, 30, 12);
      ctx.fill();
      ctx.fillStyle = "#5EEAD4";
      ctx.font = "bold 13px sans-serif";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(flashMessage, canvas.width / 2, 29);
      ctx.restore();
    }

    if (gameOver) {
      ctx.save();
      ctx.fillStyle = "rgba(4, 24, 38, 0.82)";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      let rank = "Water Explorer";
      if (score >= 180) rank = "🏆 Huella Azul Master";
      else if (score >= 90) rank = "⚡ River Guardian";

      ctx.fillStyle = "#5EEAD4";
      ctx.font = "bold 15px sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(`RANK EARNED: ${rank}`, canvas.width / 2, canvas.height / 2 - 42);

      ctx.fillStyle = "#FFFFFF";
      ctx.font = "bold 30px sans-serif";
      ctx.fillText(`Final Score: ${score} pts`, canvas.width / 2, canvas.height / 2 - 4);

      ctx.fillStyle = "#CBD5E1";
      ctx.font = "15px sans-serif";
      ctx.fillText(
        `Water Saved: ${liters.toLocaleString()} L — Press SPACE or "Restart Run"`,
        canvas.width / 2,
        canvas.height / 2 + 34
      );
      ctx.restore();
    }

    requestAnimationFrame(step);
  }

  window.addEventListener("keydown", (e) => {
    if (["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown", "Space"].includes(e.code)) {
      if (document.activeElement === canvas || gameOver) {
        e.preventDefault();
      }
    }
    keys[e.code] = true;
    if (gameOver && e.code === "Space") {
      resetGame();
    }
  });

  window.addEventListener("keyup", (e) => {
    keys[e.code] = false;
  });

  function bindHoldButton(id, code) {
    const el = document.getElementById(id);
    el.addEventListener("pointerdown", () => { keys[code] = true; canvas.focus(); });
    el.addEventListener("pointerup", () => { keys[code] = false; });
    el.addEventListener("pointerleave", () => { keys[code] = false; });
  }
  bindHoldButton("btnLeft", "ArrowLeft");
  bindHoldButton("btnRight", "ArrowRight");
  bindHoldButton("btnUp", "ArrowUp");
  bindHoldButton("btnDown", "ArrowDown");

  restartBtn.addEventListener("click", resetGame);
  updateHud();
  requestAnimationFrame(step);
})();
</script>
</body>
</html>
"""

components.html(game_html, height=495)
st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# 10. INTERACTIVE QUIZ, FILTERED TABLE (STRICT SCOPE) & APA REFERENCES
# ==============================================================================
st.markdown('<div id="quiz"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="closing-dark-box">
        <div style="font-size:0.72rem; text-transform:uppercase; letter-spacing:1.6px; color:#5EEAD4; font-weight:700;">
            PICK YOUR TEEN CHALLENGE
        </div>
        <div style="font-size:1.9rem; font-weight:800; color:#FFFFFF; margin-top:0.25rem;">
            Your footprint can make a difference in Irapuato.
        </div>
        <div style="font-size:0.94rem; color:#CBD5E1; margin-top:0.35rem;">
            Filter concrete actions, connections, and local context strictly by scope—without mixing categories—and view the APA references below.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)
q_col1, q_col2 = st.columns([1.4, 1], gap="large")

with q_col1:
    scope_options = ["All (Random)"] + df["Scope"].dropna().unique().tolist()
    scope_sel = st.radio(
        "Which scope do you want to explore?",
        scope_options,
        horizontal=True,
    )

if scope_sel == "All (Random)":
    filtered_pool = df.copy()
else:
    filtered_pool = df[df["Scope"] == scope_sel].copy()

max_r = max(1, len(filtered_pool))

with q_col2:
    if max_r == 1:
        num_r = 1
        st.info("Showing the 1 matching record for this scope.")
    else:
        num_r = st.slider(
            f"Number of rows to display (available in {scope_sel}: {max_r}):",
            min_value=1,
            max_value=max_r,
            value=min(4, max_r),
        )

if st.button("Generate results table ✨"):
    st.success(f"Showing only **{scope_sel}** records ({num_r} of {max_r} available)")

df_res = filtered_pool.sample(n=min(num_r, len(filtered_pool)))

cols_ok = [c for c in ["Name", "Category", "Scope", "Impact", "Description"] if c in df_res.columns]
st.dataframe(
    df_res[cols_ok],
    use_container_width=True,
    hide_index=True,
)

st.markdown(
    """
    <div class="apa-box">
        <div style="font-weight:800; font-size:0.98rem; color:#082F49; margin-bottom:0.75rem;">
            📚 APA References
        </div>
        <div class="apa-entry">
            Comisión Nacional del Agua [CONAGUA]. (2023). <em>Estadísticas del agua en México</em>. Secretaría de Medio Ambiente y Recursos Naturales (SEMARNAT). https://www.gob.mx/conagua
        </div>
        <div class="apa-entry">
            Ellen MacArthur Foundation. (2022). <em>What is a circular economy?</em> https://www.ellenmacarthurfoundation.org/topics/circular-economy-introduction/overview
        </div>
        <div class="apa-entry">
            Food and Agriculture Organization of the United Nations [FAO]. (2021). <em>The state of food and agriculture 2021: Making agrifood systems more resilient to shocks and stresses</em>. https://doi.org/10.4060/cb4476en
        </div>
        <div class="apa-entry">
            Julia. (2026, November 23). <em>HUELLA AZUL - a page to think about the actions about we do in the world</em> [Video]. YouTube. https://www.youtube.com/watch?v=AnIR7CY3HxI
        </div>
        <div class="apa-entry">
            Junta de Agua Potable, Drenaje, Alcantarillado y Saneamiento del Municipio de Irapuato [JAPAMI]. (2024). <em>Cultura del agua y cuidado del recurso hídrico en Irapuato</em>. Gobierno Municipal de Irapuato. https://www.japami.gob.mx
        </div>
        <div class="apa-entry">
            United Nations. (2015). <em>Transforming our world: The 2030 Agenda for Sustainable Development</em> (Goals 6 &amp; 12). https://sdgs.un.org/goals
        </div>
        <div class="apa-entry">
            United Nations Educational, Scientific and Cultural Organization [UNESCO]. (2024). <em>The United Nations world water development report 2024: Water for prosperity and peace</em>. https://www.unesco.org/reports/wwdr/en/2024
        </div>
        <div class="apa-entry">
            United Nations Environment Programme [UNEP]. (2024). <em>Global resources outlook 2024: Bend the trend – Pathways to a liveable planet as resource use spikes</em>. https://www.unep.org/resources/Global-Resource-Outlook-2024
        </div>
        <div class="apa-entry">
            UN-Water. (2023). <em>Water facts: Water, sanitation, and hygiene</em>. United Nations. https://www.unwater.org/water-facts
        </div>
        <div class="apa-entry" style="margin-bottom:0;">
            Water Footprint Network. (2023). <em>Product gallery &amp; personal water footprint calculator</em>. https://www.waterfootprint.org
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 11. FOOTER
# ==============================================================================
st.markdown(
    """
    <div class="footer-dark">
        <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:2rem;">
            <div>
                <div style="font-weight:800; font-size:1rem; color:#FFFFFF;">💧 Huella Azul • Irapuato</div>
                <div style="margin-top:0.4rem; max-width:350px; color:#94A3B8;">
                    Student project for secondary &amp; high school on SDG 6, SDG 12 (United Nations, 2015), circular economy, and everyday water habits in Irapuato.
                </div>
            </div>
            <div>
                <div style="font-weight:700; color:#FFFFFF; margin-bottom:0.4rem;">Key Citations</div>
                <div style="color:#94A3B8;">United Nations (2015) — SDG 6 &amp; SDG 12</div>
                <div style="color:#94A3B8;">Water Footprint Network (2023) &amp; UNEP (2024)</div>
                <div style="color:#94A3B8;">CONAGUA (2023) &amp; JAPAMI (2024) — Irapuato context</div>
            </div>
            <div>
                <div style="font-weight:700; color:#FFFFFF; margin-bottom:0.4rem;">Focus</div>
                <div style="color:#94A3B8;">Concrete actions at home, school &amp; streets</div>
                <div style="color:#94A3B8;">Practical habits for teenagers</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)