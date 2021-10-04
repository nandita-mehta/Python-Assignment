import urllib.request
import re


urllib.request.urlretrieve(input("Enter Website:"), 'webpage.html')
f = open("webpage.html", 'r', encoding='utf-8')
file_data = f.read()
text = re.sub('<[^<]+?>', '', file_data)
print(text)
