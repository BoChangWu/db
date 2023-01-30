from unittest import result
from db_connection import *
from setting import MSSQL, MySQL
from datetime import datetime
sql = DB_sqlalchemy(MySQL)

datas = [
    {'name': 'Karry','fullname' : 'Karry chen','nickname':'tudo','number':'0932','gender':1,'weight': 50.0},
    ]



# get tables
# sql.get_tables()
# create table
sql.create_table_all()

# migrations
# sql.db_migrate('User_Account')

#select
# res = sql.select_data('User_Account')
# res = sql.select_data_interval('User_Account','id',0,6)
# print(res)

# insert
# sql.insert_data(datas,'User_Account')

# update
# sql.update_datas('User_Account','name','Barney',fullname='Ted Mosby')

# delete
# sql.delete_datas('User_Account')