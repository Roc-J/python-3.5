import json

class Student(object):
      def __init__(self,name,age,score):
            self.name=name
            self.age=age
            self.score=score

def student2dict(std):
      return {
              'name':std.name,
              'age':std.age,
              'score':std.score
        }

def dict2student(d):
      return Student(d['name'],d['age'],d['score'])
s=Student('Bob',20,88)
