from dataclasses import dataclass
import time
@dataclass(frozen=True)
class RetryPolicyV2:
    max_attempts:int=3
    base_delay:float=.1
    def delay(self,attempt:int)->float:return self.base_delay*(2**max(0,attempt-1))
class RetryGuard:
    def __init__(self,policy:RetryPolicyV2=RetryPolicyV2()):self.policy=policy
    def run(self,operation):
        last=None
        for attempt in range(1,self.policy.max_attempts+1):
            try:return operation()
            except (TimeoutError,ConnectionError) as exc:
                last=exc
                if attempt<self.policy.max_attempts: time.sleep(self.policy.delay(attempt))
        raise last
