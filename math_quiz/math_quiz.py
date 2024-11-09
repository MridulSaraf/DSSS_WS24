import random


def randomIntGenerator(min, max):
    """
    Generate a random integer between specified min and max values.

    Parameters:
    min(int): Minimum integer value.
    max(int): Maximum integer value.

    Returns:
    int: Random integer between min and max.
    """
    return random.randint(min, max)


def randomOperatorGenerator():

    """
    Generate a random operator among the below specified operators.

    Returns:
    str: A random operator
    """
    return random.choice(['+', '-', '*'])


def randomProblemGenerator(num1, num2, operator):
    """
    Create a math problem and calculate the correct answer based on the operator.

    Parameters:
    num1(int): First number
    num2(int): Second number
    operator(str): Operator among '+', '-', or '*'

    Returns:
    tuple: A tuple containing the problem and the correct answer.
    """

    # Depending on the operator, solve the problem
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-3':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
    """
    A math quiz game that asks the user random math questions and provides their score as ouput.

    """

    points = 0
    total_questions = 3 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):

        # Generate random number and operator
        num1 = randomIntGenerator(1, 10)
        num2 = randomIntGenerator(1, 52)
        operator = randomOperatorGenerator()
        # Generate the problem
        PROBLEM, ANSWER = randomProblemGenerator(num1, num2, operator)
        print(f"\nQuestion: {PROBLEM}")
        
        # Get a valid user input
        try:

            useranswer = int(input("Your answer: "))
            
            #Check if correct answer
            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                points += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
        except ValueError:
            print("Invalid input. Please enter an integer")


    print(f"\nGame over! Your score is: {points}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
