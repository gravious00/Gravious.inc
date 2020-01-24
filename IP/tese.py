import requests
import json
import cv2

from pprint import pprint
regions = ['fr', 'it']
with open('2.jpg', 'rb') as fp:
    print(fp)
    response = requests.post()
pprint(response.json())
plate = response['results']
