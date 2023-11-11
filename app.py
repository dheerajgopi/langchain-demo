import streamlit as st
from langchain.llms.openai import OpenAI
from openai import AuthenticationError, RateLimitError

from exceptions import NoApiKeyError


def openAI_api_key_sidebar() -> str:
    """
    Add a sidebar with a text input field.
    User can input the OpenAI API key using the text input.
    """

    return st.sidebar.text_input("OpenAI API key")

def generate_answer(usr_input: str, api_key: str) -> str:
    """
    Use OpenAI to generate content based on user input.
    """

    llm = OpenAI(temperature=0.7, api_key=api_key)
    return llm(usr_input)

def qa_form(api_key: str):
    """
    Add a form where user can provide the prompt input.
    On submit, OpenAI will return the AI-generated content,
    which will be displayed as a text output.
    """

    with st.form('qa-form'):
        question_text = st.text_area("Enter your question")
        submit = st.form_submit_button("Submit")

        if not api_key:
            raise NoApiKeyError()

        if submit:
            st.info(generate_answer(question_text, api_key))

def init():
    """
    Landing page
    """

    st.set_page_config(page_title="LangChain-OpenAI Demo App")
    st.title("LangChain-OpenAI Demo app")

    api_key = openAI_api_key_sidebar()
    try:
        qa_form(api_key)
    except NoApiKeyError:
        st.warning("Please enter your OpenAI API key")
    except AuthenticationError:
        st.warning("OpenAI authentication failed. Please provide a valid API key")
    except RateLimitError:
        st.warning("You have exceeded your quota in OpenAI. Please check your OpenAI plan and billing details")
    except Exception:
        st.warning("Something went wrong at our end. Please re-try later")


if __name__ == '__main__':
    init()
