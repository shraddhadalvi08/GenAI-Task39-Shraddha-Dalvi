---
title: Study Note Summarizer
emoji: 📝
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
short_description: A small Streamlit GenAI summarizer for deployment practice
---

# Assignment 39 - GenAI App Deployment

**Student:** Shraddha Dalvi  
**Application:** Study Note Summarizer

## Project idea

For this assignment, I made a small GenAI app that summarizes study notes. A user can paste text, choose a short, medium, or detailed summary, and download the result. I selected `google/flan-t5-small` because it is much lighter than many large models and does not require a paid API key.

The app also cleans repeated spaces and splits long notes into smaller pieces before sending them to the model. This helped me understand that deployment is not only about uploading `app.py`; dependency size, startup time, and input limits also matter.

## Files

- `app.py` - Streamlit interface and summarization pipeline.
- `text_utils.py` - small text cleaning and chunking functions.
- `requirements.txt` - packages installed by both platforms.
- `Dockerfile` - current Hugging Face Spaces method for a Streamlit app.
- `.streamlit/config.toml` - simple visual settings without changing the port.
- `DEPLOYMENT_CHECKLIST.md` - step-by-step deployment tasks.
- `DEPLOYMENT_EVIDENCE.md` - place for real URLs and screenshots after deployment.
- `PLATFORM_COMPARISON.md` - Task 3 observations.
- `test_text_utils.py` - quick test for the non-model functions.

## Run locally

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

The first run needs internet access to download the model. Later runs can reuse the cached copy.

## Task 1 - Streamlit Community Cloud

1. Create a GitHub repository and upload this folder's contents.
2. Sign in to Streamlit Community Cloud and connect the GitHub account.
3. Select the repository and set the main file to `app.py`.
4. Click Deploy and wait for the model download to finish.
5. Test the sample text and copy the real public URL into `DEPLOYMENT_EVIDENCE.md`.

## Task 2 - Hugging Face Spaces

Hugging Face deprecated the built-in Streamlit SDK in April 2025, so this project uses the supported Docker method while the actual interface remains Streamlit.

1. Create a new Hugging Face Space and choose Docker.
2. Upload all project files, including `Dockerfile` and the YAML block in this README.
3. Wait until the Space status changes to Running.
4. Test the app and copy the real public URL into `DEPLOYMENT_EVIDENCE.md`.

## Testing before deployment

```powershell
python test_text_utils.py
python -m compileall .
```

I did not fill in fake deployment links because GitHub, Streamlit Cloud, and Hugging Face require the student's own accounts. The evidence page is ready to complete immediately after the two real deployments.

## What I learned

My first thought was that the same files would work everywhere automatically. The app code is reusable, but each platform needs a different entry method. Streamlit Cloud directly runs `app.py`, while the current Hugging Face setup builds the provided Dockerfile.

I also learned that small models are more suitable for free deployment. They may not produce the best possible summary, but they start faster and are easier to demonstrate within limited RAM.

## References checked

- Streamlit Community Cloud deployment: https://docs.streamlit.io/deploy/streamlit-community-cloud
- Streamlit dependencies: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies
- Hugging Face Docker Spaces: https://huggingface.co/docs/hub/spaces-sdks-docker
- Hugging Face Spaces changelog: https://huggingface.co/docs/hub/spaces-changelog

