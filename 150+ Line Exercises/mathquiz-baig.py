import random


# ------------- Main Difficulty Levels and Functions -----------------

def displayMenu() -> int:
    # This part shows the difficulty level options and validates what the user inputs

    print("\nDIFFICULT LEVEL")
    print(" 1. Easy")
    print(" 2. Medium")
    print(" 3. Advanced")

    while True:
        choice = input("Choose (1-3): ").strip()
        if choice in {"1", "2", "3"}:
            return int(choice)
        print("ivalid Choice. Enter 1, 2, or 3.")

def randomInt(level: int) -> int:
    # based on Difficulty level, random numbers will be generated within range of level difficulty
    # Easy -> 1-digit (1..9)
    # Medium -> 2-digit (10..99)
    # Advanced -> 3-digit (1000..9999)

    if level == 1:
        lo, hi = 1,9
    elif level == 2:
        lo, hi = 10,99
    else:
        lo, hi = 1000,9999
    return random.randint(lo,hi)

def decideOperation() -> str:
    # This basically generates + or - for any question
    return random.choice(['+', '-'])


def displayProblem(a: int, b: int, op: str) -> int:
    # It will show the arithmetic question and receive a valid integer input from the user
    while True:
        ans = input(f"{a} {op} {b} = ").strip()
        try:
            return int(ans)
        except ValueError:
            print("Enter a valid integer!")

def _correct_value(a: int, b: int, op: str) -> int:
    # Compute the correct answer for the question
    return a + b if op == '+' else a - b


def isCorrect(a: int, b: int, op: str, user_ans: int, attempt: int) -> bool:
    # It will compare the answer with user input and give feedback
    correct = _correct_value(a, b, op)
    if user_ans == correct:
        if attempt == 1:
          print("Amazing! Correct on first try! (+10)")
        else: 
          print("Good! Correct on second try! (+5)")
        return True
    else:
        if attempt == 1:
            print("Thats not it! Try again!")
        else:
            print(f"Wrong again! Correct answer was {correct} ")
        return False

def displayResults(score: int)-> None:
    # Now here you will see final score, converted to grading system with a small note of confidence :p
    print("\n--------Results-------")
    print(f"Final Score: {score} / 100")


    # Grade based on the score user got

    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    print(f"Rank: {grade}")

    # Small line of confidence based on the grade user gets
    if grade in ("A+" , "A"):
        note = "Excellent work, Keep going!"
    elif grade in ("B" , "C"):
        note = "Good, Try for fewer attempts!"
    else: 
        note = "Practice more often"
    print(note)
    
# ---------------------------- Quiz Engine -------------------------------

def play_quiz():
    # Starts 1 full quiz attempt with 10 questions based on chosen difficulty
    level = displayMenu()
    total_score = 0
    QUESTIONS = 10

    print("\nAnwer each question, You get 2 attempts per question.")
    print("Important Note: The Difficulty you choose controls the number sizes; substraction questions can have negative answers.")


    for i in range(1, QUESTIONS + 1):
        # This generates random questions with random operations based on difficulty
        a = randomInt(level)
        b = randomInt(level)
        op = decideOperation()

        print(f"\nQuestion {i}/{QUESTIONS}")

        # First attempt at the question
        ans1 = displayProblem(a, b, op)
        if isCorrect(a, b, op, ans1, attempt=1):
            total_score += 10
            continue

        # Second attempt at the same problem
        ans2 = displayProblem(a, b, op)
        if isCorrect(a, b, op, ans2, attempt=2):
            total_score += 5

        # End of quiz attempt : show results summary

    displayResults(total_score)

def ask_Replay() -> bool:
    # Here the user is asked to play again or not
    while True:
        again = input("Play again? (y/n): ").strip().lower()
        if again in ("y", "yes"):
            return True
        if again in ("n", "no"):
            return False
        print("Enter 'y or 'n'.")

def main():
    # This part basically loops the quizzes until the user quits
    print("----MATHS QUIZ----")
    while True:
        play_quiz()
        if not ask_Replay():
            print("Quiz ended. Thank you for playing.")
            break
if __name__ == "__main__":
    main()

             




    

