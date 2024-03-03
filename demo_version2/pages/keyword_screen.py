import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
import pyperclip

if "keywords" not in st.session_state:
    st.session_state["keywords"] = None 


def generate_output(content_text):
    prompt_template = """
    You've been given a task to generate keywords that accurately represent the content of the following {paragraph}. Ensure that the keywords are relevant, specific, and provide insight into the main topics and themes discussed in the text. Aim to produce a diverse range of keywords that cover different aspects of the paragraph. Consider the context and relationships between words, phrases, and sentences when generating keywords. list of keywords and follow language and grammar rules for keyword generation. Generated the comma seperated list of the keywords.
    """

    prompt = PromptTemplate.from_template(template=prompt_template)

    prompt_formatted_str = prompt.format(paragraph=content_text)
    llm = OpenAI(temperature=0, model_name="gpt-4")

    # Generate question
    prediction = llm.predict(prompt_formatted_str)
    return prediction

def copy_to_clipboard(text):
    # Function to copy text to clipboard
    pyperclip.copy(text)
    st.success("Text has been copied to clipboard")

def main():
    st.title("Keywords Generator")

    # Input box for user input with increased height
    content = st.text_area("Enter your text:", height=200)

    # Button to trigger generation
    if st.button("Generate"):
        with st.spinner("Generating..."):
            # Call generate_output function with input_text
            output_text = generate_output(content)
            st.write("Generated Keywords: \n" + output_text)
            # st.write(st.session_state["Model"])
            # st.write(st.session_state["LO"])
            st.session_state["keywords"] = output_text

            # Button to copy output to clipboard
            st.button("Copy to Clipboard", on_click=copy_to_clipboard, args=(output_text,))
            
            # copy_to_clipboard(output_text)

if __name__ == "__main__":
    main()
