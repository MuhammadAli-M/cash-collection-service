from datetime import UTC, datetime, timedelta


def get_datetime_after_week():
    return datetime.now(UTC) + timedelta(weeks=1)
