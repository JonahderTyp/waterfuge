start "Webserver" flask --app waterfuge:create_app run --host 0.0.0.0 -p 8080
start "Broadcast" python broadcastIp.py