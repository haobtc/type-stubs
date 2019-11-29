from typing import TypeVar, Type

class Base:
    pass

def declarative_base() -> Type[Base]: ...
