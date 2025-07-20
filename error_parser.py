def extract_error_info(error_message):
    # Very basic parser stub; you'd expand this for better traceback parsing
    lines = error_message.strip().splitlines()
    return {"raw": error_message, "summary": lines[-1] if lines else ""}
