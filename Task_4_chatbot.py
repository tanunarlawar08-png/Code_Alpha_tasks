def chatbot():
    print("Hello I'm your chatbot Alex.")
    print("text bye to end this conversation.\n")
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("Hii!")
        elif user_input == "how are you":
            print("I'm fine, Thankyou!")
        elif user_input == "what is your name":
            print("My name is Alex")
        elif user_input == "name the coding language that is used":
            print("I'm made from Python language")
        elif user_input == "what can you do":
            print("I can answer simple questions and have a basic conversation with you!")
        elif user_input == "who created you":
            print("I was created by a Python developer as an internship project!")
        elif user_input == "what is today":
            print("Sorry, I don't have access to real-time data, but you can check your device!")
        elif user_input == "tell me a joke":
            print("Why do programmers prefer dark mode? Because light attracts bugs! ")
        elif user_input == "what is python":
            print("Python is a popular, beginner-friendly programming language used in web development, AI, and more!")

        elif user_input == "bye":
            print("Goodbye!")
            break                  
        else:
            print("Sorry I don't understand what you are saying")

chatbot()
