PERSIAN_UI = {
    'app_name':'Tradeapp', 'connect_account':'اتصال حساب', 'market':'بازار', 'strategies':'استراتژی‌ها',
    'news':'اخبار بازار', 'risk':'مدیریت ریسک', 'backtest':'پس‌آزمایی', 'paper':'معاملات آزمایشی',
    'start':'شروع', 'stop':'توقف', 'pause':'مکث', 'resume':'ادامه', 'hold':'عدم معامله',
    'buy':'خرید', 'sell':'فروش', 'no_trade':'فعلاً معامله‌ای انجام نشد',
    'why':'چرا؟', 'confidence':'میزان اطمینان', 'session':'جلسه اجرا', 'pnl':'سود و زیان',
    'max_loss':'حداکثر زیان', 'exposure':'در معرض ریسک', 'emergency_stop':'توقف اضطراری',
    'paper_only':'فقط حالت آزمایشی', 'live_disabled':'معاملات واقعی فعلاً غیرفعال است',
    'account_connected':'حساب با موفقیت متصل شد', 'connection_failed':'اتصال به حساب ناموفق بود',
    'data_unavailable':'داده بازار در دسترس نیست', 'risk_blocked':'معامله به‌دلیل محدودیت ریسک رد شد',
    'news_impact':'اثر اخبار', 'strategy_agreement':'میزان توافق استراتژی‌ها'
}

def validate_persian_ui() -> None:
    bad = [k for k,v in PERSIAN_UI.items() if not isinstance(v,str) or not v.strip() or '\ufffd' in v]
    if bad: raise ValueError(f'invalid Persian UI entries: {bad}')
