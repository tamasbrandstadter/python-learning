import re
import operator


def divide_by_ten(number):
    try:
        print(10 / number)
    except ZeroDivisionError:
        print("Fail, can't divide by zero.")


# Write a function that opens a file called "my-file.txt", then prints
# each line from the file.
# If the program is unable to read the file (for example it does not exist),
# then it should print the following error message: "Unable to read file: my-file.txt"
def show_file():
    file_name = 'my-file.txt'
    try:
        file = open(file_name, 'r').read().split('\n')
        for line in file:
            print(line)
    except IOError:
        print('Unable to read file: {}'.format(file_name))


# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.
def count_lines_in_file(file_name):
    try:
        return len(open(file_name, 'r').read().split('\n'))
    except IOError:
        return 0


# Write a function that is able to manipulate a file
# By writing your name into it as a single line
# The file should be named "my-file.txt"
# In case the program is unable to write the file,
# It should print the following error message: "Unable to write file: my-file.txt"
def write_name_to_file(name):
    try:
        file = open('my-file.txt', 'w')
        file.write(name)
    except IOError:
        print("Unable to write file: my-file.txt")


# Create a function that takes 3 parameters: a path, a word and a number
# and is able to write into a file.
# The path parameter should be a string that describes the location of the file you wish to modify
# The word parameter should also be a string that will be written to the file as individual lines
# The number parameter should describe how many lines the file should have.
# If the word is "apple" and the number is 5, it should write 5 lines
# into the file and each line should read "apple"
# The function should not raise any errors if it could not write the file.
def write_to_file(path, word, number):
    try:
        file = open(path, 'w')
        for i in range(number):
            file.write(word)
            file.write('\n')
    except IOError:
        print("Can't read file")


# Write a function that copies the contents of a file into another
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful
def copy_content(from_file, to_file):
    try:
        with open(from_file) as f:
            lines = f.read()
            with open(to_file, 'w') as to:
                for line in lines:
                    to.write(line)
        return True
    except IOError:
        return False


# Read all data from 'log.txt'.
# Each line represents a log message from a web server
# Write a function that returns an array with the unique IP addresses.
def get_unique_ips():
    ips = set()
    try:
        with open('log.txt') as logs:
            lines = logs.read().split('\n')
            for line in lines:
                found = re.search("(\d{1,2}\.){3}(\d{1,2})", line)
                if found:
                    group = found.group(0)
                    ips.add(group)
        return ips
    except IOError:
        return ips


# Read all data from 'log.txt'.
# Each line represents a log message from a web server
# Write a function that returns the GET / POST request ratio
def get_to_post_ratio():
    try:
        with open('log.txt') as logs:
            lines = logs.read().split(' /')
            post_count = 0
            get_count = 0
            for line in lines:
                method = line[-4:]
                if method == 'POST':
                    post_count += 1
                else:
                    get_count += 1
        return get_count / post_count
    except IOError:
        return -1


# Create a method that decrypts the duplicated-chars.txt
def decrypt_duplicated():
    try:
        with open('duplicated-chars.txt') as duplicated:
            lines = duplicated.read().split('\n')
            for line in lines:
                print(line[::2])
    except IOError:
        print('Could not open file')


# Create a method that decrypts reversed-lines.txt
def decrypt_reversed():
    try:
        with open('reversed-lines.txt') as reversed_lines:
            lines = reversed_lines.read().split('\n')
            for line in lines:
                print(line[::-1])
    except IOError:
        print('Could not open file')


# Create a method that decrypts reversed-order.txt
def decrypt_reversed_order():
    try:
        with open('reversed-order.txt') as reversed_order:
            lines = reversed_order.read().split('\n')
            for line in reversed(lines):
                print(line)
    except IOError:
        print('Could not open file')


# Create a method that find the 5 most common lottery numbers in lottery.csv
def five_most_frequent():
    frequency = {}
    try:
        with open('lottery.csv') as lottery:
            lines = lottery.read().split('\n')
            for line in lines:
                numbers = line[-14:].split(';')
                for number in numbers:
                    if number.isdigit():
                        i = int(number)
                        if i in frequency:
                            frequency[i] += 1
                        else:
                            frequency[i] = 1
            sorted_items = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
            for i in range(5):
                key, value = sorted_items[i]
                print(key)
    except IOError:
        print('Could not open file')


divide_by_ten(0)
show_file()
print(count_lines_in_file('my-file.txt'))
write_name_to_file('Tamas')
write_to_file('my-file.txt', 'alma', 5)
copy_content('from-file.txt', 'to-file.txt')
ret_ips = get_unique_ips()
print(ret_ips)
print(len(ret_ips))
print(get_to_post_ratio())
decrypt_duplicated()
decrypt_reversed()
decrypt_reversed_order()
five_most_frequent()
