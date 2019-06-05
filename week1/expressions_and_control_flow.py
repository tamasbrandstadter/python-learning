def remaining_seconds(a, b, c):
    day_in_seconds = 24 * 60 * 60
    print('Remaining {}'.format(day_in_seconds - a * b * c))


def calculate_volume(a, b, c):
    print('Surface volume: {}'.format(a * b * c))


def legs(chickens, pigs):
    print('Legs {}'.format(chickens * 2 + pigs * 4))


def sum_and_avg(a, b, c, d, e):
    summary = a + b + c + d + e
    avg = summary / 5
    print('Sum: {}, Avg: {}'.format(summary, avg))


def bigger(a, b):
    print(max(a, b))


def draw_full_pyramid(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))


def draw_inverted_pyramid(rows):
    for i in reversed(range(rows)):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))


def find_index_of(text, keyword):
    return text.find(keyword)


print('Tamas')
print(31)
print(1.75)

print(13 + 22)
print(22 - 13)
print(22 * 13)
print(22 / 13)
print(22 // 13)
print(22 % 13)

semester_hours = 6 * 5 * 17
print('Hours spent coding {}'.format(semester_hours))
print('Avg weekly work hours {}'.format(semester_hours / 52))

mass_in_kg = 81.2
height_in_m = 1.78

bmi = mass_in_kg / height_in_m.__pow__(2)
print(bmi)

current_hours = 14
current_minutes = 34
current_seconds = 42

calculate_volume(5.4, 3.6, 2.4)
remaining_seconds(current_hours, current_minutes, current_seconds)

legs(int(input('Chickens: ')), int(input('Pigs: ')))
bigger(int(input('Number1: ')), int(input('Number2: ')))

num = int(input('Enter count: '))
count = 0
sum_value = 0

while count < num:
    y = int(input('Num:'))
    sum_value += y
    count += 1

print('Sum: {}, Avg: {}'.format(sum_value, sum_value / num))
print(find_index_of("this is what I'm searching in", "searching"))
print(find_index_of("this is what I'm searching in", "not"))
