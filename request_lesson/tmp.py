import requests

req = requests.get("http://127.0.0.1:5000/template")
p = requests.post("http://127.0.0.1:5000/data", json={'df': 'fdf'})



if __name__ == '__main__':
    print(p.headers)