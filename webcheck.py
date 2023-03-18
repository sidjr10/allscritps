import requests
producturl="https://www.google.com/"

res = requests.get(producturl, timeout=5)
print(res)
