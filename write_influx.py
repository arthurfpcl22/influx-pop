from influxdb import InfluxDBClient

user = 'root'
password = 'root'
dbname = 'teste'
dbuser = 'isau'
dbuser_password = 'my_secret_password'
#query = 'select Float_value from cpu_load_short;'
#query_where = 'select Int_value from cpu_load_short where host=$host;'
#bind_params = {'host': 'server01'}
hostname = 'localhost'
port = 8086

client = InfluxDBClient(host= hostname, port=port, database=dbname)

client.create_database('teste4')

print(client.get_list_database())

client.switch_database('teste4')

json_body = [
    {
        "measurement": "teste_escrita",
        "tags": {
            "local": "pop-rn"
        },
        "time": "2022-05-05T11:09:00Z",
        "fields": {
            "duration": 127.0
        }
    }
]

#client.switch_user(dbuser, dbuser_password)

print(client.write_points(json_body))

