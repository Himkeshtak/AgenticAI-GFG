import os
from crewai_tools import FileReadTool
hf_config = {
    "provider": "huggingface",
    "config": {
        "api_url": "https://api-inference.huggingface.co", # Example model URL
        "token": "YOUR_HF_TOKEN" # Can also be read from HF_TOKEN env var
    }
}
os.environ['OPENAI_API_KEY'] = ""

file_reader = FileReadTool(file_path="content/text.txt")

print(file_reader)

