import streamlit as st
from transformers import pipeline

from text_utils import clean_text, split_for_model


st.set_page_config(page_title="Study Note Summarizer", page_icon="📝")
st.title("📝 Study Note Summarizer")
st.caption("A small GenAI app prepared for Assignment 39 deployment practice")


@st.cache_resource(show_spinner="Loading the summarization model for the first time...")
def load_summarizer():
    return pipeline("text2text-generation", model="google/flan-t5-small")


def summarize(text, length):
    cleaned = clean_text(text)
    chunks = split_for_model(cleaned)
    summaries = []
    max_tokens = {"Short": 70, "Medium": 120, "Detailed": 180}[length]

    model = load_summarizer()
    for chunk in chunks:
        prompt = "Summarize these study notes clearly in simple language:\n" + chunk
        result = model(prompt, max_new_tokens=max_tokens, do_sample=False)
        summaries.append(result[0]["generated_text"].strip())
    return "\n\n".join(summaries)


sample = """Generative AI creates new content such as text, images, audio, and code.
Large language models learn patterns from large text collections. A prompt gives the model
instructions and context. Clear prompts usually produce more useful answers. Generated
answers should still be checked because a model can return incorrect information."""

if "notes" not in st.session_state:
    st.session_state.notes = ""

with st.sidebar:
    st.header("Options")
    length = st.radio("Summary length", ["Short", "Medium", "Detailed"], index=1)
    if st.button("Load sample notes"):
        st.session_state.notes = sample
        st.rerun()
    st.info("The first response is slower because the model downloads and loads once.")

notes = st.text_area(
    "Paste your notes",
    key="notes",
    height=260,
    placeholder="Paste a paragraph, meeting note, or study material here...",
)

left, right = st.columns([1, 4])
with left:
    run = st.button("Summarize", type="primary")
with right:
    st.caption(f"{len(notes)} characters")

if run:
    cleaned = clean_text(notes)
    if len(cleaned) < 80:
        st.warning("Please enter at least 80 characters so the summary is meaningful.")
    else:
        try:
            with st.spinner("Preparing your summary..."):
                answer = summarize(cleaned, length)
            st.subheader("Summary")
            st.write(answer)
            st.download_button("Download summary", answer, "summary.txt", "text/plain")
        except Exception as error:
            st.error("The model could not load or generate a response. Please try again.")
            with st.expander("Technical details"):
                st.code(str(error))

