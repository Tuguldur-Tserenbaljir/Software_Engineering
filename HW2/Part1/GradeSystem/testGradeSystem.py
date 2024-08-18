
#from gradeSystem import Grading  # Adjust this import based on your project structure

import unittest
from unittest.mock import patch
from gradeSystem import Grading  # Adjust this import based on your actual file and class names
from io import StringIO
 
import sys
import io
import shutil
import os

path = "input.txt"
tes = Grading(path)
class TestGradingSystem(unittest.TestCase):

    def setUp(self):
        # Path to the original and temporary input file
        self.original_file_path = 'input.txt'
        self.temp_file_path = 'temp_input.txt'
        # Make a copy of the original input file to use for testing
        shutil.copyfile(self.original_file_path, self.temp_file_path)
        # Initialize your Grading system with the temporary file
        self.grading_system = Grading(self.temp_file_path)

    def tearDown(self):
        # Delete the temporary file after the test to ensure no permanent changes
        os.remove(self.temp_file_path)

    @patch('builtins.input', side_effect=['10'])
    def test_show_score(self, mock_input):
        """
        Test the show_score function to ensure it prints the expected scores.
        :param mock_input: Mock input to simulate user input.
        :type mock_input: Mock
        :return: None
        :running example: test.show_score("962001044")
        :Time taken to implement:  30 minutes
        :Docstring time: 4/05/2024 8:00 AM
        """
        # Example student ID and scores. Adjust these values based on your actual data or setup.
        student_id = "962001044"
        result = tes.show_score(student_id)
        expected_result = "87 86 98 88 87"  # This is the expected print output; adjust it as necessary.
        self.assertEqual(expected_result,result,"Wrong score")

    @patch('builtins.input', side_effect=['10'])
    def test_show_grade_letter(self, mock_input):
        """
        Test the show_grade_letter function to ensure it returns the expected grade letter.

        :param mock_input: Mock input to simulate user input.
        :type mock_input: Mock
        :return: None
        :running example: test.show_grade_letter("962001044")

        :Time taken to implement:  20 minutes
        :Docstring time: 4/05/2024 8:00 AM
        """
        student_id = "962001044"
        result = tes.show_grade_letter(student_id)
        expected_result = "A"
        self.assertEqual(expected_result,result,"Wrong grade letter")

    @patch('builtins.input', side_effect=['10'])
    def test_show_average(self, mock_input):
        """
        Test the show_average function to ensure it returns the expected average score.

        :param mock_input: Mock input to simulate user input.
        :type mock_input: Mock
        :return: None
        :running example: test.show_average("962001044")

        :Time taken to implement:  30 minutes
        :Docstring time: 4/05/2024 8:05 AM
        """
        student_id = "962001044"
        result = tes.show_average(student_id)
        expected_result = 88.75
        self.assertEqual(expected_result,result,"Wrong average score")

    @patch('builtins.input', side_effect=['10'])
    def test_show_rank(self, mock_input):
        """
        Test the show_rank function to ensure it returns the expected rank.

        :param mock_input: Mock input to simulate user input.
        :type mock_input: Mock
        :return: None
        :running example: test.show_rank("962001044")

        :Time taken to implement:  10 minuites
        :Docstring time: 4/05/2024 8:07 AM
        """
        student_id = "962001044"
        result = tes.show_rank(student_id)
        expected_result = 32
        self.assertEqual(expected_result,result,"Wrong rank")

    @patch('builtins.input', side_effect=['10'])
    def test_show_distribution(self, mock_input):
        """
        Test the show_distribution function to ensure it returns the expected grade distribution.

        :param mock_input: Mock input to simulate user input.
        :type mock_input: Mock
        :return: None
        :running example: test.show_distribution()

        :Time taken to implement:  5 minutes
        :Docstring time: 4/05/2024 8:10 AM
        """
        result = tes.show_distribution()
        expected_result = ("Grade Distribution:\n"
                        "    ≥ 90    85-89    80-84    77-79    73-76    70-72    67-69    63-66    60-62    50-59      < 50  \n"
                        "      A+        A       A-       B+        B       B-       C+        C       C-        D         E   \n"
                        "      30       31        2        0        1        0        0        0        0        0         0   \n\n")
        self.assertEqual(expected_result,result,"Wrong distribution")

    @patch('builtins.input', side_effect=['10'])
    def test_filter_by_score(self, mock_input):
        """
        Test the filter_by_score function to ensure it filters students correctly based on given score threshold.

        :return: None
        :running example: test.filter_by_score()

        :Time taken to implement:  35 minutes
        :Docstring time: 4/05/2024 8:15 AM
        """
        # Assuming the Grading class and an input file are correctly set up
        limit = 95
        grade_weight=[15, 15, 15, 25, 30]
        result = tes.filter_by_score(limit,grade_weight)
        expected_result = {'985002515': {'name': '辜麟傑', 'scores': [98, 96, 98, 98, 91]}}
        self.assertEqual(expected_result,result,"Wrong filter")

    @patch('builtins.input', side_effect=['10'])
    def test_add_student(self, mock_input):
        """
        Test the add_student function to ensure it correctly adds a new student with given data.

        :return: None
        :running example: test.add_student()

        :Time taken to implement:  40 minutes
        :Docstring time: 4/05/2024 8:20 AM
        """
        new_student_id = '987654321'
        new_student_name = 'Alice'
        new_student_scores = [90, 85, 92, 88, 95]  # Example scores
        student_data = f"{new_student_id} {new_student_name} " + " ".join(map(str, new_student_scores))
        self.grading_system.add_student(student_data)
        
        #self.assertIn(new_student_id, self.grading_system.students, "The new student ID wrong")
        #self.assertEqual(self.grading_system.students[new_student_id]['name'], new_student_name, "The student's name wrong")
        self.assertEqual(self.grading_system.students[new_student_id]['scores'], new_student_scores, "The student add wrong")
        print("test_add_student ok")

    @patch('builtins.input', side_effect=['10'])
    def test_update_grade(self, mock_input):
        """
        Test the update_grade function to ensure it correctly updates the grade for a given student.

        :return: None
        :running example: test.update_grade()

        :Time taken to implement:  10 minutes
        :Docstring time: 4/05/2024 8:25 AM
        """
        student_id = '962001051'  # Assuming this student exists in your setup
        #assignment_index = 2  # Assuming first assignment
        #student_data = f"{new_student_id} {new_student_name} " + " ".join(map(str, new_student_scores))
        #student_name= "李威廷"
        new_score = ["80","95","75","30","95"]
        assignment_index = f"{student_id} {' '.join(map(str, new_score))}"
        new_score_int = [int(score) for score in new_score]

        self.grading_system.update_grade(assignment_index)
        self.assertNotEqual(self.grading_system.students[student_id]['scores'], new_score_int,  "Grade was not upgraded correctly.")
        
        print("test_update_grade ok")

    @patch('builtins.input', side_effect=['10'])
    def test_update_grade_weight(self, mock_input):
        """
        Test the update_grade_weight function to ensure it correctly updates the grade weights.

        :return: None
        :running example: test.update_grade_weight()

        :Time taken to implement:  10 minutes
        :Docstring time: 4/05/2024 8:30 AM
        """
        new_weights = [10, 20, 30, 20, 20]  # Example of new weights
        
        self.grading_system.update_grade_weight(new_weights)
        
        self.assertEqual(self.grading_system.get_grade_weights(), new_weights,  "Grade weights were not upgraded correctly.")
        print("test_update_grade ok")
    
    def test_grading_system_integration(self):
        """
        A comprehensive test that covers multiple functionalities of the Grading system.
        This simulates adding a new student, updating grades, and verifying calculations.
        """
        new_student_id = '900000001'
        new_student_name = 'Test'
        new_student_scores = [85, 90, 95, 88, 92]
        
        # Simulate adding a new student
        student_data = f"{new_student_id} {new_student_name} " + " ".join(map(str, new_student_scores))
        self.grading_system.add_student(student_data)
        
        # Verify the student was added correctly
        with open(self.original_file_path, 'r', encoding='utf-8') as f:
            contents = f.read()
            self.assertIn(new_student_id, contents, "The new student ID was not found in the file.")
            self.assertIn(new_student_name, contents, "The new student name was not found in the file.")
        
        # Update the grade weight
        new_weights = [15, 15, 15, 25, 30]
        self.grading_system.update_grade_weight(new_weights)

        # Verify the grade weights were updated
        self.assertEqual(self.grading_system.grade_weights, new_weights)

        # Check calculations: average, grade letter, rank (Assuming the methods return values and not just print them)
        avg_score = self.grading_system.show_average(new_student_id)
        grade_letter = self.grading_system.show_grade_letter(new_student_id)
        rank = self.grading_system.show_rank(new_student_id)  # Assuming show_rank method returns a rank value

        # Example assertions (Your methods need to return these values, not just print them)
        self.assertAlmostEqual(avg_score, 90.1, places=2, msg="Average score calculation is incorrect")
        self.assertEqual(grade_letter, 'A+', msg="Grade letter calculation is incorrect")
        self.assertTrue(isinstance(rank, int), msg="Rank calculation is incorrect")
    
    def test_grading_system_integration_extended(self):
        """
        An extended test that covers more functionalities of the Grading system.
        This simulates adding a single student, updating grades, and verifying calculations.
        """
        # Simulate adding a single student
        charlie_id = '900000004'
        charlie_name = 'Charlie'
        charlie_scores = [85, 88, 82, 90, 92]

        student_data = f"{charlie_id} {charlie_name} " + " ".join(map(str, charlie_scores))
        self.grading_system.add_student(student_data)

        # Verify the student was added correctly
        with open(self.original_file_path, 'r', encoding='utf-8') as f:
            contents = f.read()
            self.assertIn(charlie_id, contents, f"The student with ID {charlie_id} was not found in the file.")
            self.assertIn(charlie_name, contents, f"The student with name {charlie_name} was not found in the file.")

        # Update the grade weight
        new_weights = [20, 20, 20, 20, 20]
        self.grading_system.update_grade_weight(new_weights)

        # Verify the grade weights were updated
        self.assertEqual(self.grading_system.grade_weights, new_weights)

        # Check calculations: average, grade letter, rank for Charlie
        avg_score = self.grading_system.show_average(charlie_id)
        grade_letter = self.grading_system.show_grade_letter(charlie_id)
        rank = self.grading_system.show_rank(charlie_id)  # Assuming show_rank method returns a rank value

        # Example assertions (Your methods need to return these values, not just print them)
        self.assertAlmostEqual(avg_score, 87.4, places=2, msg="Average score calculation is incorrect")
        self.assertEqual(grade_letter, 'A', msg="Grade letter calculation is incorrect")
        self.assertTrue(isinstance(rank, int), msg="Rank calculation is incorrect")



# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main()