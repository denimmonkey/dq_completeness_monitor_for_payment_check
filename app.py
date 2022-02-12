from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import json
import os
from src import completeness_monitor_service as CMS

app = Flask(__name__)
engine = create_engine(os.environ.get('PG_CONNECTION_STRING'))
#engine = create_engine("postgresql://nrvzjggz:ZKFqcbIccMe-_HwxTzRz--n-jbXY4Qeb@abul.db.elephantsql.com/nrvzjggz")

@app.route("/")
def status_check():
    return "DQ completeness service is running",200

@app.route("/dq_check/", methods=["GET"])
def compare_data():
    file_id = request.args.get("file_id")
    cms = CMS.completeness_monitor_service()
    count_mismatch = cms.check_missing_data(engine, cms.get_payments_service_api_data(file_id))
    return jsonify(count_mismatch)

if __name__ == '__main__':
	app.run(host ='0.0.0.0', port = 8080, debug = True)