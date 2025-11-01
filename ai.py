from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
  ChatPromptTemplate,
  SystemMessagePromptTemplate,
  HumanMessagePromptTemplate
)


def get_response(expert: str, question: str) -> str:
  """
  指定された専門家と質問に基づいてLLMからの応答を取得する関数
  """

  llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

  messages = _create_prompt(expert, question)

  response = llm(messages)
  return response.content


def _create_prompt(expert: str, question: str) -> list:
  """
  プロンプト作成のみを行う関数
  """

  system_template = "あなたは、きのこの山たけのこの里の{expert}派閥のリーダーAIです。ユーザーからの質問に100文字以内で回答してください。お互い相手には辛辣な態度を取ります。"
  human_template = "{question}"

  prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template),
  ])

  messages = prompt.format_messages(question=question, expert=expert)
  return messages
