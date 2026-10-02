from dataclasses import dataclass
@dataclass(frozen=True)
class AndroidUXContract:
    screens:tuple[str,...]
    rtl:bool=True
    def valid(self)->bool:return bool(self.screens) and self.rtl
DEFAULT_ANDROID_CONTRACT=AndroidUXContract(("ورود","اتصال حساب","بازار","استراتژی","جلسه","گزارش"))
