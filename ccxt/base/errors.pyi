# ccxt error hierchary

class BaseError(Exception):
    pass

class NetworkError(BaseError):
    pass

class ExchangeError(BaseError):
    pass

# inherited from network error
class RequestTimeout(NetworkError):
    pass

class DDoSProtection(NetworkError):
    pass

class RateLimitExceeded(DDoSProtection):
    pass

class ExchangeNotAvailable(NetworkError):
    pass

class InvalidNonce(NetworkError):
    pass

# inherited from ExchangeError
class BadRequest(ExchangeError):
    pass

class BadSymbol(BadRequest):
    pass

class BadResponse(ExchangeError):
    pass

class NullResponse(BadResponse):
    pass


class NotSupported(ExchangeError):
    pass

class InvalidOrder(ExchangeError):
    pass


class InvalidAddress(ExchangeError):
    pass

class AddressPending(InvalidAddress):
    pass

class NotSupported(ExchangeError):
    pass

class ArgumentsRequired(ExchangeError):
    pass

class AuthenticationError(ExchangeError):
    pass

class InsufficientFunds(ExchangeError):
    pass

# inherited from InvalidOrder
class OrderNotFound(InvalidOrder):
    pass

class OrderNotCached(InvalidOrder):
    pass

class CancelPending(InvalidOrder):
    pass

class OrderImmediatelyFillable(InvalidOrder):
    pass

class OrderNotFillable(InvalidOrder):
    pass

class DuplicateOrderId(InvalidOrder):
    pass
