from typing import Dict, Any, List, Union, Iterable, Optional, Tuple, Set, Iterator, TypeVar, Generic
from datetime import datetime
from decimal import Decimal

T = TypeVar('T')

class Model:
    id: 'BigIntegerField'
    objects: Manager['Model']

    class DoesNotExist(Exception):
        ...

    def save(self, **kwargs:Any) -> Any: ...
    def refresh_from_db(self) -> None: ...

class Manager(Generic[T]):
    model: 'Model'
    def all(self) -> 'QuerySet': ...
    def create(self, *args:Any, **kwargs:Any) -> Any: ...
    def get_or_create(self, *args:Any, **kwargs:Any) -> Tuple[T, bool]: ...
    def update_or_create(self, *args:Any, **kwargs:Any) -> Tuple[T, bool]: ...
    def filter(self, *args:'Q', **kwargs:Any) -> Any: ...
    def exclude(self, *args:'Q', **kwargs:Any) -> Any: ..
    def count(self) -> int: ...
    def exists(self) -> bool: ...    
    def get(self, **kwarg:Any) -> Any: ...
    def get_for_model(self, *args:Any, **kwargs:Any) -> Any: ...

class Field:
    def __init__(self, *args:Any, **kwargs:Any): ...
    def __get__(self, instance:Any, owner:Any) -> Any: ...

class IntegerField(Field):
    def __get__(self, instance:Any, owner:Any) -> int: ...

class SmallIntegerField(Field):
    def __get__(self, instance:Any, owner:Any) -> int: ...

class BigIntegerField(Field):
    def __get__(self, instance:Any, owner:Any) -> int: ...

class FloatField(Field):
    def __get__(self, instance:Any, owner:Any) -> float: ...

class CharField(Field):
    def __get__(self, instance:Any, owner:Any) -> str: ...

class TextField(Field):
    def __get__(self, instance:Any, owner:Any) -> str: ...

class AutoField(Field):
    def __get__(self, instance:Any, owner:Any) -> int: ...

class BooleanField(Field):
    def __get__(self, instance:Any, owner:Any) -> bool: ...

class DecimalField(Field):
    def __get__(self, instance:Any, owner:Any) -> Decimal: ...

class DateTimeField(Field):
    def __get__(self, instance:Any, owner:Any) -> datetime: ...

class ForeignKey(Field): ...
class ImageField(Field): ...

class PositiveIntegerField(Field):
    def __get__(self, instance:Any, owner:Any) -> int: ...

class OneToOneField(Field): ...

class NullBooleanField(Field):
    def __get__(self, instance:Any, owner:Any) -> Optional[bool]: ...
class ManyToManyField(Field): ...

def CASCADE(collector:Any, field:Field, sub_objs:Any, using:str): ...
def SET_NULL(collector:Any, field:Field, sub_objs:Any, using:str): ...

class Q:
    def __init__(self, *fields:str, **kwargs:Any): ...
    def __or__(self, other:'Q') -> 'Q': ...

class Sum:
    def __init__(self, *fields:str, **kwargs:Any): ...

class Count:
    def __init__(self, *fields:str, **kwargs:Any): ...

class Max:
    def __init__(self, *fields:str, **kwargs:Any): ...


class QuerySet(Generic[T]):
    def filter(self, *args:'Q', **kwargs:Any) -> 'QuerySet'[T]: ...
    def exclude(self, *args:'Q', **kwargs:Any) -> 'QuerySet'[T]: ...
    def all(self) -> 'QuerySet'[T]: ...
    def order_by(self, *args:str, **kwargs:Any) -> 'QuerySet'[T]: ...
    def select_related(self, *names:str) -> 'QuerySet'[T]: ...
    def first(self) -> Optional[T]: ...
    def last(self) -> Optional[T]: ...
    def get(self, *args:Q, **kwargs:Any) -> T: ...
    def count(self) -> int: ...    
    def exists(self) -> bool: ...
    def __iter__(self) -> Iterator[T]: ...
    def __getitem__(self, idx:int) -> T: ...
