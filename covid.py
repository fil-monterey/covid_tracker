import requests

url = "https://coronavirus-tracker-api.herokuapp.com/all"
country = input("Please enter the country you want to search: ")
api = requests.get(
    url,
    headers={"Accept": "application/json"}
).json()
confirmed_cases = api["latest"]["confirmed"]
deaths = api["latest"]["deaths"]
print(f"Total number of deaths globally: {deaths}")
for i in (api["confirmed"]["locations"]):
    if (i["country"] == country):
        print(f'{country} has {i["latest"]} recent cases.')
confirmed_all = api["confirmed"]["locations"][0]
