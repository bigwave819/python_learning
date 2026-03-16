# import sqlite3

# connection = sqlite3.connect("data.db")

# connection.execute(
#     "INSERT INTO CUSTOMER (ID, NAME, AGE) VALUES (1, 'Hirwa', 99)"
# )

# all_data = connection.execute("SELECT * FROM CUSTOMER")

# for row in all_data:
#     print(row)

# connection.commit()
# connection.close()

# import requests
# import json

# response = requests.get('https://rwanda-hackthons-connect.onrender.com/events')

# print(response.status_code)
# print(response.text)

# res = json.loads(response.text)

# print(res)

# for data in res:
#     print(data)


import requests 
from bs4 import BeautifulSoup


res = requests.get("https://inzozilabs.vercel.app/")

soup = BeautifulSoup(res.content, 'html.parser')

print(soup.title)