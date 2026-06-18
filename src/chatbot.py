# Core chatbot logic

from src.responses import RESPONSES, DEFAULT_RESPONSE

def get_response(user_input):
    cleaned_input = user_input.lower().strip()
    for key in RESPONSES:
        if key in cleaned_input:
            return RESPONSES[key]
    return DEFAULT_RESPONSE

def start_chat():
    print("=" * 40)
    print("   Welcome to ByteBot 🤖")
    print("   Type 'bye' to exit")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ")
        if user_input.lower().strip() == "bye":
            print("ByteBot: Goodbye! Have an awesome day 👋")
            break
        response = get_response(user_input)
        print(f"ByteBot: {response}")
