def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Hello, what is your name?")

    # Prompt the user for their scores in Math, Science, and English
    # Turned string inputs into integers
    math_score = int(input("What is your math score?"))
    science_score = int(input("What is your science score?"))
    english_score = int(input("What is your english score?"))
    
    # Added math_score, science_score, english_score variables
    # Then divided them by 3 to calculate average grade
    average_grade = (math_score + science_score + english_score) / 3
    
    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"{student_name}'s average grade is {average_grade}")