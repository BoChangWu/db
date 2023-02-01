from xmlrpc.client import Boolean
import sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import inspect
import urllib
from db_model import *
from db_model_parser import *

# DB Class
class DB_sqlalchemy():

    def __init__(self,db_info=None,is_mssql=False):
        
        if is_mssql:
            params = urllib.parse.quote_plus(f"DRIVER={db_info['DRIVER']};"
                                    f"SERVER={db_info['HOST']};"
                                    f"DATABASE={db_info['DB']};"
                                    f"UID={db_info['USER']};"
                                    f"PWD={db_info['PASSWORD']}")

            self.engine = create_engine(f"{db_info['ENGINE']}:///?odbc_connect={params}")
        else: 
            self.engine = create_engine(f"{db_info['ENGINE']}://{db_info['USER']}:{db_info['PASSWORD']}@{db_info['HOST']}/{db_info['DB']}?charset=utf8mb4")
        self.session = Session(self.engine)

    def create_table_all(self) -> None:
        # 建立所有的table , 若有新增table , 可以再呼叫一次此function即可建立
        Base.metadata.create_all(self.engine)

    def compare_col(self,table:str,new:list,old:list) -> None:
        '''
        function for db_migrate
        '''
        for n in new:

            if n not in [i['name'] for i in old]:
                
                self.add_column(table,n,Models[table].cols[n].type)
                
        for o in old:

            if o['name'] not in new:

                self.drop_column(table,o['name'])
                pass

    def add_column(self,table:str,col:str,c_type:str):
        '''
        function for db_migrate
        '''
        connection = self.engine.connect()
        stmt = f"ALTER TABLE {table.lower()} ADD {col} {c_type};"
        # stmt = f"ALTER TABLE cos_account ADD number VARCHAR(30);;"
        connection.execute(stmt)

    def drop_column(self,table:str,col:str) -> None:
        '''
        function for db_migrate
        '''
        connection = self.engine.connect()
        stmt = f"ALTER TABLE {table.lower()} DROP {col};"
        connection.execute(stmt)

    def db_migrate(self,table=None) -> None:
        '''
        目前只有針對沒有的column 做新增或刪除
        '''
        inspector = inspect(self.engine)
        '''
        schemas = inspector.get_schema_names()
        for schema in schemas:
            print(schema)
            for table in inspector.get_table_names(schema=schema):
                print(table)
                for column in inspector.get_columns(table,schema=schema):
                    print(column)

        目前我們使用的 schema 都是dbo 最外層的 schema可以寫死, 也可以不要給
        '''
    
        if table:

            new = Models[table].__table__.columns.keys()
            t_info = inspector.get_columns(table,schema='dbo')
            self.compare_col(table,new,t_info)

        else:
            for t in inspector.get_table_names(schema='dbo'):
                
                new = Models[t].__table__.columns.keys()
                t_info = inspector.get_columns(t,schema='dbo')
                self.compare_col(new,t_info)

    

    def insert_data(self,datas,table:str) -> None:

        with self.session as session:
            
            data_lst = []

            for data in datas:

                data_lst.append(Model_Parser[table].parse(data))

            session.add_all(data_lst)
            session.commit()

    def select_data(self,table:str,order_by=None,group_by=None,offset=None,limit=None,**kwargs) -> list:
        '''
        order_by: col name, group_by: col name, limit: int
        '''

        instance = self.session.query(Models[table])

        if kwargs:

            for i,k in kwargs.items():
                instance = instance.filter(Models[table].cols[i] == k)
        else:
            instance = instance.all()
            

        if order_by:
                instance = instance.order_by(order_by)
        if group_by:
                instance = instance.group_by(group_by)
        if offset:
                instance = instance.offset(offset=offset)
        if limit:
                instance = instance.limit(limit)
        
        
        datas = []

        for i in instance:
            print()
            datas.append(Model_Parser[table].load(i))
        
        return datas

    def select_data_interval(self,table:str,col=None,gte=None,lte=None) -> list:
        '''
        定義參數 interval 只接受 {'col':欄位名稱,'gte': 最小值 , 'lte': 最大值 }
        '''
        
        instance = self.session.query(Models[table])
        
        if col:
            if gte:
                instance = instance.filter(Models[table].cols[col]>=gte)
            if lte:
                instance = instance.filter(Models[table].cols[col]<=lte)

        datas = []

        if instance:

            for i in instance:
                
                datas.append(Model_Parser[table].load(i))

        return datas

    def delete_datas(self,table:str,con_key=None,con_val=None) -> None:
        
        instance = self.session.query(Models[table])
        if con_key and con_val:
            
            instance.filter(Models[table].cols[con_key] == con_val).delete(synchronize_session = False)
        else:
            instance.delete(synchronize_session = False)
        
        
        self.session.commit()

    def update_datas(self,table:str,con_key=None,con_val=None,**kwargs) -> None:

        instance = self.session.query(Models[table])
        if kwargs:
            if con_key and con_val:
                instance = instance.filter(Models[table].cols[con_key] == con_val)
                
                for i,k in kwargs.items():

                    instance.update({Models[table].cols[i]: k},synchronize_session = False)

            self.session.commit()

    ####### 以下開放自訂功能 #######
'''
    tutorial: 
    https://docs.sqlalchemy.org/en/14/orm/quickstart.html#simple-select
    Selecting ORM Entities and Columns: 
    https://docs.sqlalchemy.org/en/14/tutorial/data_select.html#tutorial-selecting-orm-entities
'''

    



    


