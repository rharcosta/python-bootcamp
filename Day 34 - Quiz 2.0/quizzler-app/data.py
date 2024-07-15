import requests

parameters = {
    "amount": 20,
    "type": "boolean"
}
data = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = data.json()["results"]
# print(question_data)
