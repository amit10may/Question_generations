# prompt_template.py
PROMPT_TEMPLATE = """
As an esteemed college professor tasked with crafting {{ type }} questions based on the {{ content }} provided, your objective is to design questions that align properly with the given {{learning_objective}} and {{Keywords}}, evaluating students' understanding and application of the content. Each question should focus on a single concept and be written in the singular tense, with correct answers not exposed within the questions generated. Ensure that correct answers are the best possible answers, while distractors should be plausible alternatives of similar complexity, detail, and length. Aim for a balanced level of challenge and solvability, avoiding questions that are overly simplistic or excessively difficult. Design questions based on Bloom's Taxonomy level {{ level }} to assess different aspects of student learning. Enhance student engagement by providing concrete examples or scenarios within the questions, facilitating connections to real-world contexts. Ensure meticulous proofreading and editing for clarity, conciseness, and grammatical accuracy. Aim to generate a minimum of 10 questions, adjusting the count based on the length and complexity of the content, while maintaining high-quality standards.


Please respond to each question in the following {{format}}:
{% if format == "json_format" %}
    {% if type == "Multiple Type Questions" %}
    [{
      "question_id": "<number>",
      "type": "Multiple Choice Question",
      "stem": "<main body of the question>",
      "options": {
        "a": "Option1",
        "b": "Option2",
        "c": "Option3",
        "d": "Option4"
      },
      "rationale": "if Correct why?, if incorrect why?",
      "correct_option": "<correct_option>",
      "blooms_taxonomy_level": "<level of blooms taxonomy>",
      "difficulty_level": "<High/Medium/Low>",
      "student_level": "<Elementary/High School/College/University>"
    }]
    {% elif type == "Fill In The Blanks" %}
    [{
      "question_id": "<number>",
      "type": "Fill in the Blanks",
      "stem": "<main body of the question>",
      "options": {
        "a": "_____",
        "b": "_____",
        "c": "_____",
        "d": "_____"
      },
      "rationale": "if Correct why?, if incorrect why?",
      "correct_option": "<correct_option>",
      "blooms_taxonomy_level": "<level of blooms taxonomy>",
      "difficulty_level": "<High/Medium/Low>",
      "student_level": "<Elementary/High School/College/University>"
    }]
    {% elif type == "True False" %}
    [{
      "question_id": "<number>",
      "type": "True/False",
      "stem": "<main body of the question>",
      "options": {
        "a": "True",
        "b": "False"
      },
      "rationale": "if Correct why?, if incorrect why?",
      "correct_option": "<correct_option>",
      "blooms_taxonomy_level": "<level of blooms taxonomy>",
      "difficulty_level": "<High/Medium/Low>",
      "student_level": "<Elementary/High School/College/University>"
    }]
    {% endif %}
{% elif format == "plain_text" %}
    {% if type == "Multiple Type Questions" %}
        Question with its respective options:
        Option A
        Option B
        Option C
        Option D
        Correct answer:
        Blooms Taxonomy Level:

    {% elif type == "Fill In The Blanks" %}
        Correct answer: 
        Blooms Taxonomy Level:

    {% elif type == "True False" %}
        Options A: True/False
        Options B: True/False
        Correct answer:
        Blooms Taxonomy Level:

    {% endif %}
{% endif %}


"""
