# Threat detection logic

def analyze_log(log):

    if "LOGIN FAILED" in log:
        return "[ALERT] Failed login attempt detected"

    if "LOGIN SUCCESS - admin" in log:
        return "[ALERT] Admin login detected"

    if "confidential" in log:
        return "[ALERT] Sensitive file accessed"

    return None
