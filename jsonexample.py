from asyncore import read
import json

jsonstr= """{"people":[{"Id": "1","FirstName":"Benjamin","Last Name":"Finkel","Email":"ben.finkel@gmail.com"}
{"Id": "2","FirstName":"Jane","Last Name":"Doe","Email":"jane.doe@gmail.com"}
{"Id": "3","FirstName":"Pat","Last Name":"Smith","Email":"pat.smith@gmail.com"}]}"""


jsonobj=json.loads(jsonstr)

print(jsonobj)


jsonobj= json.load(open('sample.json'))

print(jsonobj)
