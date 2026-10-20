import json
import re
import sys

INTENT_RESPONSES = {
    "greeting": [
        "Hello! Welcome to Datheon Support. How can I help you today?",
        "Hi there! How can I assist you with our services?",
    ],
    "business_hours": [
        "Our business hours are Monday to Friday, 9:00 AM to 5:00 PM EST.",
        "We are open weekdays from 9 AM to 5 PM. We are closed on weekends.",
    ],
    "product_faqs": [
        "Datheon offers industry-modeled project engineering internships to build your portfolio.",
        "Our certificates feature a verifiable QR code issued upon successful project evaluation.",
    ],
    "exit": [
        "Goodbye! Thank you for using Datheon Assistant.",
        "See you next time! Have a great day.",
    ],
}

INTENT_PATTERNS = {
    "greeting": re.compile(r"\b(hi|hello|hey|greetings|good\s+morning|sup)\b"),
    "business_hours": re.compile(
        r"\b(hours|open|close|time|timing|weekdays|schedule)\b"
    ),
    "product_faqs": re.compile(
        r"\b(faq|product|internship|certificate|program|cost|fee)\b"
    ),
    "exit": re.compile(r"\b(bye|exit|quit)\b"),
}


def load_sample_faq(filepath=None):
    """Optional loader for external JSON dataset if available."""
    if filepath:
        try:
            with open(filepath, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(
                f"[System Warning] FAQ file '{filepath}' not found. Using internal fallback rules."
            )
    return INTENT_RESPONSES


def get_intent(user_input):
    """Matches the preprocessed user input against regex patterns to detect intent."""
    for intent, pattern in INTENT_PATTERNS.items():
        if pattern.search(user_input):
            return intent
    return "unknown"


def main():
    # Load responses (uses internal dictionary by default)
    responses = load_sample_faq()

    print("==================================================")
    print("      Datheon Interactive Terminal Assistant       ")
    print("==================================================")
    print("Type your query below. Type 'bye', 'exit', or 'quit' to leave.\n")

    # Initialize conversational state tracking if needed
    is_active = True

    while is_active:
        try:
            # Capture user input
            raw_input = input("You: ")

            # 3. Normalize user input (lowercase, strip whitespace)
            clean_input = raw_input.lower().strip()

            # Skip empty inputs smoothly
            if not clean_input:
                continue

            # 4. Intent classification using regex keyword extraction
            intent = get_intent(clean_input)

            # 5. Conversational state management & resolution
            if intent == "exit":
                print(f"Bot: {responses['exit'][0]}")
                is_active = False

            elif intent == "greeting":
                print(f"Bot: {responses['greeting'][0]}")

            elif intent == "business_hours":
                print(f"Bot: {responses['business_hours'][0]}")

            elif intent == "product_faqs":
                print(f"Bot: {responses['product_faqs'][0]}")

            else:
                # Provide graceful fallbacks when query confidence is low
                print(
                    "Bot: I'm sorry, I didn't quite catch that. Could you rephrase your question regarding our business hours, product FAQs, or programs?"
                )

            print()  # Spacer line for clean terminal UI

        except (KeyboardInterrupt, EOFError):
            # Clean exit handling on terminal interrupt signals (Ctrl+C, Ctrl+D)
            print(f"\nBot: {responses['exit'][1]}")
            sys.exit(0)


if __name__ == "__main__":
    main()