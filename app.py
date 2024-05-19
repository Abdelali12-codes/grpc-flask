from flask import Flask, request, jsonify
import grpc
import service_pb2
import service_pb2_grpc

app = Flask(__name__)

# Create a gRPC channel
channel = grpc.insecure_channel('localhost:50051')
stub = service_pb2_grpc.MyServiceStub(channel)

@app.route('/hello', methods=['POST'])
def say_hello():
    name = request.json['name']
    response = stub.SayHello(service_pb2.HelloRequest(name=name))
    return jsonify({'message': response.message})

if __name__ == '__main__':
    app.run(port=5000)
