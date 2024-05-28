import openai
import gradio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv("../.env")

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")


messages = [{"role": "system", "content": "You are a career counselor expert staying in India and you are aware of Indian Education System that specializes Engineering. "}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "career counselor")

demo.launch(share=True)