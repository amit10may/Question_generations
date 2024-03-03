import streamlit as st
from langchain.llms import OpenAI
from jinja2 import Template
from prompt_template import PROMPT_TEMPLATE

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

def main():
    st.title("Question Generation Tool")

    # Get user input
    content = st.text_area("Enter the content:", height=200)
    learning_objective = st.text_area("Enter the learning objective:", height=100)
    keywords = st.text_area("Enter keywords (separated by commas):", height=100)
    bloom_level = st.selectbox("Select the Bloom's taxonomy level:" , ("Remember", "Understand","Apply","Analyze","Evaluate","Create"))
    
    plain_text_checkbox = st.checkbox("Plain Text Format")
    json_checkbox = st.checkbox("JSON Format")

    if plain_text_checkbox:
        st.session_state["format"] = "plain_text"
    if  json_checkbox:
        st.session_state["format"] = "json_format"

    
    ques_type = st.selectbox("Select the type of the questions:",("Multiple Type Questions","Fill In The Blanks" , "True False"))
    # ques_type = st.text_input("Enter the type of the questions:")

    if st.button("Generate Questions"):
        # Create an instance of Qa_Gen_Params
        params = Qa_Gen_Params(learning_objective, content, keywords, ques_type, bloom_level)

        # Generate prompt using Qa_Gen_Params
        prompt = params.construct_prompt()

        # Initialize OpenAI model
        llm = OpenAI(temperature=0, model_name="gpt-4")

        prediction = llm.predict(prompt)

        # Display the generated questions
        st.write("Generated Questions:")
        st.write(prediction)

if __name__ == "__main__":
    main()
