from decimal import Decimal
from tradeapp.backtest.metrics import calculate_metrics
from tradeapp.backtest.costs import ExecutionCostModel
from tradeapp.portfolio.exposure import PortfolioSnapshot,PositionExposure
from tradeapp.safety.circuit_breaker import CircuitBreaker
from tradeapp.i18n import PERSIAN_UI,validate_persian_ui

def test_metrics():
    m=calculate_metrics(Decimal('100'),Decimal('110'),[Decimal('100'),Decimal('90'),Decimal('110')],2,1,Decimal('20'),Decimal('10'))
    assert m.total_return==Decimal('.1') and m.max_drawdown==Decimal('.1') and m.win_rate==Decimal('2')/Decimal('3')

def test_cost_model():
    c=ExecutionCostModel(); assert c.buy_price(Decimal('100'))>Decimal('100') and c.fee(Decimal('100'))==Decimal('.1')

def test_portfolio_concentration():
    p=PortfolioSnapshot(Decimal('100'),(PositionExposure('BTC',Decimal('70'),Decimal('.7')),),Decimal('.3')); assert p.concentration()==Decimal('.7')

def test_circuit_breaker():
    c=CircuitBreaker(); c.trip('market anomaly'); assert not c.permits_trading(); c.reset(); assert c.permits_trading()

def test_persian_ui():
    validate_persian_ui(); assert PERSIAN_UI['no_trade']=='فعلاً معامله‌ای انجام نشد'
