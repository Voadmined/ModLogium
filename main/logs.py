from datetime import datetime


def get_next_id(logs):
    if not logs:
        return "1"

    existing_ids = [int(log["id"]) for log in logs if "id" in log]

    if not existing_ids:
        return "1"

    return str(max(existing_ids) + 1)


def create_log_entry(log_id, username, userID, action, reason, moderator):

    log_entry = {
        "id": log_id,
        "username": username,
        "userID": userID,
        "action": action,
        "reason": reason,
        "moderator": moderator,
        "date": datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    }

    return log_entry


def search_logs(logs, query):
    if not query.strip():
        return logs
    lowquery = query.strip().lower()

    results = []
    
    for log in logs:
        if any(lowquery in str(value).lower() for value in log.values()):
            results.append(log)

    return results