import requests
import json



full_data = []
for page in range(1,32):
    url = "https://api.dane.gov.pl/resources/17363/data?page=" + str(page)
    response = requests.get(url)
    data = json.loads(response.text)
    data_2 = data["data"]
    for i in data_2:
        full_data_appended = full_data.append(i["attributes"])


for row in full_data:
    if row["col1"] == "Polska":
        print(row["col2"])


