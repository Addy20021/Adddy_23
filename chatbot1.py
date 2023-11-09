import gradio as gr
import openai
import requests

openai.api_key = 'nv2-uJsdUSG01wRCUGpn9VyO_NOVA_v2_WzILCU3y6C8OoGpR91O7'

URL = "https://api.nova-oss.com/v1/chat/completions"
obt_question = []
c_a = 0
t_a = 0
def reply(message):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}],
        "temperature": 1.0,
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

def initial(m, pos):
    questions = [
        f"What is {m} programming language?",
        f"PreRequisites for {m} programming language?",
        f"Requirements for {m} programming language?",
        f"Installations for {m} programming language?",
        f"What are the advantages of {m} programming language?",
        f"What are the applications of {m} programming language? (with examples like frameworks, libraries, etc.)",
        f"What are the concepts to learn {m} programming language?",
        f"What are the resources to learn {m} programming language? (like courses, video, blogs, etc. links)",
        f"what is {m}?",
    ]
    return reply(questions[pos])

def gen0(n):
    m = n
    return initial(m, 0)

def gen1(n):
    m = n
    return initial(m, 1)

def gen2(n):
    m = n
    return initial(m, 2)

def gen3(n):
    m = n
    return initial(m, 3)

def gen4(n):
    m = n
    return initial(m, 4)

def gen5(n):
    m = n
    return initial(m, 5)

def gen6(n):
    m = n
    return initial(m, 6)

def gen7(n):
    m = n
    return initial(m, 7)

def gen8(n):
    m = n
    return initial(m, 8)

infoQuestions = [
    f"About ",
    f"PreRequisites ",
    f"Requirements ",
    f"Installations ",
    f"Advantages ",
    f"Applications ",
    f"Concepts to learn ",
    f"Resources to learn ",
    f"Submit",  # Add the "Submit" button
]

btn = ["btn" + str(i) for i in range(9)]
generate = [gen0, gen1, gen2, gen3, gen4, gen5, gen6, gen7, gen8]

def quiz_section(topic, level):
  ask = f"Generate new 1 {level} question based on {topic} with 4 option with one right answer "+"generate it in the form of python list with 1st element as question and next 4 elements are option and last element is answer"
  obtained = reply(ask)
  start = obtained.find("[")
  end = obtained.rfind("]")
  global obt_question
  obt_question = eval(obtained[start:end+1])
  bst = str(obt_question[0])+"\n\n"+"1.) "+ str(obt_question[1])+"\t\t"+"2.) "+ str(obt_question[2])+"\t\t"+"3.) "+ str(obt_question[3])+"\t\t"+"4.) "+ str(obt_question[4])
  return bst

def check_ans(pos):
  if obt_question[pos] == obt_question[5]:
    global c_a
    c_a = c_a + 1
    global t_a
    t_a = t_a + 1
    com = f"correct answer....!. you answered {c_a} out of {t_a}"
    return com
  else:
    t_a = t_a + 1
    com = f"wrong answer....!. you answered {c_a} out of {t_a}"
  return com


with gr.Blocks(css=".gradio-container {background: url('file=https://e1.pxfuel.com/desktop-wallpaper/861/840/desktop-wallpaper-gray-map-illustration-world-map.jpg") as demo:
    with gr.Row():
      gr.Markdown(
      """
      # EDUbot
      AI in education.



    """)
    with gr.Tab("CHAT BOT "):
        txt = gr.Textbox(label="Input", lines=2,placeholder="Please enter here : )    (if u have any specific qns in mind plzz use the submit button)")
        txt_3 = gr.Textbox(value="", label="Output", lines=2)
        with gr.Row():
          with gr.Column(scale=4):
              for n in range(4):
                btn[n] = gr.Button(value=infoQuestions[n], size=["sm"])
                btn[n].click(generate[n], inputs=[txt], outputs=[txt_3])
          with gr.Column(scale=4):
              for n in range(5,9):
                btn[n] = gr.Button(value=infoQuestions[n], size=["sm"])
                btn[n].click(generate[n], inputs=[txt], outputs=[txt_3])
    with gr.Tab("QUIZ "):
              with gr.Row():
                topic = gr.Textbox(label="TOPIC", lines=2,placeholder="Please enter the programming language u want to evaluate )")
                level = gr.Dropdown(["easy", "intermediate", "hard"], label="level", info="all the best!")
              sub = gr.Button(value="SUBMIT", size=["sm"])
              result = gr.Textbox(value="", label="questions", lines=5)
              sub.click(quiz_section, inputs=[topic,level],outputs=[result])
              user_choice = gr.Radio([1, 2, 3, 4], label="options", info="pick any one....!")
              comment = gr.Textbox(value="", label="score", lines=2)
              with gr.Row():
                sub_opt = gr.Button(value="evalute", size=["sm"])
                sub_opt.click(check_ans, inputs=[user_choice],outputs=[comment])
                nxt_btn = gr.Button(value="next question", size=["sm"])
                nxt_btn.click(quiz_section, inputs=[topic,level],outputs=[result])




if __name__ == "__main__":
    demo.launch(debug=True)


