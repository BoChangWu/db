from sqlalchemy import Column,String, Integer,Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from datetime import datetime
# define your model here
# model class 的命名要跟 tablename 一致
    
Base = declarative_base()

#example
class User_Account(Base):

    __tablename__ = 'User_Account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String(30))
    nickname = Column(String(30))
    number  = Column(String(30))
    gender = Column(Integer)
    birth = Column(DateTime,default=datetime.now)
    weight = Column(Float)

    cols = {
        'id': id,
        'name': name,
        'fullname': fullname,
        'nickname': nickname,
        'number': number,
        'gender': gender,
        'birth': birth,
        'weight': weight 
    }

    # def __repr__(self):
    #     return f"User(id={self.id!r},name={self.name!r}, fullname={self.fullname!r})"


Models = {
'User_Account' : User_Account
}