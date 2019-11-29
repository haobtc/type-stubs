from typing import Dict, Any, List, Union, Iterable, Optional, Tuple, Set

class Storage:
    def get_available_name(self, name:str, max_length:Optional[int]=None) -> str: ...

class FileSystemStorage(Storage):
    def _save(self, name:str, content:Any, *args:Any, **kwargs:Any) -> None: ...
