from core.agent import BankingAIAgent

def main():
    agent = BankingAIAgent()

    print("\n=== AI Banking Support & Advisory Agent ===")
    print("Type 'exit' to quit.\n")

    while True:
        user_query = input("User: ")

        if user_query.lower() == "exit":
            break

        response = agent.handle_query(user_query)
        print(f"\nAgent: {response}\n")

if __name__ == "__main__":
    main()