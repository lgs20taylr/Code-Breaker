import random


def main():
    win = False
    codeLength = 4
    code, codeStr = generateCode(codeLength)
    for i in range(12):
        print(f"{12-i} guesses remaining.")
        guess = input("Enter a guess.")
        guess = list(guess)
        if checkGuess(guess, code, codeLength):
            print(f"Correct. The code was {str(code)}.")
            win = True
            break
    if not win:
        print(f"Game over. The code was: {code}")
    
    
    
def generateCode(digits):
    code = []
    for _ in range(digits):
        code.append(str(random.randint(0,9)))
    return code, "".join(code)

def checkGuess(guess, code, digits):
    correctDigits = 0
    for digit in range(len(guess)):
        if guess[digit] == code[digit]:
            correctDigits += 1
    if correctDigits == digits:
        return True
    else:
        print(f"Incorrect code entered. {correctDigits} correct digits.")
        return False


if __name__ == "__main__":
    main()