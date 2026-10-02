from tradeapp.adapters.base import TradingAdapter

class AdapterRegistry:
    def __init__(self) -> None:
        self._adapters: dict[str, TradingAdapter] = {}
    def register(self, adapter: TradingAdapter) -> None:
        key = adapter.name.strip().lower()
        if not key:
            raise ValueError("adapter name cannot be empty")
        if key in self._adapters:
            raise ValueError(f"adapter already registered: {key}")
        self._adapters[key] = adapter
    def get(self, name: str) -> TradingAdapter:
        try:
            return self._adapters[name.strip().lower()]
        except KeyError as exc:
            raise KeyError(f"unknown adapter: {name}") from exc
    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._adapters))
