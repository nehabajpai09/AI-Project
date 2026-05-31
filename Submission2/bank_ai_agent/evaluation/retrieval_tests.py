# %%
from tools.rag_tool import RAGTool


rag = RAGTool()


TESTS = [
    {
        "query": "What affects home loan EMI?",
        "expected": "principal amount"
    },
    {
        "query": "Should I share OTP?",
        "expected": "never share OTP"
    },
    {
        "query": "What is a good credit score?",
        "expected": "750"
    }
]


correct = 0

for test in TESTS:

    response = rag.run(test["query"])

    if test["expected"].lower() in response.lower():
        correct += 1

accuracy = correct / len(TESTS)

print(f"Retrieval Accuracy: {accuracy * 100}%")

