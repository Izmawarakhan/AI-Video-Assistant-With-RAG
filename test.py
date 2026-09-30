from dotenv import load_dotenv

load_dotenv()   # MUST be before any core/ imports


from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summarized import summarize, generate_title
from core.extractor import (
    extract_action_items,
    extract_key_decisions,
    extract_questions
)


source = "https://www.youtube.com/watch?v=Tyg24n4zOcE"


# =========================================================
# PROCESS AUDIO
# =========================================================

chunks = process_input(source)


# =========================================================
# TRANSCRIBE + URDU → ENGLISH TRANSLATION
# =========================================================

transcript = transcribe_all(
    chunks,
    language="urdu",
    translate=True
)

print("\n" + "=" * 60)
print("📝 TRANSCRIPT / ENGLISH TRANSLATION")
print("=" * 60)

print(
    transcript[:500] + "..."
    if len(transcript) > 500
    else transcript
)


# =========================================================
# TITLE + SUMMARY
# =========================================================

title = generate_title(transcript)
summary = summarize(transcript)


print("\n" + "=" * 60)
print(f"📌 TITLE: {title}")
print("=" * 60)

print("\n📋 SUMMARY")
print("-" * 60)
print(summary)


# =========================================================
# ACTION ITEMS
# =========================================================

action_items = extract_action_items(transcript)


# =========================================================
# KEY DECISIONS
# =========================================================

decisions = extract_key_decisions(transcript)


# =========================================================
# OPEN QUESTIONS
# =========================================================

questions = extract_questions(transcript)


# =========================================================
# DISPLAY RESULTS
# =========================================================

print("\n" + "=" * 60)
print("✅ ACTION ITEMS")
print("=" * 60)
print(action_items)


print("\n" + "=" * 60)
print("🔑 KEY DECISIONS")
print("=" * 60)
print(decisions)


print("\n" + "=" * 60)
print("❓ OPEN QUESTIONS")
print("=" * 60)
print(questions)