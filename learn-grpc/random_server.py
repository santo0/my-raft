import random
import time

import grpc

import random_service_pb2_grpc
import random_service_pb2

class RandomNumberServiceServicer(random_service_pb2_grpc.RandomNumberServiceServicer):

    DEFAULT_SEED = 42

    def GenerateRandomNumber(self, request, context):
        
        min_value = request.min
        max_value = request.max
        seed = request.seed if request.seed else None
        count = request.count if request.count else 1
        unique = request.unique if request.unique else False
        output_duration = request.output_duration if request.output_duration else False
        print(f"Received request: min={min_value}, max={max_value}, count={count}, unique={unique}, output_duration={output_duration}")
        if output_duration:
            start_time = time.time()

        if count <= 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Count must be a positive integer.")
            return random_service_pb2.RandomNumberResponse()

        if min_value > max_value:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Minimum value cannot be greater than maximum value.")
            return random_service_pb2.RandomNumberResponse()

        if seed is not None:
            random.seed(seed)

        if unique:
            numbers = random.sample(range(min_value, max_value + 1), count)
        else:
            numbers = [random.randint(min_value, max_value) for _ in range(count)]

        if output_duration:
            end_time = time.time()
            duration = end_time - start_time
            output_duration = "Generated {} numbers in {:.2f} seconds".format(len(numbers), duration)

        response = random_service_pb2.RandomNumberResponse(
            numbers=numbers,
            seed_used=seed if seed is not None else self.DEFAULT_SEED
        )
        print(f"Generated numbers: {numbers}, Seed used: {response.seed_used}")
        return response
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    random_service_pb2_grpc.add_RandomNumberServiceServicer_to_server(RandomNumberServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    from concurrent import futures
    serve()