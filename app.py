import gradio as gr
from transformers import stream_to_gradio

from src.Agent import get_agent
from config import load_config

config = load_config()
agent = get_agent(config=config)

def interact_with_agent(task):
    messages = []
    messages.append(gr.ChatMessage(role="user", content=task))
    yield messages
    for msg in stream_to_gradio(agent, task):
        messages.append(msg)
        yield messages + [
            gr.ChatMessage(role="assistant", content="⏳ Task not finished yet!")
        ]
    yield messages

with gr.Blocks() as demo:
    text_input = gr.Textbox(lines=1, label="Chat Message", value="(1 + 2) / 12")
    submit = gr.Button("Solve")
    chatbot = gr.Chatbot(
        label="Agent",
        type="messages",
        avatar_images=(
            None,
            "https://em-content.zobj.net/source/twitter/53/robot-face_1f916.png",
        ),
    )
    submit.click(interact_with_agent, [text_input], [chatbot])

if __name__ == "__main__":
    demo.launch()