import openai
import re
from gradio.components import Textbox
from gradio import Interface

# Set up OpenAI API credentials
openai.api_key = "****************************************************"
questions = [
    [
        "History of {} programming language",
        "What is {} programming language?",
        "What are the features of {} programming language?",
    ],
    "PreRequisites for {} programming language?",
    "Requirements for {} programming language?",
    "Installations for {} programming language?",
    "What are the advantages of {} programming language?",
    "What are the applications of {} programming language? (with examples like frameworks, libraries, etc.)",
    "What are the concepts to learn {} programming language?",
    "What are the resources to learn {} programming language? (like courses, video, blogs, etc. links)",
]

infoQuestions = [
    "About {}: ",
    "PreRequisites for {}: ",
    "Requirements for {}: ",
    "Installations for {} programming language?",
    "Advantages of {}: ",
    "Applications of {}: ",
    "Concepts to learn {}: ",
    "Resources to learn {}: ",
]

conversation_history = []

def generate_chatbot_response(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=200,  # Increase the max_tokens value to get a longer response
        temperature=0.7,
        top_p=1.0,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def chat_with_programming_language_bot(language):
    if language:
        language = language.lower()
        question = "Is {} a programming language? Reply True or False"
        if bool(generate_chatbot_response(question.format(language))):
            responses = []
            for question in questions:
                if type(question) == list:
                    info_responses = []
                    for q in question:
                        res = re.sub(r"\n", "\n", generate_chatbot_response(q.format(language)))
                        info_responses.append(res)
                    responses.append(info_responses)
                else:
                    res = re.sub(r"\n", "\n", generate_chatbot_response(question.format(language)))
                    responses.append(res)
            conversation_history.append((language, responses))
            return responses
        else:
            rs = re.sub(r"\n", "\n", generate_chatbot_response(f"What is {language}?"))
            conversation_history.append((language, rs))
            return rs
    else:
        return "Please enter the name of a programming language."

# Create a Gradio Component
inputs = Textbox(lines=4, label="Chat with AI")
outputs = Textbox(lines=20, label="Reply")  # Use Textbox to display plain text responses

# Create a Gradio interface
chat_interface = Interface(
    fn=chat_with_programming_language_bot,
    inputs=inputs, 
    outputs=outputs, 
    title=" Chatbot",
    description=" programming language.",
    theme="dark"
)

chat_interface.queue()
chat_interface.launch(inline=True, share=True)
chat_interface.launch(inline=True, share=True, debug=True)
