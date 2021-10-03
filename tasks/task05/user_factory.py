import json
from typing import Dict

def create_user(name: str, surname: str, age: int = 42, **kwargs) -> Dict:
    result = {  'name':     '',
                'surname':  '',
                'age':      65,
                'extra':    {}
                }



    result['name'] = name
    result['surname'] = surname
    result['age'] = age
    for n, v in kwargs.items():
        result['extra'][n] = v

    return result

# print(create_user("John", "Doe"))
# print(create_user("Bill", "Gates", age=65))
print(create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True))
