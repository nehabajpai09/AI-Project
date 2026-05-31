from core.safety import SafetyLayer
from core.router import IntentRouter
from core.logger import SafeLogger
from tools.emi_tool import EMITool
from tools.rag_tool import RAGTool
from tools.escalation_tool import EscalationTool


class BankingAIAgent:

    def __init__(self):
        self.safety = SafetyLayer()
        self.router = IntentRouter()
        self.logger = SafeLogger()
        self.emi_tool = EMITool()
        self.rag_tool = RAGTool()
        self.escalation_tool = EscalationTool()

    def handle_query(self, query):
        # Step 1: Safety validation
        safety_result = self.safety.check(query)

        if safety_result["blocked"]:
            self.logger.log(query, safety_result["response"])
            return safety_result["response"]

        # Step 2: Route intent
        intent = self.router.route(query)

        # Step 3: Tool execution
        if intent == "emi":
            response = self.emi_tool.run(query)

        elif intent == "fraud":
            response = self.escalation_tool.run(query)

        else:
            response = self.rag_tool.run(query)

        # Step 4: Safe logging
        self.logger.log(query, response)

        return response
