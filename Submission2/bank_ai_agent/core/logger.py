# %%
import json
import re
import os

from datetime import datetime


class SafeLogger:

    def __init__(self):

        self.log_dir = "logs"
        self.log_file = os.path.join(
            self.log_dir,
            "agent_logs.json"
        )

        # Create logs directory if missing
        os.makedirs(self.log_dir, exist_ok=True)

        # Create empty log file if missing
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as file:
                file.write("")

    def sanitize(self, text):

        # Remove possible account numbers
        text = re.sub(
            r"\\b\\d{10,16}\\b",
            "[REDACTED_ACCOUNT]",
            text
        )

        # Remove emails
        text = re.sub(
            r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+",
            "[REDACTED_EMAIL]",
            text
        )

        return text

    def log(self, query, response):

        entry = {
            "timestamp": str(datetime.now()),
            "query": self.sanitize(query),
            "response": self.sanitize(response)
        }

        with open(self.log_file, "a") as file:
            file.write(json.dumps(entry))

