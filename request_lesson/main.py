import requests
headers = {
    "User-Agent": "Alex"
}
# response = requests.get("https://catalog.onliner.by/mobile/get")
response = requests.post("https://httpbin.org/post",
                         headers=headers,
                         params={'a': 'd'},
                         json={'username': 'kroot'})
# if response.status_code == 200:
#     print("OK!")
#
if response.ok:
    print("OK!")
#
# response.raise_for_status()

print(response.text)
# print(response.json()['headers'])
