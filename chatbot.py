import openai
import requests
import gradio as gr
openai.api_key = 'nv2-uJsdUSG01wRCUGpn9VyO_NOVA_v2_WzILCU3y6C8OoGpR91O7'

URL = "https://api.nova-oss.com/v1/chat/completions"

def reply(message,temp):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}],
        "temperature": temp,
        "top_p": 1.0,
        "n": 1,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }

    response = requests.post(URL, headers=headers, json=payload, stream=False)

    return response.json()["choices"][0]["message"]["content"]

# while True:
#     call_reply = str(input("User: "))
#     response = reply(call_reply)
#     print("AI:", response)
# demo= gr.Interface(fn=reply,inputs = ["text",gr.inputs.Number("temperature")],outputs = "text",title = "ai in education")
demo = gr.Interface(fn=reply, inputs=["text", gr.inputs.Slider(0, 1, label = "temp")],outputs="text", title="AI")
demo.launch()
