from unittest import result
from db_connection import *
from db_model_parser import *
from db_model import *
from setting import MSSQL, MySQL
from datetime import datetime
sql = DB_sqlalchemy(MSSQL,is_mssql=True)

datas = []



# get tables
# sql.get_tables()
# create table
# sql.create_table_all()

# migrations
# sql.db_migrate('User_Account')

#select
# res = sql.select_data('Parent')
# res = sql.select_data_interval('User_Account','id',0,6)
# print(res)

# insert

# m = {
#     'name': 'mission_1',
#     'sub_missions': ['S1','S2'] 
# }
# m['sub_missions'] = [Sub_Mission_handler.parse({'step': m['sub_missions'][k]}) for k in range(len(m['sub_missions'])) ]
# sql.insert_data([m],'Main_Mission')
user =[
    {
        'name': 'Jason',
        'fullname':'JasonWu',
        'nickname': 'Json'
    }
]
sql.insert_data(user,'User_Account')
# update
# sql.update_datas('User_Account','name','Barney',fullname='Ted Mosby')

# delete
# sql.delete_datas('User_Account')