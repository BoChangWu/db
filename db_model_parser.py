from db_model import *

# create your Parser here.
# example
class eRack_Comnct_Log_handler():
    def parse(data=None) -> eRack_Comnct_Log:

        if data != None:
            return eRack_Comnct_Log(
                secs_function = data['secs_function'],
                function_class = data['function_class'],
                action = data['action'],
                message  = data['message'],
                )

    def load(data: eRack_Comnct_Log) -> dict:
        return {
            'id':data.id, 
            'create_time': data.create_time,
            'secs_function': data.secs_function,
            'function_class': data.function_class,
            'action': data.action,
            'message' : data.message
            }

class Rack_Station_handler():
    
    def parse(data=None) -> Rack_Station:

        if data != None:
            return Rack_Station(
                rack_type = data['rack_type'], 
                rack_floor = data['rack_floor'],
                column = data['column'],
                row = data['row'], 
                rack_no = data['rack_no'], 
                rack_name = data['rack_name'], 
                area_no = data['area_no'], 
                area_name = data['area_name'],
                storages = data['storages']
        )

    def load(data: Rack_Station) -> dict:

        return {
            'id': data.id, 
            'rack_type': data.rack_type, 
            'rack_floor': data.rack_floor,
            'column': data.column,
            'row': data.row, 
            'rack_no': data.rack_no, 
            'rack_name': data.rack_name, 
            'area_no': data.area_no, 
            'area_name': data.area_name,
            'storages': data.storages 
        }

class Rack_Storage_Station_handler():
    
    def parse(data=None) -> Rack_Storage_Station:

        if data != None:
            return Rack_Storage_Station( 
                storage_no = data['storage_no'], 
                storage_name = data['storage_name'], 
                robot_port = data['robot_port'],
                status = data['status']
            )

    def load(data: Rack_Storage_Station) -> dict:
        
        return {
            'id': data.id, 
            'storage_no': data.storage_no, 
            'storage_name': data.storage_name, 
            'robot_port': data.robot_port,
            'status': data.status,
            'rack_id': data.rack_id,
        }

class Rack_Storage_Status_handler():
    def parse(data=None) -> Rack_Storage_Status:

        if data != None:
            return Rack_Storage_Status(
                foup_no = data['foup_no'], 
                sort_no = data['sort_no'], 
                action = data['action'], 
                status = data['status'],
                stuff_no = data['stuff_no'],
                update_time = data['update_time'],
            )
    
    def load(data: Rack_Storage_Status) -> dict:
        return {
            'id': data.id,
            'foup_no': data.foup_no, 
            'sort_no': data.sort_no, 
            'action': data.action, 
            'status': data.status,
            'stuff_no': data.stuff_no,
            'update_time': data.update_time,
            'storage_id': data.storage_id,
        }

Model_Parser = {
    'eRack_Comnct_Log': eRack_Comnct_Log_handler,
    'Rack_Storage_Status': Rack_Storage_Status_handler,
    'Rack_Station': Rack_Station_handler,
    'Rack_Storage_Station' : Rack_Storage_Station_handler
}
