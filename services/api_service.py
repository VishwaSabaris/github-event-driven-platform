def validate_payload(data):
    """
    Validates incoming JSON payload.
    """

    if not data:
        return False, "Empty JSON body"

    required_fields = ["event", "repo", "time"]

    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"

    return True, "Valid payload"
