import base64
from openai import OpenAI
import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

client = OpenAI(
    api_key="AIzaSyBm6Q2jsnQDZxK_cuwgWhxhYR5LVbYqap8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Getting the base64 string
base64_image = encode_image("homeschool-middle-school-science-textbook-2nd-edition-sample-Page_4-min_1200x.jpg")

response = client.chat.completions.create(
  model="gemini-2.0-flash",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url":  f"data:image/jpeg;base64,{base64_image}"
          },
        },
      ],
    }
  ],
)

print(response.choices[0])



def upload_image(image_path):
    """Simulate image upload by returning the path of the uploaded image."""
    # In a real application, you would handle file uploads here
    return image_path

def generate_question_paper(text, image_paths):
    """Generate a dynamic question paper based on text and images."""
    questions = []

    # Generate questions from text
    text_questions = text_to_question(text)
    questions.append(text_questions)

    # Generate questions from images
    for image_path in image_paths:
        image_description = analyze_image(image_path)
        image_questions = text_to_question(image_description)
        questions.append(image_questions)

    return questions


