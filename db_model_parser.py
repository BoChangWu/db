from db_model import *

# create your Parser here.
# example
class User_handler():
    def parse(self,data=None) -> User_Account:

        if data != None:
            return User_Account(
                name = data['name'],
                fullname = data['fullname'],
                nickname = data['nickname'],
                number  = data['number'],
                gender = data['gender']
                )

    def load(self,data: User_Account) -> dict:
        return {
            'id':data.id, 
            'name': data.name,
            'fullname': data.fullname,
            'nickname' : data.nickname,
            'number'  : data.number,
            'gender' : data.gender
            }

Model_Parser = {
    'User_Account': User_handler
}