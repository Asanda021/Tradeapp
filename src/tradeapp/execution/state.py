from enum import Enum
class OrderState(str,Enum):
    CREATED='created'; SUBMITTED='submitted'; PARTIAL='partial'; FILLED='filled'; CANCELLED='cancelled'; REJECTED='rejected'
