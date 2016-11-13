import json

# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# s = json.loads(json_str)
# print(s)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 86)


print(json.dumps(s, default=lambda obj: obj.__dict__))