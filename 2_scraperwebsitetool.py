import os
from crewai_tools import ScrapeWebsiteTool
os.environ['OPENAI_API_KEY'] = ""

scraper = ScrapeWebsiteTool(website_url='https://www.destyn.in/')
response = scraper.run()

print(response)