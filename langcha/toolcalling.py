from langchain_ollama import ChatOllama
from langchain_core.tools import tool 
from langchain_core.messages import HumanMessage,SystemMessage 
import requests 

WEATHER_API_KEY=""
# weather, currency calculator 

# weather tool
@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""  # doc string 
    # The docstring is important because the LLM uses it to understand when to call the tool.

    try:
        url = "http://api.weatherapi.com/v1/current.json"

        params = {
            "key": WEATHER_API_KEY,
            "q": city
        }

        response = requests.get(url, params=params)
        data = response.json()

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        return (
            f"Weather in {city}: "
            f"{temp}°C, {condition}"
        )

    except Exception as e:
        return f"Weather lookup failed: {str(e)}"

# currency convertor
@tool
def currency_converter(query: str) -> str:
    """
    Convert currency.
    Example:
    '100 USD to INR'
    """
    try:
        parts = query.upper().split()  # [100, USD, TO, INR]

        amount = float(parts[0])
        from_currency = parts[1]
        to_currency = parts[3]

        url = f"https://open.er-api.com/v6/latest/{from_currency}"

        response = requests.get(url)
        data = response.json()

        rate = data["rates"][to_currency]

        converted = amount * rate

        print(
            f"{amount} {from_currency} = "
            f"{converted:.2f} {to_currency}"
        )
        return (
            f"{amount} {from_currency} = "
            f"{converted:.2f} {to_currency}"
        )

    except Exception as e:
        return f"Conversion failed: {str(e)}"
    
# register tools 
tools = [
    get_weather,
    currency_converter
]

llm= ChatOllama(model='llama3.2:1b')
llm_with_tools = llm.bind_tools(tools)

# creating a agent loop 
def run_assistant(user_query):
    response= llm_with_tools.invoke(
        [HumanMessage(content=user_query)]
    )
    
    # check if model selected a tool
    if response.tool_calls:
        tool_call= response.tool_calls[0]
        # {
        # "name": "get_weather",
        # "args": {
        #     "city": "Delhi"
        # }}
        
        tool_name= tool_call['name']
        tool_args= tool_call['args']

        selected_tool = next(
            tool for tool in tools
            if tool.name==tool_name
            )
        # get_weather
        
        result= selected_tool.invoke(tool_args)
        print(f"Result","\n{result}")
        return result
    else:
        print(response.content)
        return response.content

while True:
    user_input= input("\nYou: ")
    if user_input.lower=="exit":
        break
    run_assistant(user_input)
    