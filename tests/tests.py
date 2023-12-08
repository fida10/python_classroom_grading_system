import unittest
from src.answer import classify_grades


class TestClassifyGrades(unittest.TestCase):
    def test_classify_grades(self):
        grades = [55, 65, 75, 95]
        expected = ['Fail', 'Pass', 'Good', 'Excellent']
        self.assertEqual(classify_grades(grades), expected)

    def test_empty_list(self):
        self.assertEqual(classify_grades([]), [])

    def test_boundary_values(self):
        grades = [59, 60, 69, 70, 89, 90, 100]
        expected = ['Fail', 'Pass', 'Pass', 'Good',
                    'Good', 'Excellent', 'Excellent']
        self.assertEqual(classify_grades(grades), expected)


if __name__ == '__main__':
    unittest.main()
