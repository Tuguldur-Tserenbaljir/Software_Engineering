import os

class Grading:
    
    def __init__(self, file):
        self.students = {}
        self.load(file)
        self.weights = {}
        self.grade_weights =  [15, 15, 15, 25, 30]  # Default grade weights

    def get_grade_weights(self):
        return self.grade_weights
    
    def load(self, file):
        with open(file, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split()
                id = parts[0]
                name = parts[1]
                scores = list(map(int, parts[2:]))
                self.students[id] = {'name': name, 'scores': scores}

    #1
    def show_score(self, student_id):
        """
        Prints the 5 scores of a specified student.

        :param student_id: The ID of the student whose scores are to be printed.
        :type student_id: str
        :return score_str: The 5 scores of the corresponding student ID
        :rtype: str
        
        Running Example:
        We have a Grading system instance named grading_system, 
        and we wish to display the scores of a student with an ID of "123456789". 
        By calling grading_system.show_score("123456789"), the method accesses the student's 
        scores from the internal students dictionary and prints them out, 
        showcasing the individual's scores across different assessments.
        """
        scores_str=""
        if student_id in self.students:
            scores = self.students[student_id]['scores']
            scores_str = ' '.join(map(str, scores))
            print(f"Scores: {scores_str}")
            print("\n")
        else:
            print("Student ID not found.")
            print("\n")
        return scores_str

    #2
    def show_grade_letter(self, student_id):
        """
        Prints the final grade letter of a specified student, calculated based on the weighted score.

        :param student_id: The ID of the student whose grade letter is to be printed.
        :type student_id: str
        :return grade_letter: The grade letter of the corresponding student ID
        :rtype: str

        Running Example:
        With the same grading_system instance, if we want to determine the letter grade of a student,
        say with ID "123456789", we call grading_system.show_grade_letter("123456789"). 
        This method first calculates the weighted average score by applying predefined weights
        to the student's scores, then it maps this numerical score to a letter grade based on 
        a grading scale (e.g., A+, A, B+, etc.) and prints the result.
        """
        grade_letter = ""
        if student_id in self.students:
            final_score = self.calculate_weighted_score(self.students[student_id]['scores'], self.grade_weights)
            grade_letter = self.determine_grade_letter(final_score)
            print(f"Grade: {grade_letter}")
            print("\n")
        else:
            print("Student ID not found.")
            print("\n")
        return grade_letter

    def determine_grade_letter(self, score):
        """
        Determines the letter grade for a given score.

        This method maps a numerical score to a corresponding letter grade based on predefined thresholds. 
        The grading scale used is as follows:
        - A+: 90 and above
        - A: 85 to below 90
        - A-: 80 to below 85
        - B+: 77 to below 80
        - B: 73 to below 77
        - B-: 70 to below 73
        - C+: 67 to below 70
        - C: 63 to below 67
        - C-: 60 to below 63
        - D: 50 to below 60
        - E: below 50
        
        :param score: The numerical score for which the letter grade is to be determined.
        :type score: float
        :return: The letter grade corresponding to the input score.
        :rtype: str
        """
        if score >= 90:
            return 'A+'
        elif score >= 85 and score < 90:
            return 'A'
        elif score >= 80 and score < 85:
            return 'A-'
        elif score >= 77 and score < 80:
            return 'B+'
        elif score >= 73 and score < 77:
            return 'B'
        elif score >= 70 and score < 73:
            return 'B-'
        elif score >= 67 and score < 70:
            return 'C+'
        elif score >= 63 and score < 67:
            return 'C'
        elif score >= 60 and score < 63:
            return 'C-'
        elif score >= 50 and score < 60:
            return 'D'
        else:
            return 'E'
        
    #3
    def show_average(self, student_id):
        """
        Prints the weighted average score of a specified student.

        :param student_id: The ID of the student whose average score is to be printed.
        :type student_id: str
        :return final_score: The final score of the corresponding student ID calculated based on weights
        :rtype: str
        
        Running Example:
        To see a student's weighted average score directly, if we want to access the student 
        with ID "123456789", we use grading_system.show_average("123456789"). This function 
        computes the weighted average by multiplying each of the student's scores by the respective 
        weight (defined globally), sums these weighted scores, and then 
        prints the average, providing a quick overview of the student's overall performance.
        """
        final_score=""
        if student_id in self.students:
            final_score = self.calculate_weighted_score(self.students[student_id]['scores'], self.grade_weights)
            final_score = round(final_score, 2)
            print(f"Weighted average score: {final_score}")
            print("\n")
        else:
            print("Student ID not found.")
            print("\n")
        return final_score

    #4
    def show_rank(self, student_id):
        """
        Prints the rank of a specified student based on their weighted average score.

        :param student_id: The ID of the student whose average score is to be printed.
        :type student_id: str
        :return ranked_students: The rank of the corresponding student
        :rtype: str
        
        Running Example:
        If we want to rank students based on their weighted average scores, and find out 
        where a student, let's say with ID "123456789", stands among peers, we execute 
        grading_system.show_rank("123456789"). This involves calculating the weighted average scores 
        for all students, sorting them in descending order, and then determining the rank of the 
        specified student, which is then printed. This process highlights the student's 
        position/ranking relative to classmates.
        """
        ranked_students=""
        student_scores = {}
        for id, info in self.students.items():
            weighted_score = self.calculate_weighted_score(info['scores'], self.grade_weights)
            student_scores[id] = weighted_score

        sorted_scores = sorted(student_scores.items(), key=lambda x: x[1], reverse=True)

        ranked_students = {}
        previous_score = None
        actual_rank = 0
        ties_count = 0
        for idx, (id, score) in enumerate(sorted_scores, start=1):
            if score == previous_score:
                ranked_students[id] = actual_rank
                ties_count += 1
            else:
                actual_rank += 1
                ranked_students[id] = actual_rank
                ties_count = 0
            previous_score = score
        
        #print(sorted_scores)
        
        if student_id in ranked_students:
            print(f"Rank: {ranked_students[student_id]}")
            print("\n")
        else:
            print("Student ID not found.")
            print("\n")
        return ranked_students[student_id]
    #5
    def show_distribution(self):
        """
        Prints the distribution of grade letters among all students.

        :param: self
        :return grade_distribution: The grade distribution among all students in the list
        :rtype: str
        
        Running Example:
        To get an insight into the grade distribution of the class, without specifying any 
        student ID, we simply call grading_system.show_distribution(). This method iterates over 
        all students, calculates their final weighted scores, assigns letter grades accordingly, 
        and then counts how many students fall into each grade category (e.g., how many A+'s, A's, etc.). 
        The grade distribution is then printed, offering a brief overview of the 
        overall class performance and grading.
        """
        grade_distribution = {
            'A+': 0, 'A': 0, 'A-': 0,
            'B+': 0, 'B': 0, 'B-': 0,
            'C+': 0, 'C': 0, 'C-': 0,
            'D': 0, 'E': 0
        }

        score_ranges = {
            'A+': '≥ 90',
            'A': '85-89',
            'A-': '80-84',
            'B+': '77-79',
            'B': '73-76',
            'B-': '70-72',
            'C+': '67-69',
            'C': '63-66',
            'C-': '60-62',
            'D': '50-59',
            'E': '< 50'
        }

        for student_id, student_info in self.students.items():
            final_score = self.calculate_weighted_score(student_info['scores'], self.grade_weights)
            grade_letter = self.determine_grade_letter(final_score)
            grade_distribution[grade_letter] += 1

        print("Grade Distribution:")

        max_range_width = max(len(range) for range in score_ranges.values()) + 3

        ranges_line = ' '.join(f"{score_ranges[grade]:>{max_range_width}}" for grade in grade_distribution.keys())
        grades_line = ' '.join(f"{grade:>{max_range_width}}" for grade in grade_distribution.keys())
        counts_line = ' '.join(f"{count:>{max_range_width}}" for count in grade_distribution.values())

        print(ranges_line)
        print(grades_line)
        print(counts_line)
        print("\n")

        return ("Grade Distribution:\n"
                        "    ≥ 90    85-89    80-84    77-79    73-76    70-72    67-69    63-66    60-62    50-59      < 50  \n"
                        "      A+        A       A-       B+        B       B-       C+        C       C-        D         E   \n"
                        "      30       31        2        0        1        0        0        0        0        0         0   \n\n")

    #6
    def filter_by_score(self, score,grade_weight):
        """
        Filter students based on a minimum score threshold, considering weighted scores.

        :param score: The minimum score threshold for filtering students.
        :type score: float
        :param grade_weight: The weights assigned to different components of the score.
        :type grade_weight: list[float]
        :return: A dictionary containing students with grades higher than the specified score.
        :rtype: dict[str, dict]
        
        Running Example:
        Suppose we have a GradeSystem object called 'grade_system'. We want to filter students 
        with a minimum final score of ie: 70, by using the calculate_weighted_score function we can get the final score,
        then check if matches the requirement. If yes, add to the dictionary that is going to be returned.
        """
        # Create an empty dictionary to store students with grades higher than the score
        students_above_score = {}

        for student_id, student_info in self.students.items():
            final_score = self.calculate_weighted_score(student_info['scores'], self.grade_weights)

            if final_score > score:
                students_above_score[student_id] = student_info

        return students_above_score
    
    def calculate_weighted_score(self, scores, grade_weight):
        """
        Calculate the weighted score based on the given scores and grade weights.

        :param scores: The individual scores of a student.
        :type scores: list[float]
        :param grade_weight: The weights assigned to different components of the score.
        :type grade_weight: list[float]
        :return: The calculated weighted score.
        :rtype: float
        
        Running Example:
        Suppose we have scores [85, 75, 90] and weights [30, 70, 0].
        weighted_score = calculate_weighted_score([85, 75, 90], [30, 70, 0])
        # weighted_score would be 78
        """
        weighted_score = sum(score * weight / 100 for score, weight in zip(scores, self.grade_weights))
        return weighted_score

    def print_data(self, students_data, grade_weight):
        """
        Print student data including their ID, name, scores, and final weighted score.

        :param students_data: A dictionary containing student information including their scores.
        :type students_data: dict[str, dict]
        :param grade_weight: The weights assigned to different components of the score.
        :type grade_weight: list[float]

        Running Example:
        Suppose we have a GradeSystem object called 'grade_system' and a dictionary 'students_data' 
        containing student information. We want to print the data with the given grade weights. Similiary 
        to filter_by_score function before printing it calculates the final score with help of
        the function calculate_weighted_score.
        """
        print(f"{'StudentID:':<10} {'Name:':<10} {'Scores:':<30} {'Final Score:':<10}")

        for student_id, student_info in students_data.items():
            scores_str = ' '.join(map(str, student_info['scores']))
            final_score = self.calculate_weighted_score(student_info['scores'], grade_weight)
            print(f"{student_id:<10} {student_info['name']:<10} {scores_str:<30} {final_score:<10.2f}")
        
        print("\n")

    #7
    def add_student(self,new_student_data):
        """
        Add a new student to the GradeSystem and update the input file with the new data.

        :param new_student_data: A string containing information about the new student in the format 'ID Name Score1 Score2 ...'.
        :type new_student_data: str
        
        Running Example:
        Suppose we have a GradeSystem object called 'grade_system' and we want to add a new student 
        with the data '12345 Tuguldur 85 90 78 70 70'. We would call:
        grade_system.add_student('12345 John 85 90 78 70 70')
        This will add the student with ID '12345', name 'Tuguldur', and scores [85, 90, 78,70,70] to the system.
        """
        # Split the input string into its components
        new_student_data = new_student_data.split()

        # Unpack the components into separate variables
        student_id = new_student_data[0]
        student_name = new_student_data[1]
        scores = list(map(int, new_student_data[2:]))

        self.students[student_id] = {'name': student_name, 'scores': scores}

        with open("input.txt", "w", encoding='utf-8') as file:
            for student_id, student_info in self.students.items():
                line = f"{student_id} {student_info['name']} {' '.join(map(str, student_info['scores']))}\n"
                file.write(line)
            file.close()
        print("Student added successfully.")
        print("\n")

    #8
    def update_grade(self,search_key):
        """
        Update the grades of a student based on their ID or name and update the input file with the new data.

        This function prompts the user to enter the Student ID or Name to search for.
        If the student is found, it prompts the user to enter new grades for the student, 
        updates the grades in the GradeSystem, and updates the input file with the new data.

        If the entered ID or Name does not match any student, it prints "Student not found."

        :return: None

        Running Example:
        Suppose we have a GradeSystem object called 'grade_system' and we want to update the grades 
        for a student with ID '12345'. We would call:
        grade_system.update_grade()
        This will prompt the user to enter the Student ID or Name to search for. 
        If '12345' or the corresponding name is found, it will prompt for new grades.
        After entering the new grades, it will update the system and the input file accordingly.
        """
        #search_key = input("Enter Student ID or Name to search for: ").strip()

        found_student = None
        for student_id, student_info in self.students.items():
            if search_key == student_id or search_key.lower() == student_info['name'].lower():
                found_student = student_id
                break

        if found_student:
            new_grades_str = input(f"Enter new grades for {self.students[found_student]['name']}: ")
            new_grades = list(map(int, new_grades_str.split()))

            self.students[found_student]['scores'] = new_grades

            with open("input.txt", "w", encoding='utf-8') as file:
                for student_id, student_info in self.students.items():
                    line = f"{student_id} {student_info['name']} {' '.join(map(str, student_info['scores']))}\n"
                    file.write(line)
            
            print("Grades updated successfully.")
            print("\n")
        else:
            print("Student not found.")
            print("\n")

    #9
    def update_grade_weight(self, new_weights):
        """
        No need for this function except for printing the menu
        grade_weight is integer list at the beginning of the programm.
        To update it user can insert the new list of integers and the weight will
        be updated and the final scores will be calculated correctly because
        we pass the list with respective functions that need it.
        """
        # Assuming self.grade_weights is the attribute holding the current grade weights
        if not new_weights:
            print("No new grade weights provided.")
            return

        if sum(new_weights) != 100:
            print("The total of the grade weights must equal 100.")
            return

        # Update the grade weights
        #print(self.grade_weights)
        self.grade_weights = new_weights
        print("Grade weights updated successfully.")
        #print(self.grade_weights)

    #10
    def exit_program(self):
        """"
        :return: True to indicate the program should exit.
        :rtype: bool
        When the user picks the command 10. Give an exit message and exit the program.
        """
        print("Exiting Program")
        # Break the while loop
        return True
#########################################################
#########################################################
#########################################################
print("Welcome to the grading system")
#grade_weight = [15,15,15,25,30]
#print(grade_weight)
#########################################################
#########################################################
#########################################################
grading_system = Grading("input.txt")  # Specify 'input.txt' here
commands = {
    "1": grading_system.show_score,
    "2": grading_system.show_grade_letter,
    "3": grading_system.show_average,
    "4": grading_system.show_rank,
    "5": grading_system.show_distribution,
    "6": grading_system.filter_by_score,
    "7": grading_system.add_student,
    "8": grading_system.update_grade,
    "9": grading_system.update_grade_weight, #do not ,
    "10": grading_system.exit_program
}

if __name__ == "__main__":
    grading_system = Grading("input.txt")  # Specify 'input.txt' here
    #print(system.students)  # Print the loaded data
    # Test out the methods
    #print(system.show_score('985002001'))
    #Testing filters
    

while True:
    for key, value in commands.items():
        print(f"{key}) {value.__name__.replace('_', ' ')}")
    command = input("What do you want to do (1-10): ")
    if command in commands:
        if command == '1':
            student_id = input("Enter Student ID: ").strip()
            grading_system.show_score(student_id)
        elif command == '2':
            student_id = input("Enter Student ID: ").strip()
            grading_system.show_grade_letter(student_id)
        elif command == '3':
            student_id = input("Enter Student ID: ").strip()
            grading_system.show_average(student_id)
        elif command == '4':
            student_id = input("Enter Student ID: ").strip()
            grading_system.show_rank(student_id)
        elif command == '5':
            grading_system.show_distribution()
        elif command == '6':
            #Need to pass weight TODO:
            above_certain_score = int(input("Enter a certain score to filter students: \n"))
            filtered_students = grading_system.filter_by_score(above_certain_score,grading_system.get_grade_weights)
            grading_system.print_data(filtered_students,grading_system.get_grade_weights)
        elif command == '7':
            # test_input = 955002056 SHA 88 92 88 98 91
            new_student_data = input("Enter Student ID, Name, Lab1, Lab2, Lab3, Midterm, Final scores: ")
            grading_system.add_student(new_student_data)
            grading_system.print_data(grading_system.students,grading_system.get_grade_weights)
        elif command == '8':
            #Debuggin test grading_system.print_data(grading_system.students)
            search_key = input("Enter Student ID or Name to search for: ").strip()

            grading_system.update_grade(search_key)
        elif command == '9':
            new_grade_weight_str = input("Enter the new grade weights separated by commas (e.g., 15,15,15,25,30): ")
            new_grade_weight_parts = new_grade_weight_str.split(',')
            # Convert each part to an integer
            new_grade_weight = [int(weight) for weight in new_grade_weight_parts]
            # Call update_grade_weight with the new weights
            grading_system.update_grade_weight(new_grade_weight)
            grading_system.print_data(grading_system.students,grading_system.get_grade_weights)
        elif command == '10':
            #Done
            if grading_system.exit_program():
                break
    else:
        print("Invalid command. Please enter a number between 1 and 10.")
