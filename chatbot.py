 #Function of predefined responses
def response(text):
    text = text.lower().strip()
    if "hello" in text or "hi" in text:
        return("Hello!")
    elif "how are you" in text or "what's up" in text:
        return("I'm fine,you?")
    elif "great" in text or "cool" in text:
        return("Cool. Good to see you")
    elif "bye" in text:
        return("Goodbye. See you soon!")
    else:
        return("I don't understand that.")

#User - Bot Conversation 
print("Tell me something...")
while True:
    user = input("You: ")
    reply = response(user)
    print("Bot: ", reply)
    if "bye" in user.lower():
        break