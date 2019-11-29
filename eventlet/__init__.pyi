from typing import Callable, Any

class GreenThread:
    pass

def spawn(func:Callable, *args:Any, **kwargs:Any) -> GreenThread:...
