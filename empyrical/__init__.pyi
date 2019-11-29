from typing import Any

import pandas as pd
DAILY = 'daily'
WEEKLY = 'weekly'
MONTHLY = 'monthly'
QUARTERLY = 'quarterly'
YEARLY = 'yearly'

def annual_volatility(returns:pd.Series, period:str=DAILY, **kwargs:Any) -> float: ...
