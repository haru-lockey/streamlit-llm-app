import streamlit as st
from ai import get_response  # ai.pyから関数をインポート

st.title("きのこたけのこ討論")

# radio button
selected_expert = st.radio(
    "専門家を選択してください。",
    ["きのこさん", "たけのこさん"]
)

# form
input_message = st.text_input(label="質問を入力してください。")

# button
if st.button("ご意見を伺う"):
  response = get_response(selected_expert, input_message)
  st.write(response)
