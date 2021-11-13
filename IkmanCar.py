import json


with open('IkmanCars.json', 'r') as f:
    data = json.loads(f)

"""
for ads in data['ads']:
    try:
        print(ads['title'], ads['description'], ads['details'], ads['price'])
    except:
        pass

"""

