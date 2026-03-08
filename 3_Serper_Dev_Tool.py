import os
from crewai import SerperDevTool

os.environ['OPENAI_API_KEY'] = ""
os.environ['SERPER_API_KEY'] = ""

serper_tool = SerperDevTool(
    name = "Web search tool",
    description = "It searches best results of web by searching on the search engine",
    summarizer = True,
    verbose = True
)

search_result = serper_tool.run(query = "Where doe the Karan Aujla hosted his latest concert?")
print(search_result)