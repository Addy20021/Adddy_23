import os
import requests
import gradio as gr

PALM_AI_API_KEY = "AIzaSyAMkX00XLrnN9vTz4aL4iqr0GeRziaBrT4"

def palm_ai_create(prompt):
    endpoint = "https://api.palm-ai.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {PALM_AI_API_KEY}"
    }
    data = {
        "text": prompt, 
        "max_length": 150  # Adjust the length as needed
    }

    response = requests.post(endpoint, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("choices")[0].get("text")
    else:
        return "Palm AI API request failed."

def chat_with_palm_ai(input, history):
    history = history or []
    history.append(("Human:", input))
    combined_text = "\n".join([f"{role} {text}" for role, text in history])
    output = palm_ai_create(combined_text)
    return history, output

block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>Build a Chatbot with Palm AI and Gradio</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder="Type your message here...")
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chat_with_palm_ai, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug=True)
