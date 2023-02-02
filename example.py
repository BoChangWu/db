from unittest import result
from db_connection import *
from setting import MSSQL,MySQL

sql = DB_sqlalchemy(MySQL)

datas = [
    {
        'rack_type': 'goods', 
        'rack_floor': 1,
        'column': 4,
        'row': 3, 
        'rack_no': 'Rack01', 
        'rack_name': 'Rack-1', 
        'area_no': 'A-2', 
        'area_name': 'Laser' 
    },
    {
        'rack_type': 'faults', 
        'rack_floor': 2,
        'column': 4,
        'row': 3, 
        'rack_no': 'Rack02', 
        'rack_name': 'Rack-2', 
        'area_no': 'A-1', 
        'area_name':  'ADE'
    }]



# get tables
# print(list(sql.show_tables()))

# create table
# sql.create_table_all()

# migrations
# sql.db_migrate('User_Account')

#select
res = sql.show_racks('Rack_Station')
# res = sql.select_data_interval('User_Account','id',0,6)
print(res[0]['storages'][0]['status'])

# insert

# sql.set_racks(datas)


# update
# sql.update_datas('User_Account','name','Barney',fullname='Ted Mosby')

# delete
# sql.delete_datas('User_Account')