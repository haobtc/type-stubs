from typing import Optional, Dict, Any

class Exchange:
    proxies: Dict[str, str]
    def load_markets(self, reload:bool=False, params:Dict[str, Any]={}): ...
    def load_accounts(self, reload:bool=False, params:Dict[str, Any]={}): ...
    def fetch_order_book(self, symbol:str) -> Dict[str, Any]: ...
    def close(self) -> None: ...

class bitmex(Exchange):
    pass

class huobipro(Exchange):
    pass

class okex(Exchange):
    pass
