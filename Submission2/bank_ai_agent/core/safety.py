import re

class SafetyLayer:

    BLOCKED_PATTERNS = [
        "transfer money",
        "approve transaction",
        "send money",
        "bypass otp",
        "share customer data",
        "hack account",
        "close account legally",
        "legal advice"
    ]

    ESCALATION_PATTERNS = [
        "fraud",
        "account hacked",
        "unauthorized transaction",
        "identity theft",
        "suspicious activity"
    ]

    def check(self, query):
        query_lower = query.lower()

        # High-risk refusal
        for pattern in self.BLOCKED_PATTERNS:
            if pattern in query_lower:
                return {
                    "blocked": True,
                    "response": (
                        "I cannot assist with money movement, approvals, "
                        "legal advice, or unsafe banking actions. "
                        "Please contact your bank directly."
                    )
                }

        # Escalation detection
        for pattern in self.ESCALATION_PATTERNS:
            if pattern in query_lower:
                return {
                    "blocked": False,
                    "escalate": True
                }

        return {
            "blocked": False,
            "escalate": False
        }