import streamlit as st
import requests

st.set_page_config(
    page_title="TouchGrass AI",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 TouchGrass AI")
st.subheader("Stop scrolling. Start exploring.")

st.write(
    "Tell us about your free time and let local AI "
    "create a real-world outdoor mission."
)

time_available = st.selectbox(
    "⏱️ How much time do you have?",
    ["15 minutes", "30 minutes", "1 hour", "2 hours"]
)

activity = st.selectbox(
    "🌿 What would you like to do?",
    [
        "Nature",
        "Walking",
        "Running",
        "Photography",
        "Bird watching",
        "Gardening",
        "Something relaxing"
    ]
)

company = st.selectbox(
    "👥 Who are you with?",
    ["Alone", "Friend", "Family", "Group"]
)

if st.button("🌱 Generate My Mission", use_container_width=True):

    prompt = f"""
You are TouchGrass AI, an outdoor activity coach.

Create a fun, practical outdoor mission.

User information:
- Available time: {time_available}
- Preferred activity: {activity}
- Company: {company}

Requirements:
- The activity must happen outdoors.
- Make it realistic for the available time.
- Give 3 to 5 simple steps.
- Encourage the user to spend less time looking at their phone.
- Make it fun and motivating.
- Do not require expensive equipment.

Return the result with:
1. A short mission title
2. A short description
3. 3 to 5 activity steps
4. One motivational final sentence

Keep the response concise.
"""

    with st.spinner("🧠 Creating your outdoor mission..."):

        try:
            response = requests.post(
                "http://localhost:11434/api/chat",
                json={
                    "model": "llama3.2:3b",
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            mission = data["message"]["content"]

            st.success("Your outdoor mission is ready! 🌱")

            st.markdown("### 🌳 Your Mission")

            st.write(mission)

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Cannot connect to Ollama. "
                "Please make sure Ollama is running."
            )

        except Exception as e:

            st.error(f"❌ Error: {e}")