from typing import Optional, Any

class BBoxClient:
    def __init__(self, connect:str, cert:Optional[str]=None): ...
    def request_result(self, srv:str, method:str, *args:Any, **kwargs:Any) -> Any: ...

class RPCError(Exception):
    code:str
