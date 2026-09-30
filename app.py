import streamlit as st
from main import run_pipeline, ask_question


# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="AI Video Assistant",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ─────────────────────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────────────────────

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: #0e1117;
    }

    /* Header */
    .hero {
        padding: 15px 10px 25px 10px;
        text-align: left;
    }

    .hero-title {
        font-size: 38px;
        font-weight: 800;
        margin-bottom: 5px;
        background: linear-gradient(90deg, #7c3aed, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Cards */
    .card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
    }

    .card-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    /* Metric cards */
    .metric-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 18px;
        text-align: center;
    }

    .metric-number {
        font-size: 28px;
        font-weight: 700;
    }

    .metric-label {
        color: #8b949e;
        font-size: 14px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #0b0f14;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }

</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────

if "result" not in st.session_state:
    st.session_state.result = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ─────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────

st.markdown("""
<div class="hero">
    <div class="hero-title">
        🎥 AI Video Assistant
    </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────

with st.sidebar:

    st.markdown("## ⚙️ Video Settings")

    source = st.text_input(
        "YouTube URL or Local File",
        placeholder="https://youtube.com/watch?v=..."
    )

    language = st.selectbox(
        "🎙️ Audio Language",
        ["english", "urdu"]
    )

    st.markdown("---")

    process_button = st.button(
        "🚀 Process Video",
        use_container_width=True,
        type="primary"
    )

    st.markdown("---")

    st.markdown("""
    ### 🧠 How it works

    1. 🎥 Get video/audio
    2. 🎙️ Whisper transcription
    3. ✂️ Split transcript
    4. 🧠 Generate embeddings
    5. 🗄️ Store in Chroma
    6. 🤖 Generate insights
    7. 💬 Chat with your video
    """)

    st.markdown("---")

    st.caption("AI Video Assistant")
    st.caption("Powered by Whisper + Chroma + Groq")


# ─────────────────────────────────────────────────────────────
# PROCESS VIDEO
# ─────────────────────────────────────────────────────────────

if process_button:

    if not source:

        st.warning(
            "⚠️ Please enter a YouTube URL or local file path."
        )

    else:

        st.session_state.chat_history = []

        progress = st.progress(0)

        status = st.empty()

        try:

            status.info("🎥 Downloading and preparing audio...")
            progress.progress(10)

            with st.spinner(
                "Processing video... This may take a few minutes."
            ):

                result = run_pipeline(
                    source,
                    language
                )

            progress.progress(100)

            st.session_state.result = result

            status.success(
                "✅ Video processed successfully!"
            )

            st.toast(
                "Video processing completed!",
                icon="🎉"
            )

        except Exception as e:

            progress.empty()

            st.error(
                f"❌ Something went wrong:\n\n{str(e)}"
            )


# ─────────────────────────────────────────────────────────────
# RESULTS
# ─────────────────────────────────────────────────────────────

result = st.session_state.result


if result:

    # ─────────────────────────────────────────────────────────
    # TITLE
    # ─────────────────────────────────────────────────────────

    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">
                📌 {result["title"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    # ─────────────────────────────────────────────────────────
    # METRICS
    # ─────────────────────────────────────────────────────────

    transcript = result["transcript"]

    word_count = len(transcript.split())

    char_count = len(transcript)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">
                    {word_count:,}
                </div>
                <div class="metric-label">
                    Transcript Words
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">
                    {char_count:,}
                </div>
                <div class="metric-label">
                    Characters
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-number">
                    RAG
                </div>
                <div class="metric-label">
                    AI Knowledge Base
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("")


    # ─────────────────────────────────────────────────────────
    # RESULT TABS
    # ─────────────────────────────────────────────────────────

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📋 Summary",
            "📝 Transcript",
            "✅ Action Items",
            "🔑 Decisions",
            "❓ Questions"
        ]
    )


    # ─────────────────────────────────────────────────────────
    # SUMMARY
    # ─────────────────────────────────────────────────────────

    with tab1:

        st.markdown("### 📋 Meeting Summary")

        st.markdown(
            result["summary"]
        )


    # ─────────────────────────────────────────────────────────
    # TRANSCRIPT
    # ─────────────────────────────────────────────────────────

    with tab2:

        st.markdown("### 📝 Full Transcript")

        st.text_area(
            "Transcript",
            transcript,
            height=500,
            label_visibility="collapsed"
        )


    # ─────────────────────────────────────────────────────────
    # ACTION ITEMS
    # ─────────────────────────────────────────────────────────

    with tab3:

        st.markdown("### ✅ Action Items")

        st.markdown(
            result["action_items"]
        )


    # ─────────────────────────────────────────────────────────
    # DECISIONS
    # ─────────────────────────────────────────────────────────

    with tab4:

        st.markdown("### 🔑 Key Decisions")

        st.markdown(
            result["key_decisions"]
        )


    # ─────────────────────────────────────────────────────────
    # QUESTIONS
    # ─────────────────────────────────────────────────────────

    with tab5:

        st.markdown("### ❓ Open Questions")

        st.markdown(
            result["open_questions"]
        )


    # ─────────────────────────────────────────────────────────
    # RAG CHAT
    # ─────────────────────────────────────────────────────────

    st.markdown("---")

    st.markdown("## 💬 Chat With Your Video")

    st.caption(
        "Ask questions about the video. "
        "Answers are generated using your transcript and RAG pipeline."
    )


    # Display chat history

    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.markdown(
                message["content"]
            )


    # Chat input

    question = st.chat_input(
        "Ask something about the video..."
    )


    if question:

        # User message

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):

            st.markdown(question)


        # Assistant response

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                answer = ask_question(
                    result["rag_chain"],
                    question
                )

            st.markdown(answer)


        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


# ─────────────────────────────────────────────────────────────
# LANDING PAGE
# ─────────────────────────────────────────────────────────────

else:

    st.markdown("## ✨ What can it do?")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="card">

        ### 🎙️ Smart Transcription

        Convert YouTube videos or audio files into
        accurate text using local Whisper.

        </div>
        """, unsafe_allow_html=True)


    with col2:

        st.markdown("""
        <div class="card">

        ### 🧠 AI Insights

        Automatically generate titles, summaries,
        action items, decisions and open questions.

        </div>
        """, unsafe_allow_html=True)


    with col3:

        st.markdown("""
        <div class="card">

        ### 💬 RAG Chat

        Ask questions about your video and retrieve
        relevant information from the transcript.

        </div>
        """, unsafe_allow_html=True)


    st.markdown("")

    st.info(
        "👈 Enter a YouTube URL or local audio/video file "
        "from the sidebar to get started."
    )