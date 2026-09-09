import streamlit as st

st.set_page_config(page_title="AI Productivity Assistant", layout="wide")
st.title("🤖 AI-Powered Productivity Assistant")
st.markdown("Automating workplace tasks with AI | CAPACITI Project - Sinesipho Mbungwana")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📧 Email", "📝 Meeting Summary", "📅 Task Planner", "🔍 Research", "💬 Chatbot"])

with tab1:
    st.header("Email Generation")
    prompt = st.text_area("What email do you want to generate?", key="email")
    if st.button("Generate Email"):
        st.success(f"Subject: Re: {prompt}\n\nDear Team,\n\nRegarding {prompt}, please see below.\n\nThis draft was generated using Role Prompting.\n\nBest regards,\nSinesipho")

with tab2:
    st.header("Meeting Summarization")
    transcript = st.text_area("Paste meeting transcript", key="meet")
    if st.button("Summarize"):
        st.write("**Summary:**\n- Key Point: Project deadline discussed\n- Action Items: Update GitHub repo\n- Decision: Use Streamlit for deployment")
        st.caption("Technique: Chain-of-Thought")

with tab3:
    st.header("Task Planning")
    goal = st.text_input("Enter your goal", key="goal")
    if st.button("Create Plan"):
        st.write(f"**Plan for: {goal}**\n1. Research\n2. Draft\n3. Review & Submit")

with tab4:
    st.header("Research Assistance")
    topic = st.text_input("Research topic", key="research")
    if st.button("Research"):
        st.write(f"Summary for {topic}: AI tools like ChatGPT and Gemini help automate workplace tasks efficiently. (Demo)")

with tab5:
    st.header("Workplace Chatbot")
    q = st.text_input("Ask me anything", key="chat")
    if st.button("Ask"):
        st.write(f"Answer to '{q}': I can help you automate that task with AI!")

st.sidebar.info("Tools: ChatGPT, Gemini\nEthical Use: No private data stored, human review required")
