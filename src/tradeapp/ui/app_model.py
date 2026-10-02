from dataclasses import dataclass
from decimal import Decimal
from tradeapp.decision.engine import Decision
@dataclass(frozen=True)
class AppViewModel:
    connection:str
    market:str
    equity:Decimal
    decision:str
    confidence:Decimal
    status:str
class AppController:
    def build(self,connection:str,market:str,equity:Decimal,decision:Decision,status:str="آماده")->AppViewModel:
        return AppViewModel(connection,market,equity,decision.signal.value,decision.confidence,status)
