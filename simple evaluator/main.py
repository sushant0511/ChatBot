import os
import base64
from dotenv import load_dotenv
from openai import OpenAI
import logging

# Import the logger from the main module
logger = logging.getLogger(__name__)

load_dotenv("../.env")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


# def convert_to_base_64(file_url: str):
#     try:
#         with open(file_url, "rb") as image_file:
#             encoded_string = base64.b64encode(image_file.read())
#         logging.info(f"Converted image to base64")
#         return f"data:image/jpeg;base64,{encoded_string}"
#     except Exception as e:
#         logging.error(f"An error occurred while converting to base64: {str(e)}", exc_info=e)
#         return None

openai_messages = [
    {
        'role': 'system',
        'content': 'You are a Deep Learning Professor. You are assessing the technical aptitude of your students.'
                   'Ask a very basic technical question to the user on topic of Large Language Models and '
                   'Prompt Engineering.'
                   'Grade the response of the student out of 10 with proper reasoning, and be lenient in marking '
                   'You have to ask a total of 10 questions turn by turn.'
                   'You give no marks for wrong and no answer.'

    },
    # {
    #     'role': 'user',
    #     "content": [{"type": "text", "text": "Grade the following assignment."},
    #                 {"type": "image_url",
    #                  "image_url": {"url": convert_to_base_64(file_url="")}}]
    # }
    # {
    #     'role': 'user',
    #     'content': "Question: How does transfer learning improve the performance of large language models like GPT-3?"
    #                "Answer: Transfer learning enhances the performance of large language models by leveraging knowledge "
    #                "from pre-trained models to adapt to specific tasks or domains with limited task-specific data. "
    #                "In the case of GPT-3, transfer learning involves fine-tuning the pre-trained model on task-specific data, "
    #                "enabling it to learn task-specific patterns and nuances. This process involves adjusting the model's parameters "
    #                "through continued training on the task-specific dataset while retaining the knowledge acquired during pre-training."
    #                " By initializing the model with general linguistic knowledge and then fine-tuning it on task-specific data, "
    #                "transfer learning allows for efficient utilization of computational resources and enables the model to "
    #                "achieve superior performance on various tasks compared to training from scratch. Additionally, "
    #                "transfer learning facilitates rapid deployment of models for new applications and domains, as it "
    #                "reduces the need for extensive labeled data and computational resources, making it a crucial technique "
    #                "in the development of large language models."
    # }
]

while input != "quit()":
    response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=openai_messages,
            max_tokens=300,
            temperature=0.5,
    )
    openai_messages.append({
        "content": response.choices[0].message.content,
        "role": "assistant"
    })
    user_response = input(f"Sharda University : {response.choices[0].message.content}\nTokens: {response.usage.total_tokens}\n\n")
    openai_messages.append({
        "content": user_response,
        "role": "user"
    })



# Demo:
# Asking and Grading questions with 0 shot learning. Right now. Tuesday.


# Pen and Paper Examination Grading:
# Input Images - 3 image with same questions and diff answers. Grade each image separately. Second Step.
# Extract the roll number and evaluate answers for each roll number. Second Step.

# Automated LLM Based MCQs (Knowledge Testing):
# Asking and Grading questions with RAG. Third Step. MCQs


