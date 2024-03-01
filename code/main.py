from langchain.llms import OpenAI
from jinja2 import Template
from code.prompt_template import PROMPT_TEMPLATE

class QaInput:
    @staticmethod
    def get_user_input():
        content = input("\nEnter the content: \n")
        keywords = input("\nEnter keywords (separated by commas): \n")
        learning_objective = input("Enter the learning objective: \n\n")
        ques_type = input("\nEnter the type of the questions: \n")
        bloom_level = input("\nEnter the Bloom's taxonomy level: \n")
        return learning_objective, content, keywords, ques_type, bloom_level

class Qa_Gen_Params:
    def __init__(self, learning_objective, content, keywords, ques_type, bloom_level):
        self.learning_objective = learning_objective
        self.content = content
        self.keywords = keywords
        self.ques_type = ques_type
        self.bloom_level = bloom_level

    def construct_prompt(self):
        template = Template(PROMPT_TEMPLATE)
        return template.render(type=self.ques_type, content=self.content, level=self.bloom_level, learning_objective=self.learning_objective, Keywords=self.keywords)

# Get user input
learning_objective, content, keywords, ques_type, bloom_level = QaInput.get_user_input()

# Create an instance of Qa_Gen_Params
params = Qa_Gen_Params(learning_objective, content, keywords, ques_type, bloom_level)

# Generate prompt using Qa_Gen_Params
prompt = params.construct_prompt()

# Initialize OpenAI model
llm = OpenAI(temperature=0, model_name="gpt-4")

prediction = llm.predict(prompt)

print(prediction)
