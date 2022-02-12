class Payments_service_api():
    def __init__(self, table_name:str, min_id:int, max_id:int, rows_exported:int, created_at:str ) -> None:
        self.table_name = table_name
        self.min_id = min_id
        self.max_id = max_id
        self.rows_exported = rows_exported
        self.created_at = created_at


    def get_details(self, file_id) -> dict:
        result = {}
        result["table_name"] = self.table_name
        result["file_id"] = file_id
        result["min_id"] = self.min_id
        result["max_id"] = self.max_id
        result["rows_exported"] = self.rows_exported
        result["created_at"] =  self.created_at
        return result