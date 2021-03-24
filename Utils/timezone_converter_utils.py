def convert_timestamp_with_coordinates(lat, lng, timestamp):
    """
    default regard timestamp as UTC timezone and convert it to its local timezone which get from coords (lat and lng)
    return string format dd/mm/yyyy hh:mm Z +/-hhmm
    """
    from datetime import datetime
    from timezonefinder import TimezoneFinder
    from pytz import timezone

    tf = TimezoneFinder()

    # From the lat/long, get the tz-database-style time zone name (e.g. 'America/Vancouver') or None
    timezone_str = tf.certain_timezone_at(lat=lat, lng=lng)
    timezone = timezone(timezone_str)

    fmt = '%d/%m/%Y %H:%M %Z %z'

    time = datetime.fromtimestamp(timestamp).astimezone(timezone).strftime(fmt)

    return time
