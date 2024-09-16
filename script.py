import requests

def fetch_data(option):
  url = f"https://swapi.mimo.dev/api/{option}/"
  try:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
  except Exception as e:
    print(f"An error occurred: {e}")
    return None

option = input("What StarWars data will you like to explore:").strip().lower()
data = fetch_data(option)

if data:
  for entity in data:
    print(entity.get("name", "No Name Found"))
else:
  print("Unable to download data")