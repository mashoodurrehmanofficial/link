links = [
    'https://www.youtube.com/watch?v=rzPnJ7w54MZFQ?username=ali',
    'https://www.name.com/watch?v=rzPnJ7w54MZFQ?u55ername=ali',
    'https://www.name.com/watch?v=rzPnJ7wMZFQ?u54sername=ali',
    'https://www.name.com/watch?v=rzPnJ7wMZFQ?u54sername=ali',
    'https://www.name.com/watch?v=rzPnJ7wMZFQ?username=ali',
    'https://www.youtube.com/watch?v=rzPnJ7w54MZFQ?username=ali',
    'https://www.youtube.com/watch?v=rzPnJ7wM54ZFQ?username=ali',
    'https://www.youtube.com/watch?v=rzPnJ7wM54ZFQ?username=ali',
    'https://www.alex.com/watch?v=rzPnJ7wMZFQ545?username=ali',
    'https://www.alex.com/watch?v=rzPnJ7wMZFQ545?username=ali',
    'https://www.alex.com/watch?v=rzPnJ7wMZFQ545?username=ali',
    'https://www.alex.com/watch?v=rzPnJ7wMZFQ545?username=ali',
    'https://www.youtube.com/watch?v=rzPnJ7wM45ZFQ?username=ali',
    'https://www.w3eschool.com/watch?v=rzPnJ7wMZ45FQ?username=ali',
    'https://www.w3school.com/watch?v=rzPnJ7wMZ45FQ?username=ali',
    'https://www.w3school.com/watch?v=rzPnJ7wMZ45FQ?username=ali',
    'https://www.w3school.com/watch?v=rzPnJ7wMZ45FQ?username=ali',
    'https://www.w3school.com/watch?v=rzPnJ7wMZ45FQ?username=ali',
    'https://www.stack.com/watch?v=rzPnJ7wMZ45FQ?username=ali',
] 
import urllib.parse 
from urllib import parse
 
# print(urllib.parse.urlsplit('https://www.w3schools.com/bootstrap/bootstrap_ver.asp?username=ali/').query.split('=')[1])
 
# url='https://www.w3schools.com/bootstrap/bootstrap_ver.asp?username=ali/'
# data = urllib.parse.urlsplit(url)
# print(data.scheme+"://"+data.netloc+data.path)
 
# if url.endswith('/'):
#     print(url[:-1])
import requests

print(requests.get('https://www.youtube.com/').status_code)