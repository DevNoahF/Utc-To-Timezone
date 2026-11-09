from datetime import datetime
from zoneinfo import ZoneInfo


class ConvertToUserTimezoneMiddleware:
    def convert_to_user_timezone(self, datetime_str: str, timezone: str) -> str:
        utc_time = datetime.fromisoformat(datetime_str)
        converted_time = utc_time.astimezone(ZoneInfo(timezone))
        return converted_time.isoformat()