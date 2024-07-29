import gradio as gr
from gradio import ChatMessage
from src.agent_streaming import stream_from_transformers_agent
from src.Agent import get_agent
from config import load_config

config = load_config()
agent = get_agent("HuggingFaceTB/SmolLM-135M-Instruct", config)

def interact_with_agent(prompt, messages):
    messages.append(ChatMessage(role="user", content=prompt))
    yield messages
    for msg in stream_from_transformers_agent(agent, prompt):
        messages.append(msg)
        yield messages
    yield messages

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            chatbot_one_state = gr.State([])
            chatbot = gr.Chatbot(
                label="Agent",
                type="messages",
                )
            
            text_input = gr.Textbox(lines=1, label="Let me solve your math problems:")
            text_input.submit(lambda s: (s, ""), [text_input], [chatbot_one_state, text_input]).then(interact_with_agent, [chatbot_one_state, chatbot], [chatbot])


if __name__ == "__main__":
    demo.launch(share=False)