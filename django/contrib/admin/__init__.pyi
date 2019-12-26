from typing import List, Tuple, Union, Any

class Admin:
    pass

class ModelAdmin(Admin):
    list_display: Union[List[str], Tuple[str, ...]]
    search_fields: Union[List[str], Tuple[str, ...]]

def autodiscover() -> None: ...

site: Any
