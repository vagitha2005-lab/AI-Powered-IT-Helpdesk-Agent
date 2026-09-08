from agent import troubleshoot


def main():
    print("=" * 50)
    print("AI IT HELPDESK AGENT")
    print("=" * 50)

    problem = input("\nDescribe your IT problem: ")

    if not problem.strip():
        print("Please enter an IT problem.")
        return

    print("\nAnalyzing your problem...")
    print("Please wait...\n")

    result = troubleshoot(problem)

    print("TROUBLESHOOTING RESULT")
    print("-" * 50)
    print(result)


if __name__ == "__main__":
    main()