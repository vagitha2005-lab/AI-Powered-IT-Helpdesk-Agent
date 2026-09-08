import streamlit as st
from agent import troubleshoot


st.set_page_config(
    page_title="AI IT Helpdesk Agent",
    page_icon="🛠️",
    layout="centered"
)

st.title("🛠️ AI IT Helpdesk Agent")
st.subheader("Intelligent Troubleshooting System")

st.write(
    "Describe your IT problem and get troubleshooting guidance "
    "from the AI IT Helpdesk Agent."
)

st.divider()

problem = st.text_area(
    "Describe your IT problem:",
    placeholder=(
        "Example: My Wi-Fi is connected, "
        "but I cannot access the internet."
    ),
    height=150
)

if st.button("Get Troubleshooting Help"):

    if problem.strip() == "":
        st.warning("Please describe your IT problem first.")

    else:
        with st.spinner("Analyzing your problem..."):
            result = troubleshoot(problem)

        st.success("Troubleshooting completed!")

        st.subheader("Your Problem")
        st.info(problem)

        st.subheader("AI Troubleshooting Result")
        st.write(result)