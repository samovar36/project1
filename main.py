from requests import get, status_codes

r = get ('https://www.google.com')
print(r.status_code)
print('Hello world')
