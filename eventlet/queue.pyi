from typing import Any, Union

class Empty(Exception):
    ...

class LightQueue:
    def put(self, v:Any) -> None: ...
    def get(self, timeout:Union[None, float, int]=None): ...
