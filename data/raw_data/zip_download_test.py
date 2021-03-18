url = 'https://www.fantasyfootballdatapros.com/static/files/2019projections.csv'

import requests

r = requests.get(url)

with open("test_zip.zip","wb") as code:
    code.write(r.content)

