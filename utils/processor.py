from datetime import datetime


def classify_activity(time_value):
    """
    Classifies activity based on UTC hour.
    Late Activity = 22:00 UTC or later.
    """

    if not time_value:
        return {
            "parsed_hour": None,
            "status": "Unknown Activity"
        }

    try:
        parsed_time = datetime.fromisoformat(time_value.replace("Z", "+00:00"))
        hour = parsed_time.hour

        status = "Late Activity" if hour >= 22 else "Normal Activity"

        return {
            "parsed_hour": hour,
            "status": status
        }

    except Exception:
        return {
            "parsed_hour": None,
            "status": "Invalid Time Format"
        }


def process_event(data):
    """
    Processes incoming event data.
    """

    event = data.get("event", "unknown")
    repo = data.get("repo", "unknown")
    time_value = data.get("time")

    activity = classify_activity(time_value)

    return {
        "event": event,
        "repo": repo,
        "time": time_value,
        "parsedHour": activity["parsed_hour"],
        "status": activity["status"]
    }
