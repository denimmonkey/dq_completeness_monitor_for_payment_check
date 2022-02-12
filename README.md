# dq_completeness_monitor_for_payment_check
checks and alerts for missing data in database tables 

#.   The service gets data about the exported file using the file_id and payments service_api
     Using the information received from the payments servie api the corresponding table is queried
     The count of rows between min_id and max_id  for the appropriate created_at timestamp is compared
     against row_exported 

     end poins:
     1. /
        returns if service is up and running 
        eg.  curl -i "http://192.168.178.54/"
            HTTP/1.0 200 OK
            Content-Type: text/html; charset=utf-8
            Content-Length: 34
            Server: Werkzeug/2.0.3 Python/3.8.3
            Date: Sat, 12 Feb 2022 19:37:56 GMT

            DQ completeness service is running

    2. /dq_check/?<file_id>
        takes file_id as input parameter for payments service api and compares row counts between file and table
    eg.
    curl -i "http://192.168.178.54/dq_check/?file_id=10"
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 99
    Server: Werkzeug/2.0.3 Python/3.8.3
    Date: Sat, 12 Feb 2022 19:28:47 GMT

    {
    "description": "exported file has rows not present in table ledger_tax_rate", 
    "status": 1
    }

1. create docker image using provided Dockerfile

    docker build -t flask-image .

2. run the docker image, mapping port 80 on server to port 8080 on container

    docker run -d -p 80:8080 --name flask-container flask-image

3. hit the endpoints on the host system ip at port 90

 eg.  curl -i "http://192.168.178.54/dq_check/?file_id=10"

 HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 99
Server: Werkzeug/2.0.3 Python/3.8.3
Date: Sat, 12 Feb 2022 19:28:47 GMT

{
  "description": "exported file has rows not present in table ledger_tax_rate", 
  "status": 1
}

4. To run the application on local 
    source .env
    flask run