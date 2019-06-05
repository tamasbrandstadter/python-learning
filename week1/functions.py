def doubling(a):
    return a * 2


def append_a(s):
    return s + 'a'


def summarize(a):
    if a < 1:
        return a
    return a + summarize(a - 1)


def factorial(a):
    if a < 2:
        return a
    return a * factorial(a - 1)


def subint(a, numbers):
    indices = []
    for i in range(0, len(numbers)):
        if numbers[i] == a or str(numbers[i]).__contains__(str(a)):
            indices.append(i)
    return indices


def unique(numbers):
    return set(numbers)


def anagram(text, text2):
    return sorted(text) == sorted(text2)


def palindrome(text):
    return text + text[::-1]


def bubble(numbers, descending=False):
    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[i]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    if descending:
        return numbers[::-1]
    else:
        return numbers


print(summarize(5))
print(factorial(5))
print(subint(1, [1, 11, 34, 52, 61]))
print(subint(9, [1, 11, 34, 52, 61]))
print(unique([1, 11, 34, 11, 52, 61, 1, 34]))
print(anagram('dog', 'god'))
print(anagram('green', 'fox'))
print(palindrome('greenfox'))
print(bubble([43, 12, 24, 9, 5]))
print(bubble([43, 12, 24, 9, 5], True))
