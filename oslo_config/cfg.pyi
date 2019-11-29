from typing import Optional, List, Any

class OptGroup:
    pass


class ListOpt:
    def __init__(self, name:str, default:Optional[List[str]]=None, help:str='', **kwargs): ...

class IPOpt:
    def __init__(self, name:str, default:str='', help:str='', **kwargs): ...

class PortOpt:
    def __init__(self, name:str, default:int=0, help:str='', **kwargs): ...

class IntOpt:
    def __init__(self, name:str, default:int=0, help:str='', **kwargs): ...
    
class BoolOpt:
    def __init__(self, name:str, default:bool=False, help:str='', **kwargs): ...

class StrOpt:
    def __init__(self, name:str, default:str=False, help:str='', **kwargs): ...


class ConfigOpts:
    def __getattr__(self, name:str) -> Any: ...
    
    
    
