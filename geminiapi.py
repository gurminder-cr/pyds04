api_key="Add key here...."
#pip install google-genai

from google import genai

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Explain how AI works"
)

print(response.text)



