from dotenv import load_dotenv
load_dotenv()
import anthropic
import streamlit as st

client = anthropic.Anthropic()

def get_response(user_content):
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        system="Generate 5 attention-grabbing blog titles based on user-provided keywords",
        messages=[{"role": "user", "content": user_content}]
    )
    return response.content[0].text





st.title('Blog Title Generator 📝')
user_content = st.text_input('Enter your keywords for blog title:')

if st.button("Generate Blog Titles"):
    if not user_content:
        st.warning("Please enter your keywords", icon="warning")
    generator_titles = get_response(user_content)   
    st.success("Title generated successfully! 🎉")
    st.text_area("", value=generator_titles, height=300, max_chars=None, key=None)        


