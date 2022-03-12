import requests
import datetime

def call_zodiac_api(sign: str):
  url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
  headers = {
            'x-rapidapi-host': "sameer-kumar-aztro-v1.p.rapidapi.com",
            'x-rapidapi-key':
            "582dbb69d4mshb9f9d4742ad7993p1702d9jsn2a5a5999c7db"
        }
  querystring = {"sign":sign,"day":"today"}
  day = datetime.datetime.now()
  day = day.strftime("%A")
  response = requests.request("POST", url, headers=headers, params=querystring)
  return response