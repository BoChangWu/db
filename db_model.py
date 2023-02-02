from ast import For
from sqlalchemy import Column,String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from datetime import datetime

# define your model here
# model class 的命名要跟 tablename 一致
    
Base = declarative_base()

class eRack_Comnct_Log(Base):

    __tablename__ = 'eRack_Comnct_Log'

    id = Column(Integer, primary_key=True)
    create_time = Column(DateTime,default=datetime.now)
    secs_function = Column(String(30))
    function_class = Column(String(30))
    action = Column(String(30))
    message = Column(Text,nullable=True)

    cols = {
        'id': id,
        'create_time': create_time,
        'secs_function': secs_function,
        'function_class': function_class,
        'action': action,
        'message': message
    }

    def __repr__(self):
        return f"""
            eRack_Comnct_Log(id={self.id!r},create_time={self.create_time!r}, secs_function={self.secs_function!r},
            action={self.action!r},function_class={self.function_class!r},message={self.message!r})
            """



class Rack_Station(Base):

    __tablename__ = 'Rack_Station'

    id = Column(Integer,primary_key=True)
    rack_type = Column(String(50))
    rack_floor = Column(Integer)
    column = Column(Integer)
    row = Column(Integer)
    rack_no = Column(String(50))
    rack_name = Column(String(50))
    area_no = Column(String(50))
    area_name = Column(String(50))

    storages = relationship('Rack_Storage_Station')
    

    cols = {
        'id': id, 
        'rack_type': rack_type, 
        'rack_floor': rack_floor,
        'column': column,
        'row': row, 
        'rack_no': rack_no, 
        'rack_name': rack_name, 
        'area_no': area_no, 
        'area_name': area_name,
        'storages': storages 
    }


class Rack_Storage_Station(Base):

    __tablename__ = 'Rack_Storage_Station'
    
    id = Column(Integer,primary_key=True)
    storage_no = Column(String(50))
    storage_name = Column(String(50))
    robot_port = Column(String(50))
    
    status = relationship('Rack_Storage_Status')
    rack_id = Column(ForeignKey('Rack_Station.id',ondelete='CASCADE'))

    cols = {
        'id': id, 
        'storage_no': storage_no, 
        'storage_name': storage_name, 
        'robot_port': robot_port,
        'status': status,
        'rack_id': rack_id,
    }

class Rack_Storage_Status(Base):

    __tablename__ = 'Rack_Storage_Status'

    id = Column(Integer,primary_key=True)
    foup_no = Column(String(50))
    sort_no = Column(Integer)
    action = Column(String(50))
    status = Column(String(50))
    stuff_no = Column(String(50))
    update_time = Column(DateTime)

    storage_id = Column(ForeignKey('Rack_Storage_Station.id',ondelete='CASCADE'))

    cols = {
        'id': id,
        'foup_no': foup_no, 
        'sort_no': sort_no, 
        'action': action, 
        'status': status,
        'stuff_no': stuff_no,
        'update_time': update_time,
        'storage_id': storage_id, 
    }

Models = {
    'eRack_Comnct_Log': eRack_Comnct_Log,
    'Rack_Storage_Status': Rack_Storage_Status,
    'Rack_Station': Rack_Station,
    'Rack_Storage_Station': Rack_Storage_Station

}