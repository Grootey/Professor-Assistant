# Group name MANIAC and members are: 
# 1. Ale Magar Ridam
# 2. Subedi Kushal
# 3. Shrestha Anish
# 4. Syangtan Sameer 
# 5. Arzimatova Muyassar
# Final project: Professor Assistant Program
# Our team is creating a professor assitant program that will help professors to create exams from a question bank which was provided by our professor.

# importing the random module to use for selecting random questions from the question bank.
import random


# We created the Function to read question bank from a file question_bank.txt and return a list of question-answers pairs.
def read_question_bank(question_bank):
    """
    Reads a question bank file and returns a list of (question, answer) tuples.
    
    Args:
        question_bank (str): The filename of the question bank
        
    Returns:
        list: List of (question, answer) tuples, or None if file is invalid
    """

    try:
        # Infile basically opens the question bank file in read mode
        infile = open(question_bank, "r")

        # Now we are reading all lines from the file and storing them in a list called lines.
        lines = infile.readlines()

        # closing the file after reading
        infile.close()

        # If the file is empty, we return none to indicate that there are no questions to process.
        if not lines:
            return None

        cleaned_lines = []

        # Now, process each line from the question bank one at a time.
        # The purpose of creating this loop is to prepare the data for creating question-answer pairs by cleaning every line before it is stored.
        for line in lines:
            # The strip() method Remove leading/trailing whitespace from the line
            # as the newline character at the end of each line can cause issues when creating question-answer pairs,
            # so we use strip() to esure that we are working with clean data without extra spaces or newlines.
            line = line.strip()

            # Keep only non-empty lines and ignore blank lines in the question bank.
            if line != "":
                cleaned_lines.append(line)

        # verifying that every questions has a corresponding answer since, questions and answers come in pairs.
        # Questions and answers should come in pairs, so total lines must be even. If not thent he file format will be incorrect.
        if len(cleaned_lines) % 2 != 0:
            return None

        # Create an empty list that will store question-answer pairs
        # extracted from question_bank.txt 
        question_answers = []

        # Loop through cleaned lines in steps of 2 (one question + one answer)
        # The first line represents the question and the second line represents the answer.
        for i in range(0, len(cleaned_lines), 2):

            # Rewrite the question from the current position in the list.
            question = cleaned_lines[i]
            
            # Retrive the answer immediately that follows the question.
            answer = cleaned_lines[i + 1]

            # Store the question-answer pair as a tuple so they can be accessed later as a single pair.
            question_answers.append((question, answer))

        # Return the list of question-answer pairs
        # This data is used to generate the exam later in the program, so we need to return it to the main function.
        return question_answers

    # If the question bank file cannot be found then it will return none
    # so, the program can display an error message instead of crashing.
    except FileNotFoundError:
        return None


# Function to create an exam by randomly selecting questions
def create_exam(question_answers, total_questions, output_file):
    """
    Creates an exam by randomly selecting questions and saves it to a file.
    
    Args:
        question_answers (list): List of (question, answer) tuples
        total_questions (int): Number of questions to include in the exam
        output_file (str): The filename where the exam will be saved
    """

    # Open the output file in write mode
    # If the file does not exist it will be created 
    # If it already exists then its old contents will be overwritten.
    outfile = open(output_file, "w")

    # Create a empty list to track which questions have already been used
    used_indexes = []

    # Count total number of available questions which is in the question_bank.txt file.
    available_questions = len(question_answers)

    # Prevent requesting more questions than are available in the question bank
    # If the professor requests more questions than exist in the question bank then use the maximum available insted.
    if total_questions > available_questions:
        total_questions = available_questions

    # Loop to create the specified number of questions for the exam
    # Repeat the process until the required number of question has been added to the exam.
    for number in range(total_questions):

        # Generate a random index between 0 and the number of available questions.
        random_index = random.randint(0, available_questions - 1)

        # Avoid duplicate questions it keeps generating random indexes until we get a new one
        # Checks whether this question has already been selected or not.
        # If yes then it keep generating a new random index until a different question is found.
        while random_index in used_indexes:
            random_index = random.randint(0, available_questions - 1)

        # Save the selected index so it cannot be selected again.
        # This allows the program to track which questions have already 
        # been used and prevents duplicate question in the exam.
        used_indexes.append(random_index)

        # Retrieve the question and answer from the question bank
        # Which is stored at randomly selected position
        question = question_answers[random_index][0]
        answer = question_answers[random_index][1]

        # Write the question to the output file (question number starts from 1)
        # number + 1 is used because numbering starts at 1 not at 0.
        outfile.write(f"Question {number + 1}: {question}\n")
        
        # Write the answer to the output file.
        # Two newline characters create a blank line between pairs.
        outfile.write(f"Answer: {answer}\n\n")

    # Close the output file after writing all questions and answers
    outfile.close()


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