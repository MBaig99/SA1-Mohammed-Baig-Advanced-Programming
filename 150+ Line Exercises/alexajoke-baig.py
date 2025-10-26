# ========== Exercise 2 - Alexa tell me a Joke ========== #


import random

def load_jokes(filename):
    with open(filename, "r", encoding="utf-8") as file:
        jokes = [line.strip() for line in file if "?" in line]
    return jokes


def tell_joke(jokes):
    joke = random.choice(jokes)
    setup, punchline = joke.split("?", 1)
    print("\nAlexa:", setup + "?")
    input("\n(Press ENTER to hear the punchline)\n")
    print("Alexa:", punchline)
    
    
def main():
    jokes = load_jokes("jokes.txt")
    print("Type: Alexa tell me a Joke (or type Q to quit)\n")
    
    while True:
        command = input("You: ").strip()
        
        if command.lower() == "alexa tell me a joke":
            tell_joke(jokes)
            print("\nWould you like another joke? (y/n)")
            again = input("> ").strip().lower()
            if again != "y":
                print("\nAlexa: Goodbye!")
                break
        elif command.lower() == "q":
            print("\nAlexa: Goodbye!")
            break
        else:
            print("Alexa: I didn't understand. Try again.")

if __name__ == "__main__":
    main()
