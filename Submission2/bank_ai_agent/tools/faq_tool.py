import json


class FAQTool:

    def __init__(self):
        self.faqs = {
            "what is a savings account":
                "A savings account allows customers to deposit money securely while earning limited interest.",

            "what is kyc":
                "KYC stands for Know Your Customer. Banks use KYC verification to confirm customer identity.",

            "what is minimum due":
                "Minimum due is the minimum amount a credit card holder must pay to avoid penalties.",

            "what is a fixed deposit":
                "A fixed deposit is a banking investment product that provides fixed returns over a specified period.",

            "what is a credit score":
                "A credit score represents a customer's creditworthiness based on repayment history and financial behavior."
        }

    def run(self, query):
        normalized_query = query.lower().strip()

        for faq, answer in self.faqs.items():
            if faq in normalized_query:
                return answer

        return None