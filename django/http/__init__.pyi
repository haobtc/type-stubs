from typing import Dict, Any, List, Union, Iterable, Optional, Tuple, Set
from collections import OrderedDict
from django.contrib.auth.models import User

class HttpQuery(OrderedDict):
    def getlist(self, key:str, default:List[str]=[]): ...

class HttpRequest:
    GET: HttpQuery
    POST: HttpQuery
    META: Dict[str, str]
    COOKIES: Dict[str, str]
    path: str
    method: str
    user: User
    org: Any
    member: Any
    body: str

class HttpResponse:
    def __init__(self, content: Any, **kwargs: Any): ...

class JsonResponse(HttpResponse):
    def __init__(self, content: Any, **kwargs: Any): ...

class HttpResponseBadRequest(HttpResponse):
    def __init__(self, content: Any, **kwargs: Any): ...

class HttpResponseRedirect(HttpResponse):
    def __init__(self, url: str, **kwargs: Any): ...

class HttpResponseForbidden(HttpResponse):
    def __init__(self, **kwargs: Any): ...

class HttpError(Exception): ...
class Http404(HttpError): ...

