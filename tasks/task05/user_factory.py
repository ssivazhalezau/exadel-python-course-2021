import json
from typing import Dict

def create_user(name: str, surname: str, age: int = 42, **kwargs) -> Dict:
    result = {  'name':     name,
                'surname':  surname,
                'age':      age,
                'extra':    kwargs
                }

    result['name'] = name
    result['surname'] = surname
    result['age'] = age
    for n, v in kwargs.items():
        result['extra'][n] = v

    return result

assert create_user("John", "Doe") == \
   {
       "name": "John",
       "surname": "Doe",
       "age": 42 ,
       "extra": {}
   } \
       and create_user("Bill", "Gates", age=65) == \
   {
       "name": "Bill",
       "surname": "Gates",
       "age": 65,
       "extra": {}
   } \
       and create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True) == \
   {
       "name": "Marie",
       "surname": "Curie",
       "age": 66,
       "extra": {
           "occupation": "physicist",
           "won_nobel": True
       }
   }, 'wrong function result'

print(create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True))
