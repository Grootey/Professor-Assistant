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
