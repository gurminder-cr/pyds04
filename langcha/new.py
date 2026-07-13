import os
import requests
from dotenv import load_dotenv

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.memory import ConversationBufferMemory
from langchain_ollama import ChatOllama

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


# -----------------------
# Weather Tool
# -----------------------
@tool
def get_weather(city: str) -> str:
    """Get the current weather of a city."""

    if not WEATHER_API_KEY:
        return "Weather API Key not found."

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            return "Unable to fetch weather."

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]

        return f"{city}: {weather}, {temp}°C"

    except Exception as e:
        return str(e)


# -----------------------
# Budget Tool
# -----------------------
@tool
def estimate_budget(days: int, budget: int) -> str:
    """
    Estimate travel expenses.
    """

    hotel = budget * 0.4
    food = budget * 0.25
    transport = budget * 0.2
    activities = budget * 0.15

    return f"""
Travel Duration : {days} Days

Hotel : ₹{hotel:.0f}
Food : ₹{food:.0f}
Transport : ₹{transport:.0f}
Activities : ₹{activities:.0f}
"""


# -----------------------
# LLM
# -----------------------

llm = ChatOllama(
    model='llama3.2:1b',
    temperature=0.5
)

tools = [get_weather, estimate_budget]

llm_with_tools = llm.bind_tools(tools)


# -----------------------
# Prompt
# -----------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Travel Planner.

Your responsibilities:

1. Plan trips.
2. Suggest hotels.
3. Suggest tourist attractions.
4. Recommend food.
5. Suggest packing tips.
6. Use weather tool whenever weather is required.
7. Use budget tool whenever budget estimation is required.

Always provide a day-wise itinerary.
"""
        ),

        MessagesPlaceholder(variable_name="history"),

        ("human", "{input}")
    ]
)


memory = ConversationBufferMemory(return_messages=True)


print("=" * 60)
print("🌍 AI Travel Planner")
print("Type exit to quit.")
print("=" * 60)

while True:

    user = input("\nYou : ")

    if user.lower() == "exit":
        break

    history = memory.load_memory_variables({})["history"]

    chain = prompt | llm_with_tools

    response = chain.invoke(
        {
            "input": user,
            "history": history
        }
    )

    # Tool Calling
    if response.tool_calls:

        tool_outputs = []

        for tool_call in response.tool_calls:

            name = tool_call["name"]
            args = tool_call["args"]

            if name == "get_weather":
                result = get_weather.invoke(args)

            elif name == "estimate_budget":
                result = estimate_budget.invoke(args)

            else:
                result = "Unknown tool."

            tool_outputs.append(result)

        final_prompt = f"""
User Question:
{user}

Tool Results:
{tool_outputs}

Generate the final travel response.
"""

        final = llm.invoke(final_prompt)

        print("\nAI :", final.content)

        memory.save_context(
            {"input": user},
            {"output": final.content}
        )

    else:

        print("\nAI :", response.content)

        memory.save_context(
            {"input": user},
            {"output": response.content}
        )