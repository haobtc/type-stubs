# ccxt error hierchary

class BaseError(Exception):
    pass

class NetworkError(BaseError):
    pass

class ExchangeError(BaseError):
    pass

# derived from network error
class RequestTimeout(NetworkError):
    pass

class DDoSProtection(NetworkError):
    pass

class ExchangeNotAvailable(NetworkError):
    pass

class InvalidNonce(NetworkError):
    pass

# derived from ExchangeError
class BadRequest(ExchangeError):
    pass

class BadResponse(ExchangeError):
    pass

class NotSupported(ExchangeError):
    pass

class InvalidOrder(ExchangeError):
    pass

class InvalidAddress(ExchangeError):
    pass

class ArgumentsRequired(ExchangeError):
    pass

class AuthenticationError(ExchangeError):
    pass

class InsufficientFunds(ExchangeError):
    pass
