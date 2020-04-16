from typing import Optional, Dict, Any

class Exchange:
    proxies: Dict[str, str]
    def load_markets(self, reload:bool=False, params:Dict[str, Any]={}): ...
    def load_accounts(self, reload:bool=False, params:Dict[str, Any]={}): ...
    def fetch_order_book(self, symbol:str) -> Dict[str, Any]: ...

class bitmex(Exchange):
    pass
