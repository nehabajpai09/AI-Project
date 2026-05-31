class IntentRouter:

    def route(self, query):
        query = query.lower()

        emi_keywords = [
            "emi",
            "loan payment",
            "monthly installment",
            "interest rate"
        ]

        fraud_keywords = [
            "fraud",
            "hacked",
            "unauthorized",
            "stolen"
        ]

        for word in emi_keywords:
            if word in query:
                return "emi"

        for word in fraud_keywords:
            if word in query:
                return "fraud"

        return "rag"