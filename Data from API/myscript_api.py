import requests
import json

data = []
for page in range(1,32):
    url = "https://api.dane.gov.pl/resources/17363/data?page=" + str(page)
    response = requests.get(url)
    load_data = json.loads(response.text)
    load_data_2 = load_data["data"]
    for i in load_data_2:
        full_data_appended = data.append(i["attributes"])

for row in data:
    print(row)
