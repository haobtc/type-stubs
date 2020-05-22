
class BaseError(Exception):
    pass

class RequestTimeout(BaseError):
    pass

class ExchangeError(BaseError):
    pass

class ExchangeNotAvailable(ExchangeError):
    pass

class BadRequest(ExchangeError):
    pass
