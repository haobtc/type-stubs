from typing import Any, List
from django.db.models import Model, QuerySet
from django.contrib.auth.models import Group, Permission

def assign_perm(perm:str,  group:Group, obj:Any) -> None: ...
def remove_perm(perm:str,  group:Group, obj:Any) -> None: ...

def get_group_perms(group:Group, obj:Any) -> QuerySet[Permission]: ...
def get_user_perms(group:Group, obj:Any) -> QuerySet[Permission]: ...

