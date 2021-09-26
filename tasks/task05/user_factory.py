import json

def create_user(name, surname, age=42, **kwargs):
    result = {  'name':     '',
                'surname':  '',
                'age':      65,
                'extra':    {}
                }

    assert type(name) == str and type(surname) == str and name and surname, 'Only human names allowed'
    assert type(age) == int, 'Please use positive integers for age'
    assert age>0, 'Hello, Marty McFly'

    result['name'] = name
    result['surname'] = surname
    result['age'] = age
    for n, v in kwargs.items():
        result['extra'][n] = v

    return json.dumps(result, sort_keys=False, indent=4)

# print(create_user("John", "Doe"))
# print(create_user("Bill", "Gates", age=65))
print(create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True))
