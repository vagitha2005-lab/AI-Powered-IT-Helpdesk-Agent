from pathlib import Path


KNOWLEDGE_BASE = (
    Path(__file__).parent.parent
    / "knowledge_base"
    / "troubleshooting.txt"
)


def load_knowledge_base():
    """Load the IT troubleshooting knowledge base."""
    try:
        return KNOWLEDGE_BASE.read_text(encoding="utf-8")
    except FileNotFoundError:
        return "Knowledge base file was not found."


def search_knowledge_base(problem):
    """Retrieve the most relevant troubleshooting section."""

    knowledge = load_knowledge_base()
    problem_lower = problem.lower()

    topics = [
        (
            ["wifi", "website", "websites", "internet"],
            "1. Company Websites Not Loading",
            "2. Development Laptop Running Slowly"
        ),
        (
            ["slow", "slowly", "performance", "memory"],
            "2. Development Laptop Running Slowly",
            "3. Development Application Not Responding"
        ),
        (
            ["application", "app", "software", "not responding"],
            "3. Development Application Not Responding",
            "4. Laptop Plugged In But Battery Not Charging"
        ),
        (
            ["battery", "charging", "charger"],
            "4. Laptop Plugged In But Battery Not Charging",
            None
        )
    ]

    for keywords, start_title, end_title in topics:

        if any(keyword in problem_lower for keyword in keywords):

            start = knowledge.find(start_title)

            if start != -1:

                if end_title:
                    end = knowledge.find(end_title, start)

                    if end != -1:
                        return knowledge[start:end]

                return knowledge[start:]

    return knowledge