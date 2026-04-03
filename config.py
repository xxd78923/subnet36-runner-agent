AGENT_MAX_STEPS = 10
WEBSITE_HINTS = {}
TASK_PLAYBOOKS = {}
def detect_website(url): return url.split("/")[2] if url else ""
