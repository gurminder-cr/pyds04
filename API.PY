# https://jsonplaceholder.typicode.com/posts/1 
# https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric
# token = "your_access_token_here"

# headers = {
#     "Authorization": f"Bearer {token}",
#     "Content-Type": "application/json"
# }



# pip install requests
import requests  


# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# ans=response.json()
# print(ans)
# print(ans['title'])
# print(ans['body'])


# https://home.openweathermap.org/api_keys  to get api key
city='chandigarh'


API_KEY="add your key heree..."

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
print(response.json())

city= requests.get("http://api.openweathermap.org/geo/1.0/direct?q=chandigarh&limit=5&appid=ed8a245443aa3cd109ac012f1fe3643e")
lat_long=city.json()

# print(lat_long)
# # latitude=lat_long[1]['lat']
# longitude=lat_long[1]['lon']
# print(latitude)
# print(longitude)

result=requests.get(f'https://api.openweathermap.org/data/4.0/onecall/current?lat=52.2297&lon=21.0122&units=metric&lang=en&appid={API_KEY} ')

# print("-------------")
print(result.json())