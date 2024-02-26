


class RPC:
    def send():
        raise NotImplementedError()
    def receive():
        raise NotImplementedError()


class AppendEntries(RPC):
    def send():
        pass
    def receive():
        pass

class RequestVote(RPC):
    def send():
        pass
    def receive():
        pass