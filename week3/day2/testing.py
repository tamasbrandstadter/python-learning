import unittest


class Sum:

    def __init__(self, numbers):
        self.__numbers = numbers

    def sum_nums(self):
        return sum(self.__numbers)


class SumTest(unittest.TestCase):

    def test_sum_nums(self):
        test_sum = Sum([1, 2, 3, 4, 5])
        self.assertEqual(15, test_sum.sum_nums())

    def test_sum_nums_with_empty_list(self):
        test_sum = Sum([])
        self.assertFalse(test_sum.sum_nums())

    def test_sum_nums_with_none(self):
        test_sum = Sum(None)
        with self.assertRaises(TypeError):
            test_sum.sum_nums()


class Anagram:

    @staticmethod
    def are_those_anagrams(text, text2):
        return sorted(text.lower()) == sorted(text2.lower())


class AnagramTest(unittest.TestCase):

    def test_anagram(self):
        self.assertTrue(Anagram.are_those_anagrams('Alma', 'Maal'))


class LetterCounter:

    @staticmethod
    def count_letters(text):
        frequency = {}
        for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency


class LetterCounterTest(unittest.TestCase):

    def test_count_letters(self):
        excepted_dictionary = {'a': 2, 'l': 1, 'm': 1}
        self.assertDictEqual(excepted_dictionary, LetterCounter.count_letters('alma'))


if __name__ == '__main__':
    unittest.main()
