import streamlit as st

import llm
from exceptions import NoApiKeyError


OPENAI_MODELS = {"text-davinci-003": "Davinci", "text-ada-001": "Ada", "gpt-3.5-turbo": "GPT-3.5"}

def openAI_model_dropdown_func(option):
    """
    Small hack to have separate name-value pair in OpenAI model dropdown, since
    Streamlit selectbox does not support it directly.
    """

    return OPENAI_MODELS[option]

def openAI_api_key_sidebar() -> str:
    """
    Add a sidebar with a text input field.
    User can input the OpenAI API key using the text input.
    """

    return st.sidebar.text_input("OpenAI API key")

def openAI_text_model_dropdown() -> str:
    """
    User can select the OpenAI text model to be used for generating the response.
    """

    return st.sidebar.selectbox("Choose an OpenAI model", options = OPENAI_MODELS.keys(), format_func = openAI_model_dropdown_func)


def temperature_slider() -> float:
    """
    User can change OpenAI temperature using a slider
    """

    return st.slider(
        label = "Temperature",
        min_value = 0.0,
        max_value = 2.0,
        step = 0.25,
        value = 0.75,
        help = """
            Higher temperatures add more randomness in the AI response.
            Use lower temperature if you need stable outputs (factual outputs/classifications etc.).
            Use higher temperatures if you want the AI to generate stories/poems, although very high temperatures
            might make the AI generate weird responses.
            """
    )

def prompt_form(api_key: str, model: str):
    """
    Add a form where user can provide the prompt input.
    On submit, OpenAI will return the AI-generated content,
    which will be displayed as a text output.
    """

    with st.form("prompt-form"):
        question_text = st.text_area("Send a message")
        temp = temperature_slider()
        submit = st.form_submit_button("Submit")

        if not api_key:
            raise NoApiKeyError()

        if submit:
            st.info(llm.generate_ai_reply(question_text, model, temp, api_key))
