from typing import TypeVar, Type

class ColumnType:
    def __call__(self, *args, **kwargs) -> ColumnType: ...

class DateTime(ColumnType):
    pass

class Integer(ColumnType):
    pass

class BigInteger(ColumnType):
    pass

class String(ColumnType):
    pass

class Numeric(ColumnType):
    pass

class JSON(ColumnType):
    pass

class ForeignKey(ColumnType):
    pass

class Column:
    def __init__(self, *args, **kwargs): ...
