import streamlit as st
import json

# Load legal data
with open("legal_data.json") as f:
    data = json.load(f)

st.title("Digi-Lawyer")

query = st.text_input("Ask your legal question:")

if query:
    found = False
    for key in data:
        if key in query.lower():
            st.write("Section:", data[key]["section"])
            st.write("Explanation:", data[key]["description"])
            st.write("Authority:", data[key]["authority"])
            found = True
            break

    if not found:
        st.write("Sorry, no matching law found.")