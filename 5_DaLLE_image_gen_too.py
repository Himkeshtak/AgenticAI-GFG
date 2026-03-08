import os
from crewai_tools import DallETool

os.environ['OPENAI_API_KEY'] = ""

dalle_tool = DallETool()

image_url = dalle_tool.run(image_description = 'imagine and gove futuristic car of 2050')
print(image_url)