from dataclasses import dataclass
@dataclass(frozen=True)
class DecisionExplanation:
 decision:str; confidence:float; reasons:tuple[str,...]
class DecisionExplainer:
 def explain(self,decision,confidence,reasons): return DecisionExplanation(decision,max(0.0,min(1.0,confidence)),reasons)
