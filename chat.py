import json
trans=open('intents.json',)
data=json.load(trans)
for i in data['intents']:
    print(i)

trans.close()