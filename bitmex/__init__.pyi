from typing import Dict, List, Any
class BitmexExecution:
    def Execution_get(self, symbol: str='',
                    reverse: bool=False,
                    count: int=20) -> List[Dict[str, Any]]: ...

class bitmex:
    Execution: BitmexExecution
    def __init__(self, *args, **kwargs):
        ...
