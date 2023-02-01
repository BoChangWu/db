from cgitb import handler
from datetime import date
from db_model import *

# create your Parser here.
# example
class User_handler():
    def parse(data=None) -> User_Account:

        if data != None:
            return User_Account(
                name = data['name'],
                fullname = data['fullname'],
                nickname = data['nickname'],

                )

    def load(data: User_Account) -> dict:
        return {
            'id':data.id, 
            'name': data.name,
            'fullname': data.fullname,
            'nickname' : data.nickname,
            }
class Main_Mission_handler():

    def parse(data=None) -> Main_Mission:
        print(type(data))
        if data != None:
            return Main_Mission(
                name = data['name'],
                sub_missions = data['sub_missions']
            )

    def load(data: Main_Mission) -> dict:

        return {
            'id': data.id,
            'name': data.name,
            'sub_missions': data.sub_missions
        }

class Sub_Mission_handler():

    def parse(data=None) -> Sub_Mission:

        if data != None:
            return Sub_Mission(
                step = data['step'],
            )

    def load(data: Sub_Mission) -> dict:

        return {
            'id': data.id,
            'step': data.step,
            'main_mission_id': data.main_mission_id
        }
Model_Parser = {
    'User_Account': User_handler,
    'Main_Mission': Main_Mission_handler,
    'Sub_Mission': Sub_Mission_handler

}