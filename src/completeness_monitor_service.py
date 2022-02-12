from src import payments_service_api as ps_api
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class completeness_monitor_service():

    def get_payments_service_api_data(self, file_id) -> dict:
        """
            function to get data about exported file using the api call
            ----- hard coding some return values for verification -----
        """
        psa = ps_api.Payments_service_api(table_name = "ledger_tax_rate",  
                                                      min_id = 1, 
                                                      max_id = 25, 
                                                      rows_exported = 20, 
                                                      created_at = "2020-12-22T00:00:00")        
        export_file_data = psa.get_details(file_id)
        return export_file_data

    def create_sql_engine(self, connection_string:str):
        engine = create_engine(connection_string)
        return engine

    def check_missing_data(self, engine, payments_service_api_data) -> int:
        """
        compare table count with row_count in exported file
        """
        exported_file_data = payments_service_api_data
        query_string = f"""SELECT COUNT(*) 
                           FROM {exported_file_data["table_name"]}
                           WHERE 
                                id >= {exported_file_data["min_id"]} AND 
                                id <= {exported_file_data["max_id"]} AND
                                updated = '{exported_file_data["created_at"]}' """
        statement = text(query_string)
        con = engine.connect()
        table_row_count = 0
        query_result = con.execute(statement)
        for result in query_result:
            table_row_count = result
        table_row_count = table_row_count[0]
        mismatch = exported_file_data["rows_exported"] - table_row_count

        result = {}
        if mismatch == 0:
            result["status"] = 0
            result["description"] = "no data mismatch"
            return result
        if mismatch > 0:
            result["status"] = 1
            result["description"] = f"exported file has rows not present in table {exported_file_data['table_name']}"
            return result
        if mismatch < 0:
            result["status"] = 1
            result["description"] = f"exported file has less rows than in table {exported_file_data['table_name']}"
            return result
            


if __name__ == '__main__':
    cms = completeness_monitor_service()
    #result = cms.get_payments_service_api_data()
    engine = create_engine("postgresql://nrvzjggz:ZKFqcbIccMe-_HwxTzRz--n-jbXY4Qeb@abul.db.elephantsql.com/nrvzjggz")
    count_mismatch = cms.check_missing_data(engine, cms.get_payments_service_api_data(10))
    print(count_mismatch)