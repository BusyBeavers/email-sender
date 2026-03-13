from datetime import datetime, timezone
 
 
def is_future_datetime(dt: datetime) -> bool:
    """Returns True if the given datetime is in the future."""
    now = datetime.now(tz=timezone.utc)
 
    # Make dt timezone-aware if it isn't already
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
 
    return dt > now