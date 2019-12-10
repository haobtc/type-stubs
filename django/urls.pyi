from typing import Dict, Any, List, Union, Iterable, Optional, Tuple, Set
from django.http import HttpRequest, HttpResponse

def reverse(viewname:str, urlconf:Any=None, args:Any=None, kwargs:Any=None, current_app:Optional[str]=None) -> str: ...

def path(path:str, *args, **kwargs): ...

def include(modspec:str): ...


