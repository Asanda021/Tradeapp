from dataclasses import dataclass
@dataclass(frozen=True)
class WindowsScreen:
    name:str
    controls:tuple[str,...]
@dataclass(frozen=True)
class WindowsUXContract:
    screens:tuple[WindowsScreen,...]
    rtl:bool=True
    def valid(self)->bool:
        return bool(self.screens) and self.rtl and all(s.controls for s in self.screens)
DEFAULT_WINDOWS_CONTRACT=WindowsUXContract((
    WindowsScreen("اتصال حساب",("ورود","اتصال API","وضع آزمایشی")),
    WindowsScreen("بازار",("نماد","بازه زمانی","داده بازار")),
    WindowsScreen("استراتژی",("انتخاب","آزمایش","گزارش")),
    WindowsScreen("جلسه",("شروع","مکث","توقف","توقف اضطراری")),
    WindowsScreen("گزارش",("خلاصه","معاملات","ریسک","خروجی")),
))
