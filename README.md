# 🌱 TouchGrass AI

> Stop scrolling. Start exploring.

TouchGrass AI is a local AI-powered outdoor activity companion that helps people spend less time on screens and more time in the real world.

Users tell the app how much free time they have, what outdoor activity they prefer, and who they are with. TouchGrass AI uses a locally running open-weight AI model to generate a practical outdoor mission.

## 🎯 Why TouchGrass AI?

We spend a huge amount of time looking at screens.

TouchGrass AI turns a few minutes of screen interaction into a reason to:

- 🌳 Go outside
- 🚶 Walk
- 📸 Explore
- 🐦 Observe nature
- 👨‍👩‍👧 Spend time with family and friends
- 📵 Put the phone away

The goal is simple:

**Use AI to help you stop using your screen.**

## ✨ Features

- ⏱️ Choose available time
- 🌿 Choose an outdoor activity
- 👥 Choose who you're with
- 🧠 Generate a personalized outdoor mission
- 📵 Encourages reduced phone usage
- 💻 Runs AI locally
- 🔓 Uses an open-weight AI model
- 💰 No paid AI API required

## 🤖 AI Technology

TouchGrass AI uses:

- **Llama 3.2 3B** — open-weight AI model
- **Ollama** — local AI inference
- **Streamlit** — web interface
- **Python** — application logic

The AI model runs locally through Ollama rather than sending the user's request to a cloud AI API.

## 🏗️ How It Works

```text
User
  ↓
Streamlit Interface
  ↓
Select time + activity + company
  ↓
TouchGrass AI Prompt
  ↓
Ollama
  ↓
Llama 3.2 3B
  ↓
Outdoor Mission
  ↓
🌱 Go Outside!
