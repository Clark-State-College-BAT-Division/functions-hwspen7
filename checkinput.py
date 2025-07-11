#Write a function that takes two parameters: a prompt message and an error message.
#The function will prompt the user with the passed in prompt to enter an integer
#If the text entered cannot be cast to an int, display the error message.
#The function will continue to prompt the user to enter an integer until a proper integer is entered.
#The most direct way of doing this would be using a try block, which has not been covered yet. You will need to research this.
#Write supporting code to call the function, and then display the number that was entered.

def get_integer(prompt_message, error_message):
    while True:
        user_input = input(prompt_message)
        try:
            number = int(user_input)
            return number
        except ValueError:
            print(error_message)

number_entered = get_integer("Please enter an integer: ", "That's not a valid integer, try again!")
print("You entered: ", number_entered)