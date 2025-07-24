# Learning gRPC

I need a communication mechanism for my Raft implementation, without having to deal with serialization and other things, so I can exclusively focus on my Raft implementation.
Thus, I think gRPC is the perfect match for this. My learning journey starts at [https://grpc.io/docs/languages/python/quickstart/](https://grpc.io/docs/languages/python/quickstart/).

```bash
python3 -m pip install virtualenv
virtualenv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install grpcio grpcio-tools
```

At first, let's consider a client and a server, which communicate with each other using a gRPC service defined by a protocol buffer. gRPC stands for google(idk??) Remote Procedure Calls, which uses HTTP/2 for transport and Protocol Buffers as interface description language (IDL). An IDL is a language for describing interfaces in software components, enabling communication between them without having to worry about any programming language or type of device. For example, gRPC can enable communication betwen a data center and my smartphone.

See `random_service.proto` for the service I will be using for learning. It's a service for communicating with a server that returns one or multiple random number, given some parameters. After writing the service specification, you have to generate the request and response classes.

```bash
python3 -m grpc_tools.protoc -I ./learn-grpc/ --python_out=./learn-grpc/ --pyi_out=./learn-grpc/ --grpc_python_out=./learn-grpc/ ./learn-grpc/random_service.proto
```

The required fields are deprecated in protobuf3 as explained [in this github issue](https://github.com/protocolbuffers/protobuf/issues/2497).

Pretty satisfying experience, very easy to use.
Next step, start my raft implementation using gRPC.
