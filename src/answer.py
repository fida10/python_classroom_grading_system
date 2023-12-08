"""
Practice Question 1: Classroom Grading System

Task:

Write a function classify_grades that takes a list 
of student grades (as integers) and classifies each grade. 
The function should return a list of strings with classifications: 
'Fail' (less than 60), 'Pass' (60-69), 'Good' (70-89), 'Excellent' (90-100).
"""

def classify_grades(grades):
    ans = []
    for grade in grades:
        if grade >= 90 and grade <= 100:
            ans.append('Excellent')
        elif grade >= 70 and grade <= 89:
            ans.append('Good')
        elif grade >= 60 and grade <= 69:
            ans.append('Pass')
        else:
            ans.append('Fail')
    return ans