"""Optional local-model runtime. No paid API is required.

The runtime invokes a locally installed command when configured and otherwise
uses the deterministic report engine. It never sends prompts to a network.
"""
from dataclasses import dataclass
import json,subprocess

@dataclass(frozen=True)
class LocalModelResult:
    text:str
    model:str
    used_fallback:bool

class LocalModelRuntime:
    def __init__(self,command:str|None=None,timeout:int=30):
        self.command=command; self.timeout=timeout
    def generate(self,prompt:str)->LocalModelResult:
        if not prompt: raise ValueError("prompt is required")
        if not self.command:
            return LocalModelResult("مدل محلی تنظیم نشده است؛ توضیح قطعی و محلی استفاده شد.","deterministic",True)
        proc=subprocess.run(self.command,shell=True,input=json.dumps({"prompt":prompt}),text=True,capture_output=True,timeout=self.timeout)
        if proc.returncode!=0: raise RuntimeError("local model process failed")
        return LocalModelResult(proc.stdout.strip(),self.command,False)
