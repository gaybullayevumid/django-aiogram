import requests

BASE_URL = 'http://127.0.0.1:8000/api/v1'

def create_user(username, name, user_id):
    url = f"{BASE_URL}/bot-users/"
    response = requests.get(url=url).text
    print(response)

create_user("Umid", "G'aybullayev", "438754388")
