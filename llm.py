import logging

from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


CHATTY_MODELS = ["gpt-3.5-turbo"]

def generate_ai_reply(usr_input: str, model: str, temperature: float, api_key: str) -> str:
    """
    Use OpenAI to generate content based on user input.
    """

    logging.info(f"model used: {model}")
    if is_chatty_model(model):
        chat = ChatOpenAI(model = model, temperature = temperature, api_key = api_key)
        ai_reply = chat([HumanMessage(content = usr_input)])
        return ai_reply.content
    else:
        llm = OpenAI(temperature=temperature, model=model, api_key=api_key)
        return llm(usr_input)

def is_chatty_model(model: str) -> str:
    return model in CHATTY_MODELS