import grpc
import argparse
import random_service_pb2_grpc
import random_service_pb2

def run(min_value, max_value, count, seed, unique, output_duration, server_address):
    with grpc.insecure_channel(server_address) as channel:
        stub = random_service_pb2_grpc.RandomNumberServiceStub(channel)
        request = random_service_pb2.RandomNumberRequest(
            min=min_value, 
            max=max_value, 
            count=count, 
            unique=unique, 
            output_duration=output_duration, 
            seed=seed,
        )
        response = stub.GenerateRandomNumber(request)
        print(f"Random number from server: {response}") # This will print the response object in a nice format
        print(f"Numbers: {response.numbers}") # List of generated random numbers

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="gRPC Random Number Client")
    parser.add_argument('--min', type=int, default=1, help='Minimum value')
    parser.add_argument('--max', type=int, default=100, help='Maximum value')
    parser.add_argument('--count', type=int, default=1, help='Number of random numbers to request')
    parser.add_argument('--seed', type=int, default=None, help='Seed for random number generation')
    parser.add_argument('--unique', action='store_true', help='Request unique random numbers')
    parser.add_argument('--output_duration', action='store_true', help='Output duration of the request')
    parser.add_argument('--server', type=str, default='localhost:50051', help='gRPC server address')

    args = parser.parse_args()
    run(args.min, args.max, args.count, args.seed, args.unique, args.output_duration, args.server)