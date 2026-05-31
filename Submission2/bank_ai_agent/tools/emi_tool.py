import re
import math


class EMITool:

    def extract_values(self, query):
        amounts = re.findall(r"\d+", query.replace(",", ""))

        if len(amounts) < 3:
            return None

        principal = float(amounts[0])
        annual_rate = float(amounts[1])
        tenure_months = int(amounts[2])

        return principal, annual_rate, tenure_months

    def calculate_emi(self, principal, annual_rate, tenure_months):
        monthly_rate = annual_rate / (12 * 100)

        emi = (
            principal
            * monthly_rate
            * math.pow(1 + monthly_rate, tenure_months)
        ) / (
            math.pow(1 + monthly_rate, tenure_months) - 1
        )

        return round(emi, 2)

    def run(self, query):
        extracted = self.extract_values(query)

        if not extracted:
            return (
                "Please provide principal amount, interest rate, "
                "and tenure in months.\n"
                "Example: Calculate EMI for 500000 at 8.5% for 60 months"
            )

        principal, annual_rate, tenure_months = extracted

        emi = self.calculate_emi(
            principal,
            annual_rate,
            tenure_months
        )

        return (
            f"Estimated monthly EMI: ₹{emi}\n"
            f"Principal: ₹{principal}\n"
            f"Interest Rate: {annual_rate}%\n"
            f"Tenure: {tenure_months} months"
        )