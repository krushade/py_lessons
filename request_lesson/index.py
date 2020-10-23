import requests
# prox = {"http": "localhost:8080", "https": "localhost:8080"}
# # requests.get("https://catalog.onliner.by/mobile", proxies=prox)
# requests.get("https://yandex.ru", proxies=prox, verify=False)
onliner = "https://catalog.onliner.by/mobile"
# image = "https://content2.onliner.by/catalog/device/header/c8ab72a41f2fd9b9b1473d871ed47d76.jpeg"
# image_2 = "https://content2.onliner.by/catalog/device/main/a1b62c65cacfc91ad39e6f92ef15dc63.jpeg"
# image_3 = "http://img.crazys.info/files/i/2012.4.26/1335431474_250653-1920x1200.jpg"
r = requests.get(onliner)
with open("file.html", "wb") as file:
    file.write(r.content)

# req = requests.get(image_2)
# with open("phone.jpg", "wb") as file:
#     file.write(req.content)
#
# req = requests.get(image_3, stream=True)
# with open("image.jpg", "wb") as file:
#     for chunk in req.iter_content(chunk_size=1024):
#         print("Chunk")
#         file.write(chunk)
