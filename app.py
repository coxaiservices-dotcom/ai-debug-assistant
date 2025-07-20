import streamlit as st
from debug_engine import analyze_code

st.title("AI Debug Assistant")

st.write("Upload your code file and paste the error message for analysis.")

uploaded_file = st.file_uploader("Upload Code File", type=["py", "cpp"])
error_text = st.text_area("Paste Error Message")

if st.button("Analyze"):
    if uploaded_file and error_text:
        code = uploaded_file.read().decode()
        result = analyze_code(code, error_text)
        st.write(result)
    else:
        st.error("Please upload a code file and paste an error message.")
