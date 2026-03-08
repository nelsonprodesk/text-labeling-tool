import streamlit as st
import json

st.title("Text Labeling Tool")

dataset = [
    "AI is transforming healthcare",
    "Machine learning requires data",
    "Python is great for AI"
]

labels = []

for text in dataset:
    label = st.text_input(f"Label for: {text}")
    if label:
        labels.append({"text": text, "label": label})

if st.button("Save Labels"):
    with open("labels.json", "w") as f:
        json.dump(labels, f)

    st.success("Labels saved!")
