import os
os.environ["OPENAI_API_KEY"] = ""

from crewai_tools import RagTool

rag_tool = RagTool(
    
    name = 'Knowledge base',
    description = 'A knowledge abse which can be used ot answer the question',
    summarize= True,
    result_as_answer = True,
    verbose = True
)

response = rag_tool.run("Who is the vice president of India")
print(response)