class LoggerMixin:
    def log(self,message):
        print(f'[log]{message}')

# main class
class Database(LoggerMixin):
    def save(self,data):
        self.log("saveing data to the database")
        print("data saved:",data)
  



db= Database()
db.save({
    'name':'Nazim',
    'age': 25
})

class JSONMixin:
    def to_json(self):
        import json 
        return json.dumps(self.__dict__)
    
class User (LoggerMixin,JSONMixin):
    def __init__(self,name):
        self.name=name
        self.log(f'User{self.name} created')

u=User("AASIM")
print (u.to_json())