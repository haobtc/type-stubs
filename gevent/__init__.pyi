from typing import Callable, Any

class GThread:
    pass

def spawn(func:Callable, *args:Any, **kwargs:Any) -> GThread:...
