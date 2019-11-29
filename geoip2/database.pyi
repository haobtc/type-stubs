from typing import Dict, Any, List, Union, Iterable, Optional, Tuple, Set

class City:
    names: Dict[str, str]

class CityRes:
    city: City

class Reader:
    def __init__(self, fileish:str) -> None: ...
    def city(self, ip:str) -> CityRes: ...


