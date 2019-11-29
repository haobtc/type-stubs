
class Random:
    @staticmethod
    def get_random_bytes(n:int) -> bytes: ...

    @staticmethod
    def new() -> 'Random': ...

    def read(self, n:int) -> bytes: ...

