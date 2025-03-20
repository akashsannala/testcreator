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







