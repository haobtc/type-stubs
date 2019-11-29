from typing import Any

class Cache:
    def get(self, key:str, expire:float=0): ...
    def set(self, key:str, value:Any, timeout:int=100): ...

cache:Cache
