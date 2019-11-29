from typing import Any
from django.db.models import Model
from django.contrib.auth.models import Group

def assign_perm(perm:str,  group:Group, obj:Any) -> None: ...
