import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

from crewai import Agent, Task, Crew

#2. Defining Agents
# Configure DeepSeek LLM
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

deepseek_llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=deepseek_api_key,
    base_url="https://api.deepseek.com/v1"
)

party_planner = Agent(
    role="Party Planner",
    goal="Create the party plan, including the theme, timeline, and guest list.",
    backstory=(
        "You organize the vision for the party, create a timeline, and ensure all aspects are planned. "
        "You send out invitations and coordinate with the other agents."
    ),
    allow_delegation=False,
    verbose=True,
    llm=deepseek_llm
)

food_beverage_coordinator = Agent(
    role="Food & Beverage Coordinator",
    goal="Organize the food and drinks for the party, ensuring there’s enough variety for all guests.",
    backstory=(
        "You handle the food and drink preparations, whether it’s cooking, ordering, or working with caterers. "
        "You make sure guests have plenty to eat and drink throughout the event."
    ),
    allow_delegation=False,
    verbose=True,
    llm=deepseek_llm
)

decorator = Agent(
    role="Decorator",
    goal="Make the party venue look great, fitting the theme and making it fun for guests.",
    backstory=(
        "You decorate the venue to match the theme and create a welcoming and festive environment. "
        "You ensure the venue is ready when the guests arrive."
    ),
    allow_delegation=False,
    verbose=True,
    llm=deepseek_llm
)

entertainment_guest_relations = Agent(
    role="Entertainment & Guest Relations Coordinator",
    goal="Organize entertainment, games, and manage guest interactions to ensure a fun party.",
    backstory=(
        "You make sure the guests have fun, whether it’s through music, games, or other activities. "
        "You also help guests with seating and ensure the event flows smoothly."
    ),
    allow_delegation=False,
    verbose=True,
    llm=deepseek_llm
)

#3. Assigning Tasks
party_plan_task = Task(
    description="Create a party plan including theme, timeline, and guest list.",
    expected_output="Complete party plan with theme, timeline, and invitations.",
    agent=party_planner
)

food_task = Task(
    description="Organize food and drinks menu and set up food stations.",
    expected_output="Food and drinks ready for the party.",
    agent=food_beverage_coordinator
)

decor_task = Task(
    description="Decorate the venue according to the theme.",
    expected_output="Venue decorated and ready for guests.",
    agent=decorator
)

entertainment_task = Task(
    description="Organize music, games, and manage guest interactions.",
    expected_output="A fun and engaging atmosphere with happy guests.",
    agent=entertainment_guest_relations
)

#4. Creating and Managing a Crew
party_crew = Crew(agents=[party_planner, food_beverage_coordinator, decorator, entertainment_guest_relations], 
                  tasks=[party_plan_task, food_task, decor_task, entertainment_task], verbose=True)

#5. Executing the Workflow

party_result = party_crew.kickoff(inputs={})