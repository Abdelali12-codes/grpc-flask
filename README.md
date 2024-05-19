# grpc flask app

# install requirements
```
pip install -r requirements.txt
```

# Generate gRPC Code
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto
```

# start grpc server 
```
python grpc_server.py
```

# start flask server

```
python app.py
```

# test

```
curl -X POST http://localhost:5000/hello -H "Content-Type: application/json" -d '{"name": "World"}'
```