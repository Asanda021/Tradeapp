MESSAGES={
"ready":"آماده",
"connect":"اتصال حساب",
"start":"شروع",
"pause":"مکث",
"resume":"ادامه",
"stop":"توقف",
"emergency_stop":"توقف اضطراری",
"paper":"حالت آزمایشی",
"shadow":"حالت سایه",
"risk":"ریسک",
"report":"گزارش",
"live_locked":"معامله واقعی هنوز قفل است",
}
def tr(key:str)->str:return MESSAGES.get(key,key)
