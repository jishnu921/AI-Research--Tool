import streamlit as st
import time
from pipeline import run_research_pipeline

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchMind · Multi-Agent Pipeline",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0a0a0f !important;
    color: #e8e6f0 !important;
    font-family: 'DM Mono', monospace !important;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 80% 50% at 20% -10%, rgba(120, 80, 255, 0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 110%, rgba(0, 200, 150, 0.08) 0%, transparent 60%),
        #0a0a0f !important;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"] { display: none; }

/* ── Main container ── */
.main .block-container {
    max-width: 960px !important;
    padding: 2rem 2rem 4rem !important;
    margin: 0 auto !important;
}

/* ── Hero Section ── */
.hero {
    text-align: center;
    padding: 3.5rem 0 2rem;
    position: relative;
}

.hero-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #7c5cff;
    margin-bottom: 1.2rem;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.4rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.03em;
    color: #f0eeff;
    margin: 0 0 1rem;
}

.hero-title span {
    background: linear-gradient(135deg, #7c5cff 0%, #00c896 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    font-family: 'DM Mono', monospace;
    font-size: 0.82rem;
    color: #6e6a85;
    letter-spacing: 0.04em;
    margin-bottom: 0;
}

/* ── Divider ── */
.hline {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(124,92,255,0.3) 30%, rgba(0,200,150,0.3) 70%, transparent);
    margin: 2.5rem 0;
}

/* ── Input Area ── */
.input-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #7c5cff;
    margin-bottom: 0.5rem;
}

[data-testid="stTextInput"] > div > div > input {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(124,92,255,0.25) !important;
    border-radius: 8px !important;
    color: #f0eeff !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.95rem !important;
    padding: 0.8rem 1rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}

[data-testid="stTextInput"] > div > div > input:focus {
    border-color: rgba(124,92,255,0.7) !important;
    box-shadow: 0 0 0 3px rgba(124,92,255,0.1) !important;
    outline: none !important;
}

[data-testid="stTextInput"] > div > div > input::placeholder {
    color: #3d3a50 !important;
}

/* ── Button ── */
[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #7c5cff 0%, #5a3fd4 100%) !important;
    color: #fff !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.14em !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.65rem 2.2rem !important;
    cursor: pointer !important;
    transition: opacity 0.2s, transform 0.15s !important;
    width: 100% !important;
}

[data-testid="stButton"] > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}

[data-testid="stButton"] > button:active {
    transform: translateY(0) !important;
}

/* ── Pipeline Steps ── */
.pipeline-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 2rem 0;
}

.step-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 1rem 0.85rem;
    text-align: center;
    transition: border-color 0.3s;
}

.step-card.active {
    border-color: rgba(124,92,255,0.5);
    background: rgba(124,92,255,0.06);
}

.step-card.done {
    border-color: rgba(0,200,150,0.4);
    background: rgba(0,200,150,0.05);
}

.step-icon {
    font-size: 1.4rem;
    margin-bottom: 0.4rem;
}

.step-num {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.15em;
    color: #4d4a62;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
}

.step-name {
    font-family: 'Syne', sans-serif;
    font-size: 0.75rem;
    font-weight: 600;
    color: #c5c0dc;
}

/* ── Result Cards ── */
.result-card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 1.5rem 1.6rem;
    margin-bottom: 1.2rem;
    position: relative;
    overflow: hidden;
}

.result-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
}

.result-card.search::before  { background: linear-gradient(90deg, #7c5cff, #a07fff); }
.result-card.expand::before  { background: linear-gradient(90deg, #00c896, #00a57a); }
.result-card.report::before  { background: linear-gradient(90deg, #ff6b6b, #ff9f43); }
.result-card.critic::before  { background: linear-gradient(90deg, #f9ca24, #f0932b); }

.card-header {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 1rem;
}

.card-badge {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    font-weight: 500;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    padding: 0.22rem 0.6rem;
    border-radius: 4px;
}

.badge-search { background: rgba(124,92,255,0.2); color: #a07fff; }
.badge-expand { background: rgba(0,200,150,0.2); color: #00c896; }
.badge-report { background: rgba(255,107,107,0.2); color: #ff6b6b; }
.badge-critic { background: rgba(249,202,36,0.2); color: #f9ca24; }

.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.88rem;
    font-weight: 700;
    color: #d8d4ee;
}

.card-content {
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    line-height: 1.75;
    color: #9e9ab8;
    white-space: pre-wrap;
    border-left: 2px solid rgba(255,255,255,0.06);
    padding-left: 1rem;
}

/* ── Status Bar ── */
.status-bar {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: #6e6a85;
    letter-spacing: 0.06em;
    margin-bottom: 1.5rem;
}

.status-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #7c5cff;
    animation: pulse 1.4s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(0.7); }
}

/* ── Spinner override ── */
[data-testid="stSpinner"] > div {
    color: #7c5cff !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.8rem !important;
}

/* ── Success / Error ── */
[data-testid="stAlert"] {
    border-radius: 8px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.8rem !important;
}

/* ── Progress bar ── */
[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, #7c5cff, #00c896) !important;
    border-radius: 4px !important;
}

/* ── Footer ── */
.footer {
    text-align: center;
    margin-top: 4rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.1em;
    color: #2e2b3d;
}
</style>
""", unsafe_allow_html=True)


# ─── Helpers ──────────────────────────────────────────────────────────────────

STEPS = [
    ("🔍", "01", "Search Agent"),
    ("📄", "02", "Expand Research"),
    ("✍️", "03", "Writer Agent"),
    ("🧠", "04", "Critic Agent"),
]

def render_pipeline_steps(active: int = -1, done_up_to: int = -1):
    cols = st.columns(4)
    for i, (icon, num, name) in enumerate(STEPS):
        css_class = "step-card"
        if i == active:
            css_class += " active"
        elif i <= done_up_to:
            css_class += " done"
        with cols[i]:
            st.markdown(f"""
            <div class="{css_class}">
                <div class="step-icon">{icon}</div>
                <div class="step-num">Step {num}</div>
                <div class="step-name">{name}</div>
            </div>
            """, unsafe_allow_html=True)


def result_card(card_type: str, badge_class: str, badge_label: str, title: str, content: str):
    st.markdown(f"""
    <div class="result-card {card_type}">
        <div class="card-header">
            <span class="card-badge {badge_class}">{badge_label}</span>
            <span class="card-title">{title}</span>
        </div>
        <div class="card-content">{content}</div>
    </div>
    """, unsafe_allow_html=True)


# ─── Hero ─────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="hero">
    <div class="hero-label">Multi-Agent Research System</div>
    <h1 class="hero-title">Research<span>Mind</span></h1>
    <p class="hero-sub">Search → Expand → Write → Critique · Powered by LLM agents</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="hline">', unsafe_allow_html=True)


# ─── Input ────────────────────────────────────────────────────────────────────

st.markdown('<div class="input-label">Research Topic</div>', unsafe_allow_html=True)

col_input, col_btn = st.columns([4, 1])

with col_input:
    topic = st.text_input(
        label="topic",
        placeholder="e.g. Quantum computing applications in cryptography",
        label_visibility="collapsed",
        key="topic_input",
    )

with col_btn:
    run_clicked = st.button("Run Pipeline", key="run_btn")


# ─── Pipeline Steps (idle) ────────────────────────────────────────────────────

st.markdown('<hr class="hline">', unsafe_allow_html=True)

if not run_clicked:
    render_pipeline_steps()

    if "last_state" in st.session_state:
        st.markdown("""
        <div class="status-bar">
            <span>← Previous results shown below · Enter a new topic to re-run</span>
        </div>
        """, unsafe_allow_html=True)


# ─── Run Pipeline ─────────────────────────────────────────────────────────────

if run_clicked:
    if not topic.strip():
        st.error("Please enter a research topic before running the pipeline.")
    else:
        progress_bar = st.progress(0)
        step_placeholder = st.empty()

        # Step 1
        step_placeholder.empty()
        with step_placeholder.container():
            render_pipeline_steps(active=0, done_up_to=-1)
            st.markdown("""
            <div class="status-bar">
                <div class="status-dot"></div>
                <span>Search agent is working ...</span>
            </div>""", unsafe_allow_html=True)
        progress_bar.progress(10)

        # Run actual pipeline (streaming steps via placeholder updates)
        # We'll capture each step manually

        import agents
        from agents import writer_chain, critic_chain, llm

        state = {}

        # — Step 1: Search
        response = llm.invoke(f"""
Answer in EXACTLY 3 lines.

Topic: {topic}

Rules:
- No disclaimers
- No extra explanation
- No examples
- Only 3 lines
""")
        state["search_results"] = response.content
        progress_bar.progress(25)

        # — Step 2 UI update
        step_placeholder.empty()
        with step_placeholder.container():
            render_pipeline_steps(active=1, done_up_to=0)
            st.markdown("""
            <div class="status-bar">
                <div class="status-dot"></div>
                <span>Expanding research into structured points ...</span>
            </div>""", unsafe_allow_html=True)

        state["scraped_content"] = llm.invoke(f"""
Expand this into clear bullet points.

Content:
{state["search_results"]}

Rules:
- No unrelated topics
- No puzzles
- Stay factual
""").content
        progress_bar.progress(50)

        # — Step 3 UI update
        step_placeholder.empty()
        with step_placeholder.container():
            render_pipeline_steps(active=2, done_up_to=1)
            st.markdown("""
            <div class="status-bar">
                <div class="status-dot"></div>
                <span>Writer agent is drafting the report ...</span>
            </div>""", unsafe_allow_html=True)

        research_combined = (
            f"SEARCH RESULTS:\n{state['search_results']}\n\n"
            f"DETAILED CONTENT:\n{state['scraped_content']}"
        )
        state["report"] = writer_chain.invoke({
            "topic": topic,
            "research": research_combined,
        })
        progress_bar.progress(75)

        # — Step 4 UI update
        step_placeholder.empty()
        with step_placeholder.container():
            render_pipeline_steps(active=3, done_up_to=2)
            st.markdown("""
            <div class="status-bar">
                <div class="status-dot"></div>
                <span>Critic agent is reviewing the report ...</span>
            </div>""", unsafe_allow_html=True)

        state["feedback"] = critic_chain.invoke({"report": state["report"]})
        progress_bar.progress(100)

        # — Done
        step_placeholder.empty()
        with step_placeholder.container():
            render_pipeline_steps(active=-1, done_up_to=3)
            st.markdown("""
            <div class="status-bar">
                <span>✓ Pipeline complete</span>
            </div>""", unsafe_allow_html=True)

        time.sleep(0.3)
        progress_bar.empty()

        st.session_state["last_state"] = state
        st.session_state["last_topic"] = topic


# ─── Results ──────────────────────────────────────────────────────────────────

if "last_state" in st.session_state:
    state = st.session_state["last_state"]
    last_topic = st.session_state.get("last_topic", "")

    st.markdown('<hr class="hline">', unsafe_allow_html=True)

    st.markdown(f"""
    <div style="font-family:'DM Mono',monospace; font-size:0.65rem; letter-spacing:0.2em;
                text-transform:uppercase; color:#4d4a62; margin-bottom:1.4rem;">
        Results · {last_topic}
    </div>
    """, unsafe_allow_html=True)

    result_card(
        "search", "badge-search", "Step 01 · Search Agent",
        "Initial Search Results",
        state.get("search_results", "")
    )

    result_card(
        "expand", "badge-expand", "Step 02 · Expand Research",
        "Structured Bullet Points",
        state.get("scraped_content", "")
    )

    result_card(
        "report", "badge-report", "Step 03 · Writer Agent",
        "Final Report",
        state.get("report", "")
    )

    result_card(
        "critic", "badge-critic", "Step 04 · Critic Agent",
        "Critique & Feedback",
        state.get("feedback", "")
    )

    # ── Download
    st.markdown('<hr class="hline">', unsafe_allow_html=True)
    full_output = f"""RESEARCHMIND PIPELINE OUTPUT
Topic: {last_topic}
{'=' * 60}

[STEP 1 · SEARCH RESULTS]
{state.get('search_results', '')}

[STEP 2 · EXPANDED RESEARCH]
{state.get('scraped_content', '')}

[STEP 3 · REPORT]
{state.get('report', '')}

[STEP 4 · CRITIC FEEDBACK]
{state.get('feedback', '')}
"""
    st.download_button(
        label="⬇  Download Full Report (.txt)",
        data=full_output,
        file_name=f"research_{last_topic[:30].replace(' ', '_')}.txt",
        mime="text/plain",
    )


# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">ResearchMind · Multi-Agent Pipeline · Built with Streamlit</div>
""", unsafe_allow_html=True)