# Group name MANIAC and members are: 
# 1. Ale Magar Ridam
# 2. Subedi Kushal
# 3. Shrestha Anish
# 4. Syangtan Sameer 
# 5. Arzimatova Muyassar
# Final project: Professor Assistant Program
# Our team is creating a professor assitant program that will help professors to create exams from a question bank which was provided by our professor.

# import the function that reads questions and answers 
# From the question_bank file and stores them as pairs
from question_bank import read_question_bank

# Import the function that creates an exam by randomly 
# Selecting questions from the question_bank and saving 
# Them to an output file
from exam_creator import create_exam

# Main function controls the overall flow of the program.
def main():
    """
    Main function that runs the Professor Assistant program.
    Handles user interaction and controls the exam creation workflow.
    """

    # Display welcome message to the professor when they start the program.
    print("Welcome to professor assistant version 1.0.")
    
    while True:
        # Ask the professor to enter their name so we can personalize the experience and make it more engaging.
        professor_name = input("Please Enter Your Name: ")

        # It removes any spaces from the professor's name and checks if the remaining characters are all letters using .isalpha() method.
        if professor_name.replace(" ", "").isalpha():
            break
        
        # Displays an error message if the name is invalid and prompts the professor to enter a valid name consisting of letters only.
        print ("Invalid name Try again. Please enter a valid name consisting of letters only: ")

       # Display personalized greeting using the professor's name.
    print(f"Hello Professor {professor_name}, I am here to help you create exams from a question_bank.txt file.")

    # Ask professor if they want to proceed with creating an exam?
    choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ")

    # Keep the program running as long as professor wants to create an exam.
    while choice.lower() == "yes":

        # Read the question_bank.txt file and store the question-asnwer pairs in a list.
        question_answers = read_question_bank("question_bank.txt")

        # If the file is missing or incorrectly formated then the function returns None.
        if question_answers is None:
            
            # Inform the professor that the file could not be used.
            print("Sorry Professor, the file is invalid or does not exist.")

        else:
            # Inform the professor that the question bank was successfully loaded.
            print("Yes, indeed the path you provided includes questions and answers.")

            # Ask the professor how many questions they want in the exam?
            total_questions = int(input("How many question-answer pairs do you want to include in your exam? "))

            # Ask where the professor wants to save the exam file?
            output_file = input("Where do you want to save your exam? ")

            # Create the exam with the specified number of questions the professor want.
            create_exam(question_answers, total_questions, output_file)

            # Display success message after the exam is creeated and saved.
            print(f"Congratulations Professor {professor_name}. ")
            print(f"Your exam is created and saved in {output_file}.")

        # Ask if the professor wants to create another exam.
        choice = input("Do you want me to help you create another exam (Yes to proceed | No to quit the program)? ")

    # Display farewell message when the professor exits the program.
    print("\n=========================================")
    print(f"Thank you professor {professor_name}, your exam has been created successfully.")                   
    print("Thank you professor for using our system, we hope it was helpful in creating your exam.")
    print("Have a wonderful day ahead!!")
    print("Professor assistant v1.0 is now signing off ") 
    print("=========================================")


# Start the program by calling the main function.
# Checks if this python file is being run directly as the main program. 
# If it is, it executes the main function to start the program.
if __name__ == "__main__":
    main()