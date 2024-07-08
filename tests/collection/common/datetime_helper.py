from datetime import datetime, UTC, timedelta


def get_datetime_after_week():
    return datetime.now(UTC) + timedelta(weeks=1)
