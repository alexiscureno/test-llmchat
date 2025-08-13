import gradio as gr
from load_agent import init_agent

# Ensure the agent is available for the async callback regardless of how the app is launched
agent = init_agent()

async def submit_message(message, chat_history):
    print('Chat history', chat_history)
    try:
        response = await agent.run(message)
        response_message = response.output
        response_message_thinking = response_message.replace('<think>', '').replace('</think>', '')

        chat_history.append({'role': 'user', 'content': message})
        chat_history.append({'role': 'assistant', 'content': response_message_thinking})
        
        return '', chat_history, 'i **Status:** Ready'
    
    except Exception as e:
        error_message =  f'x **Error:** {str(e)}'
        gr.Markdown(error_message)
        raise gr.Error(error_message)
    
with gr.Blocks(title='My pydantic AI agent') as app:
    gr.Markdown("<center><h1 style='color: #e72564;'>PydanticAI Agent App</h1></center>")
    
    chatbot = gr.Chatbot(label='Agent run', type='messages')

    input_field = gr.Textbox(show_label=False, placeholder="Enter text and press enter")

    clear = gr.ClearButton([input_field, chatbot])

    status_bar = gr.Markdown('i **Status:** Ready', elem_id='status-bar')

    input_field.submit(
        fn=submit_message,
        inputs=[input_field, chatbot],
        outputs=[input_field, chatbot, status_bar]
    )

if __name__ == '__main__':
    agent = init_agent()

    app.launch()