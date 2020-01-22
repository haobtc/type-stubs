
class RequestTimeout(Exception):
    pass

class ExchangeError(Exception):
    pass

class ExchangeNotAvailable(ExchangeError):
    pass
