import os
from dotenv import load_dotenv
from google import genai
from openai import OpenAI
import base64

# Load environment variables from .env file
load_dotenv()

def text_to_question(text):
    """Generate a question based on the given text using Gemini 2.0 Flash."""
    
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError("API key not found. Make sure you have set GOOGLE_API_KEY in your .env file.")
    
    # Initialize the Google AI client
    client = genai.Client(api_key=api_key)

    # Generate a question from the input text
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Make 5 question using this text: {text}",
    )

    # Remove the unwanted phrase from the generated question
    question = response.text.replace("Based on the image description, ", "")

    # Print the generated question
    print(question)

def analyze_image(image_path):
    """Encodes an image and sends it to Google's Gemini model for analysis."""
    
    # Retrieve API key from environment variables
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError("API key not found. Make sure you have set GOOGLE_API_KEY in your .env file.")
    
    # Initialize the OpenAI client with Google's API endpoint
    client = OpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Get the base64-encoded image
    base64_image = encode_image(image_path)

    # Generate a response from Gemini 2.0 Flash
    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What is in this image?"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                ],
            }
        ],
    )

    return response.choices[0]









if __name__ == "__main__":
    # Analyze the image and get the description
    image_description = analyze_image("sources\Capture.JPG")

    # Generate a question based on the image description
    text_to_question(image_description)
