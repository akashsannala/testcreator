# Test Creator

This project provides functionality to generate questions based on text and analyze images using Google's Gemini 2.0 Flash model.


WHY Google's Gemini 2.0 Flash model??

💬 Real-Time Applications :
⚡ Ideal for chatbots, AI assistants, and interactive tools that require fast responses.

📊 High-Volume Tasks :
📑 Great for bulk text processing, data extraction, and content filtering, ensuring efficiency at scale.

✍️ Summarization :
📄 Quickly summarizes documents, articles, and meetings, saving time while keeping key insights.

💻 Code Assistance :
🔧 Assists with fast debugging, code completion, and code generation for developers.

🖼️ Multimodal Processing :
📸 Efficient at handling text, images, and structured data for AI-powered workflows.

⏳ Low-Latency Needs :
📱 Optimized for mobile, edge computing, and real-time systems where speed is crucial.

------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------



## Prerequisites
------------------------------------------------------------------------------------------------------------------------------------------

- Python 3.6 or higher
- `pip` package manager
- `.env` file with the following environment variable:
    GOOGLE_API_KEY=your_google_api_key_here

------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------ 


## Installation

1. Clone the repository:
  ```
  git clone https://github.com/akashsannala/testcreator.git
  cd testcreator
  ```

2. Install the required packages:
  ```
  pip install -r requirements.txt

  ```


------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------



# Function Documentation

## **Functions**

### `text_to_question(text)`
Generates questions from the given input text.

#### **Parameters**:
- `text` (*str*): The input text to generate questions from.

#### **Raises**:
- `ValueError`: If the `GOOGLE_API_KEY` is not found in the environment variables.

------------------------------------------------------------------------------------------------------------------------------------------

### `analyze_image(image_path)`
Analyzes an image and returns its description.

#### **Parameters**:
- `image_path` (*str*): The path to the image file to be analyzed.

#### **Returns**:
- (*str*): The description of the image.

#### **Raises**:
- `ValueError`: If the `GOOGLE_API_KEY` is not found in the environment variables.


------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------

## 🧠 Models Used in This Application  

### 🔍 **Image Analysis with OpenAI & Gemini (Beta)**  
Currently using the **beta version of OpenAI integrated with Gemini** in the `analyze_image` function.  

### ✨ **Text Processing with Gemini 2.0 Flash**  
The `text_to_question` function leverages **Google's Gemini 2.0 Flash model** for efficient question generation.  



------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------


##📊 Model Performance & Analysis Capacity

🔢 Current Model Stats

Requests per Minute (RPM): 15

Requests per Day (RPD): 1,000,000

Tokens per Minute (TPM): 1,500

------------------------------------------------------------------------------------------------------------------------------------------
📄 Token Consumption Estimate (Based on CAPTURE.JPG)

Image Processing: 516 tokens

Extracted Text Processing: 662 tokens

Total Estimated Tokens per Page: ~1,178 tokens

------------------------------------------------------------------------------------------------------------------------------------------
📚 Daily Processing Capacity

Maximum Pages Processed per Day: ~666 pages

Equivalent to:
✅ Xth Class SSC Mathematics Textbook 📖 + Physics Textbook ⚛️


------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------

##🚀 Beta Features:


✅ FastAPI/Flask Integration – Seamlessly integrates with FastAPI or Flask for efficient API development.

✅ Customizable Input – Supports flexible input handling for both text and image-based AI processing.

✅ Real-time Streaming – Enables text streaming for a smoother user experience.



------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------

##🚀 Future Scope & Limitations 


🎯 Future Enhancements

✅ Performance Optimization – Reduce latency and improve response times by optimizing API calls.

✅ Structured Model with LangChain – Utilize LangChain to create a more modular and organized workflow.

✅ Customizable Input Options – Allow users to upload images and provide custom prompts for expected test sheet generation.

✅ Efficient Processing with Embeddings – Instead of passing raw text, integrate text embeddings in text_to_question for improved accuracy and performance.

✅ Modular Model Architecture – Break down processes into smaller components to enhance efficiency and scalability.


⚠️ Limitations

📌 Token Consumption – High token usage for image-to-text conversion may require optimization.

📌 API Rate Limits – Processing speed is restricted by API constraints (TPM & RPM).

📌 Dependency on External APIs – Performance may vary based on OpenAI and Gemini API updates.








