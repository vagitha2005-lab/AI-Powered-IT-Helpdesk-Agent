from langchain_ollama import ChatOllama

from rag import search_knowledge_base
from tools import (
    check_internet_connection,
    get_network_information,
    ping_test
)


llm = ChatOllama(
    model="tinyllama",
    temperature=0
)


def troubleshoot(problem):
    """Analyze an IT problem and provide troubleshooting guidance."""

    knowledge = search_knowledge_base(problem)

    problem_lower = problem.lower()

    # Use diagnostic tools mainly for network-related problems
    if any(word in problem_lower for word in
           ["wifi", "internet", "website", "network", "connection"]):

        internet_status = check_internet_connection()
        ping_status = ping_test()

        tool_results = (
            f"Internet Status: {internet_status}\n"
            f"Ping Test: {ping_status}"
        )

    else:
        tool_results = "Network diagnostic tools were not required."

    # Ask the local LLM for a short analysis
    prompt = f"""
You are an IT Helpdesk Agent.

Problem: {problem}

Relevant troubleshooting information:
{knowledge}

Diagnostic information:
{tool_results}

Give a short professional troubleshooting response.
Mention the likely causes and useful steps.
Do not repeat the prompt or instructions.
"""

    try:
        response = llm.invoke(prompt)
        ai_response = response.content.strip()

    except Exception:
        ai_response = ""

    # Reliable final response from the retrieved knowledge
    result = f"""
AI IT HELPDESK AGENT
{'=' * 50}

Problem:
{problem}

Relevant Knowledge Retrieved:
{knowledge.strip()}

Diagnostic Results:
{tool_results}

AI Analysis:
{ai_response if ai_response else "The problem was matched with the relevant troubleshooting knowledge base."}

Final Recommendation:
Follow the recommended troubleshooting steps above. If the problem continues,
contact the appropriate technical support team.
"""

    return result
