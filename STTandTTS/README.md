# 🗣️ Voice Assistant with Silero STT & TTS + Mistral AI LLM 

This project implements a simple **offline voice assistant** that listens to speech, generates a response using a local LLM, and replies with synthesized voice.

---

## 🚀 Overview

This assistant performs three main tasks:

1. **Speech-to-Text (STT)**: Converts speech input into text using [Silero STT models](https://github.com/snakers4/silero-models).
2. **Text Processing**: Passes the transcribed text to a **locally installed Mistral AI model** (via Hugging Face) for generating a suitable response.
3. **Text-to-Speech (TTS)**: Converts the response back into speech using [Silero TTS models](https://github.com/snakers4/silero-models).

All components are open-source and can run fully offline (after initial downloads).

---

## 🛠️ Technologies Used

- **[Silero STT & TTS](https://github.com/snakers4/silero-models)**:
  - Lightweight, accurate models for speech-to-text and text-to-speech.
  - Runs efficiently on CPU and GPU.
- **[Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)**:
  - An open-source large language model (LLM) used for natural conversation and answering queries.
  - Installed locally using Hugging Face Transformers.

---

## 🧩 Implementation Summary

### 1. Speech-to-Text (STT)
I used Silero’s pretrained STT model to convert voice input to text:
```python
import torch
model = torch.hub.load('snakers4/silero-models', 'silero_stt', language='en')
