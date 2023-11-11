import logging

import streamlit as st
from openai import AuthenticationError, RateLimitError

import components
from exceptions import NoApiKeyError


logging.basicConfig(level=logging.INFO)

def init():
    """
    Landing page
    """

    st.set_page_config(page_title="LangChain-OpenAI Demo App")
    st.title("LangChain-OpenAI Demo app")

    api_key = components.openAI_api_key_sidebar()
    model = components.openAI_text_model_dropdown()

    try:
        components.prompt_form(api_key, model)
    except NoApiKeyError:
        st.warning("Please enter your OpenAI API key")
    except AuthenticationError:
        st.warning("OpenAI authentication failed. Please provide a valid API key")
    except RateLimitError:
        st.warning("You have exceeded your quota in OpenAI. Please check your OpenAI plan and billing details")
    except Exception as e:
        logging.error(f"Unknown error: {e}", exc_info = True)
        st.warning("Something went wrong at our end. Please re-try later")


if __name__ == '__main__':
    init()
