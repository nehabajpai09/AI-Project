
from core.agent import BankingAIAgent

TEST_QUERIES = [
    "What is a good credit score?",
    "My account was hacked",
    "Transfer money to another account"
]

for version in ["v1","v2","v3"]:
    print(f"\n===== {version.upper()} =====")
    agent = BankingAIAgent(prompt_version=version)
    for q in TEST_QUERIES:
        print("\nQ:", q)
        print(agent.handle_query(q))
