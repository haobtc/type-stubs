from typing import Dict, Any, List, Union, Iterable, Optional, Tuple, Set
from collections import OrderedDict
from django.contrib.auth.models import User

class HttpRequest:
    GET: OrderedDict
    POST: OrderedDict
    META: Dict[str, Any]
    COOKIES: Dict[str, Any]
    path: str
    method: str
    user: User

class HttpResponse:
    def __init__(self, content: Any, **kwargs: Any): ...

class JsonResponse(HttpResponse):
    def __init__(self, content: Any, **kwargs: Any): ...

class HttpResponseBadRequest(HttpResponse):
    def __init__(self, content: Any, **kwargs: Any): ...

class HttpResponseRedirect(HttpResponse):
    def __init__(self, url: str, **kwargs: Any): ...

class HttpError(Exception): ...
class Http404(HttpError): ...
