from datetime import UTC, datetime, timedelta


def get_datetime_after_week():
    return datetime.now(UTC) + timedelta(weeks=1)


def get_datetime_yesterday():
    return datetime.now(UTC) - timedelta(days=1)


def is_datetime_close_to(datatime1, datetime2):
    diff = datetime2 - datatime1
    return diff <= timedelta(seconds=1)
