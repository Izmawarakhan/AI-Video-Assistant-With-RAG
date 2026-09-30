# 🎥 AI Video Assistant With RAG

An AI-powered video assistant that converts **YouTube videos or local audio/video files into searchable knowledge**.

The application uses **Whisper for speech-to-text, Hugging Face embeddings for semantic search, ChromaDB as the vector database, and Groq LLMs for AI-powered summarization, information extraction, and RAG-based question answering.**

## 🚀 Live Demo

**Try the application here:**

[AI Video Assistant With RAG — Live Demo](https://ai-video-assistant-with-rag-0.streamlit.app)

---

## ✨ Features

* 🎥 Process YouTube videos
* 📁 Process local audio/video files
* 🎙️ Speech-to-text using local OpenAI Whisper
* 🌐 English and Urdu transcription support
* 📝 Automatic transcript generation
* 📌 AI-generated video title
* 📋 AI-generated summary
* ✅ Action item extraction
* 🔑 Key decision extraction
* ❓ Open question extraction
* 🧠 Semantic search using embeddings
* 🗄️ ChromaDB vector database
* 🔍 RAG-based question answering
* 💬 Interactive chat with the processed video
* ⚡ Groq-powered LLM inference
* 🌐 Streamlit web interface

---

# 🧠 How It Works

The complete pipeline follows:

```text
YouTube URL / Local Video
            ↓
     Audio Extraction
            ↓
      Audio Conversion
            ↓
       Audio Chunking
            ↓
          Whisper
            ↓
        Transcript
            ↓
    ┌───────┴────────┐
    ↓                ↓
AI Insights       RAG Pipeline
    ↓                ↓
Title            Text Chunking
Summary              ↓
Actions          Embeddings
Decisions             ↓
Questions         ChromaDB
                     ↓
                  Retriever
                     ↓
               User Question
                     ↓
              Relevant Context
                     ↓
                 Groq LLM
                     ↓
                  Answer
```

---

# 🔥 RAG Pipeline

The main intelligent feature of this project is **Retrieval-Augmented Generation (RAG)**.

Instead of sending the entire transcript to the LLM every time a user asks a question, the transcript is converted into smaller chunks and stored as vectors.

When the user asks a question:

```text
User Question
      ↓
Question Embedding
      ↓
Semantic Similarity Search
      ↓
ChromaDB
      ↓
Relevant Transcript Chunks
      ↓
Context + Question
      ↓
Groq LLM
      ↓
Final Answer
```

This allows the assistant to answer questions using information retrieved directly from the processed video transcript.

---

# 🏗️ System Architecture

```text
                    USER
                     │
                     ▼
            ┌─────────────────┐
            │   Streamlit UI  │
            │     app.py      │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │     main.py     │
            │   Orchestrator  │
            └────────┬────────┘
                     │
                     ▼
             ┌───────────────┐
             │ Input Source  │
             └───────┬───────┘
                     │
              ┌──────┴──────┐
              ↓             ↓
         YouTube URL     Local File
              ↓             ↓
           yt-dlp       pydub/FFmpeg
              └──────┬──────┘
                     ↓
                  WAV Audio
                     ↓
               Audio Chunks
                     ↓
                  Whisper
                     ↓
                Transcript
                     │
          ┌──────────┴──────────┐
          ↓                     ↓
     AI Insights             RAG
          ↓                     ↓
   Summary/Actions          Embeddings
   Decisions/Questions          ↓
                            ChromaDB
                                ↓
                            Retriever
                                ↓
                         User Question
                                ↓
                       Retrieved Context
                                ↓
                            Groq LLM
                                ↓
                             Answer
                                ↓
                         Streamlit Chat
```

---

# 🛠️ Tech Stack

## Frontend

* **Streamlit**

## Speech Recognition

* **OpenAI Whisper**
* PyTorch
* Torchaudio

## Audio / Video Processing

* **yt-dlp**
* **pydub**
* **FFmpeg**

## LLM

* **Groq**
* `openai/gpt-oss-20b`
* LangChain

## Embeddings

* **Hugging Face**
* `all-MiniLM-L6-v2`
* Sentence Transformers

## Vector Database

* **ChromaDB**

## Programming Language

* **Python 3.10+**

---

# 📂 Project Structure

```text
AI Video Assistant With RAG/
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
│
├── core/
│   ├── transcriber.py
│   ├── summarized.py
│   ├── extractor.py
│   ├── vector_store.py
│   └── rag_engine.py
│
├── utils/
│   └── audio_processor.py
│
└── README.md
```

---

# 📌 Module Responsibilities

### `app.py`

The Streamlit frontend.

Responsible for:

* User input
* Language selection
* Processing button
* Progress indicators
* Transcript display
* Summary display
* Action items
* Decisions
* Open questions
* RAG chat

---

### `main.py`

The main pipeline controller.

It connects all components:

```python
process_input()
        ↓
transcribe_all()
        ↓
generate_title()
        ↓
summarize()
        ↓
extract_action_items()
        ↓
extract_key_decisions()
        ↓
extract_questions()
        ↓
build_rag_chain()
```

---

### `utils/audio_processor.py`

Responsible for:

* Detecting YouTube URLs
* Downloading audio
* Converting media to WAV
* Standardizing audio
* Splitting audio into chunks

The current audio processing uses:

```text
Mono
16 kHz
10-minute chunks
```

---

### `core/transcriber.py`

Responsible for speech recognition using Whisper.

```text
Audio
  ↓
Whisper
  ↓
Text
```

The application supports:

```text
English → en
Urdu → ur
```

---

### `core/summarized.py`

Responsible for:

* Generating the title
* Generating the summary

The LLM is accessed through LangChain's `ChatGroq`.

---

### `core/extractor.py`

Extracts:

* Action items
* Key decisions
* Open questions

from the transcript.

---

### `core/vector_store.py`

Responsible for the RAG knowledge base.

The transcript is:

```text
Transcript
    ↓
500-character chunks
    ↓
50-character overlap
    ↓
Embeddings
    ↓
ChromaDB
```

Embedding model:

```text
all-MiniLM-L6-v2
```

---

### `core/rag_engine.py`

Responsible for:

* Creating the retriever
* Retrieving relevant transcript chunks
* Passing context to the LLM
* Generating the final answer

---

# 🔄 Detailed Processing Flow

## 1. Input

The user provides:

```text
YouTube URL
```

or:

```text
Local audio/video file
```

---

## 2. Audio Processing

For YouTube:

```text
URL
 ↓
yt-dlp
 ↓
Audio
 ↓
WAV
```

For local files:

```text
MP4 / MP3 / other media
 ↓
pydub + FFmpeg
 ↓
WAV
```

---

## 3. Audio Chunking

Long audio is divided into smaller chunks.

Current configuration:

```text
10 minutes per chunk
```

---

## 4. Transcription

Whisper processes every audio chunk.

```text
Audio Chunk
    ↓
Whisper
    ↓
Text
```

All chunks are then combined into one complete transcript.

---

## 5. AI Insights

The transcript is passed to the LLM to generate:

```text
Title
Summary
Action Items
Key Decisions
Open Questions
```

---

## 6. RAG Knowledge Base

The transcript is split into smaller text chunks.

```text
Transcript
    ↓
Text Splitter
    ↓
Document Chunks
    ↓
Embedding Model
    ↓
Vector Embeddings
    ↓
ChromaDB
```

---

## 7. Question Answering

The user asks a question:

```text
"What is RAG?"
```

The system:

```text
Question
   ↓
Embedding
   ↓
Similarity Search
   ↓
Relevant Transcript Chunks
   ↓
Context
   ↓
Groq LLM
   ↓
Answer
```

---

# ⚙️ Configuration

### Whisper

Default model:

```text
small
```

It can be controlled using:

```text
WHISPER_MODEL
```

---

### Embedding Model

```text
all-MiniLM-L6-v2
```

---

### Vector Store

```text
ChromaDB
```

Collection:

```text
meeting_transcript
```

Persistence directory:

```text
vector_db
```

---

### Vector Chunking

```text
Chunk Size: 500 characters
Chunk Overlap: 50 characters
```

---

### Retriever

```text
Search Type: similarity
Top K: 4
```

---

### LLM

```text
Provider: Groq
Model: openai/gpt-oss-20b
Temperature: 0.3
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Izmawarakhan/AI-Video-Assistant-With-RAG.git
```

Move into the project directory:

```bash
cd AI-Video-Assistant-With-RAG
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

If you want to change the Whisper model:

```env
WHISPER_MODEL=small
```

---

# ▶️ Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

---

# 💬 Example Usage

### Step 1

Enter a YouTube URL:

```text
https://www.youtube.com/watch?v=XXXXXXXX
```

### Step 2

Select the audio language:

```text
English
```

or:

```text
Urdu
```

### Step 3

Click:

```text
🚀 Process Video
```

### Step 4

The application generates:

* 📌 Title
* 📋 Summary
* 📝 Transcript
* ✅ Action Items
* 🔑 Key Decisions
* ❓ Open Questions

### Step 5

Ask questions in:

```text
💬 Chat With Your Video
```

For example:

```text
What are the main topics discussed?
```

```text
Explain the main concept in simple words.
```

```text
What decisions were made?
```

```text
What are the important points from the video?
```

#

---

# 🎯 Use Cases

This project can be used for:

* 🎓 Lecture summarization
* 🧑‍💼 Meeting analysis
* 📚 Educational videos
* 🎤 Interviews
* 🎥 YouTube research
* 📝 Video note generation
* 🔎 Searching long videos
* 🤖 Question answering over video content

---

# 📈 Future Improvements

Potential improvements include:

* ⏱️ Timestamp-based answers
* 🎬 Direct video playback
* 📄 PDF report generation
* 📥 Transcript download
* 🌐 More language support
* 🧠 Better conversational memory
* 🎯 Improved retrieval strategies
* 📊 RAG evaluation metrics
* 🖼️ Video frame analysis
* 🎤 Voice-based questions
* ☁️ Cloud vector database
* ⚡ GPU-based Whisper inference

---

# 👩‍💻 Author

**Izma Wara Khan**

Software Engineering | AI/ML | Generative AI | RAG

GitHub:
[Izmawarakhan](https://github.com/Izmawarakhan)

---

# ⭐ Project Highlights

```text
🎥 Video → Audio
🎙️ Audio → Transcript
🧠 Transcript → AI Insights
🔢 Text → Embeddings
🗄️ Embeddings → ChromaDB
🔍 Question → Relevant Context
🤖 Context + Question → LLM
💬 LLM → Final Answer
```

### Core Concept

> **Turn any video into a searchable AI knowledge base and chat with its content using Retrieval-Augmented Generation (RAG).**
