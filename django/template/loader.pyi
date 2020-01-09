from typing import Dict, Any
from django.http import HttpRequest

def render_to_string(template_name:str, context:Dict[str, Any], request:HttpRequest) -> str: ...
