import google.generativeai as genai

API_KEY = "YOUR-API-KEY"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat()

print("Chat with Gemini! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    try:
        response = chat.send_message(user_input)
        print("Gemini:", response.text)
    except Exception as e:
        print("Error:", e)
