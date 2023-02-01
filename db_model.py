from sqlalchemy import Column,String, Integer,Float, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy import Integer

from sqlalchemy.orm import relationship

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

    cols = {
        'id': id,
        'name': name,
        'fullname': fullname,
        'nickname': nickname,

    }

    # def __repr__(self):
    #     return f"User(id={self.id!r},name={self.name!r}, fullname={self.fullname!r})"
class Main_Mission(Base):
    __tablename__ = 'Main_Mission'
    
    id = Column(Integer,primary_key=True)
    name = Column(String(30))
    sub_missions = relationship("Sub_Mission")

class Sub_Mission(Base):
    __tablename__ = 'Sub_Mission'
    id = Column(Integer,primary_key=True)
    step = Column(String(30))
    main_mission_id = Column(ForeignKey('Main_Mission.id',ondelete='CASCADE'))


Models = {
'User_Account' : User_Account,
'Main_Mission': Main_Mission,
'Sub_Mission': Sub_Mission
}