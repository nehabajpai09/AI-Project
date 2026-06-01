
from core.safety import SafetyLayer
from core.router import IntentRouter
from core.logger import SafeLogger
from core.llm_client import LLMClient
from core.prompts import AgentPrompts
from tools.emi_tool import EMITool
from tools.rag_tool import RAGTool
from tools.escalation_tool import EscalationTool

class BankingAIAgent:
    def __init__(self, prompt_version="v3"):
        self.safety = SafetyLayer()
        self.router = IntentRouter()
        self.logger = SafeLogger()
        self.llm = LLMClient()
        self.prompt_version = prompt_version
        self.emi_tool = EMITool()
        self.rag_tool = RAGTool()
        self.escalation_tool = EscalationTool()

    def _prompt(self):
        return {
            "v1": AgentPrompts.SYSTEM_PROMPT_V1,
            "v2": AgentPrompts.SYSTEM_PROMPT_V2,
            "v3": AgentPrompts.SYSTEM_PROMPT_V3,
        }.get(self.prompt_version, AgentPrompts.DEFAULT_PROMPT)

    def handle_query(self, query):
        safety_result = self.safety.check(query)
        if safety_result["blocked"]:
            return safety_result["response"]

        intent = self.router.route(query)

        if intent == "emi":
            response = self.emi_tool.run(query)
        elif intent == "fraud":
            response = self.escalation_tool.run(query)
        else:
            context = self.rag_tool.run(query)
            response = self.llm.generate(self._prompt(), query, context)

        self.logger.log(query, response)
        return response
