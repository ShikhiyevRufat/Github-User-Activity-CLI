def parse_events(events):
    parsed = []

    for event in events:
        type_ = event.get("type")
        repo_name = event.get("repo", {}).get("name", "unknown repo")

        if type_ == "PushEvent":
            commit_count = len(event.get("payload", {}).get("commits", []))
            parsed.append(f"Pushed {commit_count} commits to {repo_name}")
        elif type_ == "IssuesEvent":
            action = event.get("payload", {}).get("action")
            parsed.append(f"{action.capitalize()} an issue in {repo_name}")
        elif type_ == "WatchEvent":
            parsed.append(f"Starred {repo_name}")
        elif type_ == "ForkEvent":
            parsed.append(f"Forked {repo_name}")
        else:
            parsed.append(f"{type_} on {repo_name}")

    return parsed
