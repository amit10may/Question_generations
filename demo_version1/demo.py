import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate

# Define the options for question types and Bloom's taxonomy levels
question_types = ['MCQs', 'Fill in the Blanks', 'True/False']
blooms_taxonomy_levels = ['Remembering', 'Understanding', 'Applying', 'Analyzing', 'Evaluating', 'Creating']

# Prompt template for generating questions
prompt_template = """
As an experienced college professor, you're tasked with creating test MCQS types questions based on the {content} provided. Your aim is to craft questions that assess students' understanding and application of the content while considering the {learning_objectives} and {keywords}. Each question should focus on a single concept and be written in the singular tense. Provide four options for each question, ensuring a mix of one-word choices and complete sentences or phrases, while shuffling the correct answer among relevant distractors to foster critical thinking. Aim for a balanced level of challenge and solvability, avoiding questions that are overly simplistic or excessively difficult. Utilize various question types, such as recall, comprehension, application, analysis, and evaluation, to assess different facets of student knowledge <>. Enhance engagement by offering concrete examples or scenarios for each question, facilitating connections to real-world situations. Ensure questions are meticulously proofread and edited for clarity, conciseness, and grammatical accuracy. Include a combination of short and longer questions to accommodate varying levels of depth and complexity. Refrain from utilizing specific option types like "All of the above," "None of the above," or "Both A and B," while ensuring options remain discernible yet require critical thinking to distinguish the correct choices from distractors. Count of the generating questions can vary according to the length of the content but quality should not be degraded and generate minimum 10 questions at least.


Please respond to each question in the following format:

For MCQs : 
Question with its respective options:

Option A ,
Option B ,
Option C , 
Option D ,

Correct answer: ,

Blooms Taxonomy Level: ,

Learning Objective : ,

Keyword_used : 
"""
# and skills by following the {blooms_taxonomy_level}

# Load the prompt template
prompt = PromptTemplate.from_template(template=prompt_template)

# Streamlit UI
st.title('Question Generator')

content = st.text_area('Enter the content here:', height=200)
learning_objectives = st.text_area('Enter learning objectives here:', height=100)
keywords = st.text_area('Enter keywords here:', height=100)

question_type = st.selectbox('Select the type of question:', question_types)
# blooms_taxonomy_level = st.selectbox('Select Bloom\'s Taxonomy Level:', blooms_taxonomy_levels)

# Create a button to generate the question
if st.button('Generate Question'):
    # Format the prompt with user inputs
    prompt_formatted_str = prompt.format(type=question_types, content=content,learning_objectives=learning_objectives,keywords=keywords)

    # Initialize OpenAI model
    llm = OpenAI(temperature=0, model_name="gpt-4")

    # Generate question
    prediction = llm.predict(prompt_formatted_str)
    
    # Display the generated question
    st.write(prediction)
