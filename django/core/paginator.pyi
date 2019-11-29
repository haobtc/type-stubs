from typing import Dict, Any, List, Union, Iterable, Optional, Tuple, Set

class Paginator:
    def __init__(self, object_list:Iterable[Any], per_page:int, orphans:int=0, allow_empty_first_page:bool=True): ...

class Page:
    def __init__(self, object_list:Iterable[Any], number:int, paginator:Paginator): ...


class EmptyPage(Exception):
    ...
