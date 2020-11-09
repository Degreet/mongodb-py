from pymongo import MongoClient
import config, random

cluster = MongoClient(config.uri)
db = cluster.mongodb_py

def reg():
  name = input("Придумайте логин >> ")
  user = db.users.find_one({ "name": name })

  if user:
    print("Ошибка. Такой логин уже занят.\n")
    reg()
  else:
    code = random.randint(100, 900)
    db.users.insert_one({ "name": name, "code": code })
    print("Вы были зарегистрированы! Ваш код: " + str(code))

reg()