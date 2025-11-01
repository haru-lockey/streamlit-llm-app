import streamlit as st
from ai import get_response  # ai.pyから関数をインポート

st.title("Streamlit LLM App")

# radio button
selected_expert = st.radio(
    "専門家を選択してください。",
    ["きのこさん", "たけのこさん"]
)

# form
input_message = st.text_input(label="プロンプトを入力してください。")

# button
if st.button("実行"):
  response = get_response(selected_expert, input_message)
  st.write(response)
