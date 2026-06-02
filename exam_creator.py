# importing the random module to use for selecting random questions from the question bank.
import random

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