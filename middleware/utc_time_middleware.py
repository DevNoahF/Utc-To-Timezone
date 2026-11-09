from datetime import datetime, timezone

def utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()