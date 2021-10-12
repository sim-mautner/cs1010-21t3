# import libraries (if you have them)

# define constants (if you have them)
START_LOW = 1
START_HIGH = 100

# other functions you write (if you have them)

def main():
    print("Choose a number between 1 and 100.")

    low = START_HIGH
    high = START_LOW

    guess = int((low + high)/2)

    print(f"Is your number {guess}?")
    response = input("Enter H, L or C: ")

    while response != 'C': # != means "not equal to" --> while not response == 'C':
        # If need to go lower, make high = guess - 1
        if response == 'L':
            high = guess - 1
        elif response == 'H':
            # lowest possible number is guess + 1
            low = guess + 1

        guess = int((low + high)/2)

        print(f"Is your number {guess}?")
        response = input("Enter H, L or C: ")

if __name__ == '__main__':
    main()



