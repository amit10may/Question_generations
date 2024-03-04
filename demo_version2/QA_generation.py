import streamlit as st
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from jinja2 import Template
from prompt_template import PROMPT_TEMPLATE
import pyperclip


if "format" not in st.session_state:
    # st.session_state['format'] = ""
    st.session_state['format'] = "plain_text"

class Qa_Gen_Params:
    def __init__(self, learning_objective, content, keywords, ques_type, bloom_level):
        self.learning_objective = learning_objective.strip()
        self.content = content.strip()
        self.keywords = keywords.strip()
        self.ques_type = ques_type.strip()
        self.bloom_level = bloom_level.strip()

    def construct_prompt(self):
        template = Template(PROMPT_TEMPLATE)
        return template.render(type=self.ques_type, content=self.content, level=self.bloom_level, learning_objective=self.learning_objective, Keywords=self.keywords,format = st.session_state["format"])


def copy_to_clipboard(text):
    # Function to copy text to clipboard
    pyperclip.copy(text)
    st.success("Text has been copied to clipboard")


def main():
    st.title("QA Generation")

    # Get user input
    content = st.text_area("Enter the content:", height=200)
    learning_objective = st.text_area("Enter the learning objectives:", height=100)
    keywords = st.text_area("Enter the keywords (separated by commas):", height=100)
    bloom_level = st.selectbox("Select the Bloom's taxonomy level:" , ("Remember", "Understand","Apply","Analyze","Evaluate","Create"))
    
    ques_type = st.selectbox("Select the type of the questions:",("Multiple choice","Fill in the blanks" , "True or false"))
    json_checkbox = st.checkbox("JSON Output")

    if  json_checkbox:
        st.session_state["format"] = "json_format"

    if st.button("Generate Questions"):
        with st.spinner("Generating Questions..."):

            # Create an instance of Qa_Gen_Params
            params = Qa_Gen_Params(learning_objective, content, keywords, ques_type, bloom_level)

            # Generate prompt using Qa_Gen_Params
            prompt = params.construct_prompt()

            # Initialize OpenAI model
            llm = OpenAI(temperature=0, model_name="gpt-4")
            
            # Capture details about token usage and cost.
            with get_openai_callback() as cb:
                prediction = llm.predict(prompt)
                print(cb) # copy this information in a separate panel/section (possibly in left menu bottom)
            
            # Display the generated questions
            st.write("Generated Questions:")
            if st.session_state["format"] == "plain_text":
                st.write(prediction)
                st.button("Copy to Clipboard", on_click=copy_to_clipboard, args=(prediction,))

            elif st.session_state["format"] == "json_format":
                st.json(prediction)

if __name__ == "__main__":
    main()
