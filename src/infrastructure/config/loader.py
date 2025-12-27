from logging import raiseExceptions
from pathlib import Path
from datetime import time
import yaml

from infrastructure.config.schema import TradingPolicyConfig, DEFAULT_TRADING_POLICY
from infrastructure.config.errors import ConfigError

PROJECT_ROOT = Path(__file__).resolve().parents[3]

def _parse_time(val: str) -> time:
    try:
        h, m = val.split(":")
        return time(int(h), int(m))
    except Exception:
        raise ConfigError(f"Invalid time format (HH:MM expected): {val}")

def load_trading_policy_config() -> TradingPolicyConfig:
    cfg_path = PROJECT_ROOT / "config/config.yaml"
    if not cfg_path.exists():
        raise Exception("YAML Config Not Found: ", PROJECT_ROOT)
        #return DEFAULT_TRADING_POLICY

    data = yaml.safe_load(cfg_path.read_text()) or {}
    tp = data.get("trading_policy", {})

    start = _parse_time(tp.get("entry_window_start", "09:30"))
    end = _parse_time(tp.get("entry_window_end", "11:00"))
    close = _parse_time(tp.get("force_close_time", "15:15"))

    if not (start < end < close):
        raise ConfigError(
            "Invalid trading_policy ordering: entry_window_start < entry_window_end < force_close_time required"
        )

    return TradingPolicyConfig(
        entry_window_start=start,
        entry_window_end=end,
        force_close_time=close,
    )
