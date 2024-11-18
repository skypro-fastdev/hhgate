import requests

url = "/artifacts"

data = {
    'field1': 'value1',
    'field2': 'value2',
}


files = {
    'file1': ('filename1.txt', open('filename1.txt', 'rb')),
    'file2': ('filename2.jpg', open('filename2.jpg', 'rb'))
}

response = requests.post(url, data=data, files=files)
