import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
import pyperclip


if "LO" not in st.session_state:
    st.session_state["LO"] = None 

def generate_output(content_text):
    prompt_template = """
    You've been given a task to extract the primary learning objective or objectives from the {content} provided. Your task is to identify the key concepts, skills, or outcomes that students are expected to acquire or develop as a result of engaging with the text. Consider the context, subject matter, and intended audience when identifying the learning objective. Pay close attention to the specific topics covered, instructional methods utilized, and the broader implications of genetic principles discussed in the text. Give a response in the form of a list.
    """

    prompt = PromptTemplate.from_template(template=prompt_template)

    prompt_formatted_str = prompt.format(content=content_text)
    llm = OpenAI(temperature=0, model_name="gpt-4")

    # Generate question
    prediction = llm.predict(prompt_formatted_str)
    return prediction

def copy_to_clipboard(text):
    # Function to copy text to clipboard
    pyperclip.copy(text)
    st.success("Text has been copied to clipboard")

def main():
    st.title("Learning Objective Generator")

    # Input box for user input with increased height
    content = st.text_area("Enter your text:", height=200)

    # Button to trigger generation
    if st.button("Generate"):
        with st.spinner("Generating..."):
            # Call generate_output function with input_text
            output_text = generate_output(content)
            st.write("Generated Learning Objectives: \n" + output_text)
            st.session_state["LO"] = output_text
            # st.write(st.session_state["Model"])
            # Button to copy output to clipboard
            st.button("Copy to Clipboard", on_click=copy_to_clipboard, args=(output_text,))
            
            # copy_to_clipboard(output_text)

if __name__ == "__main__":
    main()
