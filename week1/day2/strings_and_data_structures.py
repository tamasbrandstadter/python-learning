import operator

products = {
    'Eggs': 200,
    'Milk': 200,
    'Fish': 400,
    'Apples': 150,
    'Bread': 50,
    'Chicken': 550
}


def spent(values):
    total = sum(values)
    print(total)
    return total


def greatest_expanse(values):
    print(max(values))


def smallest_expanse(values):
    print(min(values))


def avg_spending(values):
    total = spent(values)
    print(total / len(values))


def get_price(product):
    return products[product]


def most_expensive():
    print(sorted(products.items(), key=operator.itemgetter(1))[-1])


def cheapest():
    print(sorted(products.items(), key=operator.itemgetter(1))[0])


def below_price(target_price):
    count = 0
    for product in products.items():
        produce_name, produce_price = product
        if produce_price < target_price:
            count += 1
    return count


def price_with_more(target_price):
    products_with_more_than_price = []
    for product in products.items():
        produce_name, produce_price = product
        if produce_price > target_price:
            products_with_more_than_price.append((produce_name, produce_price))
    return products_with_more_than_price


# The position returned by josephus(n - 1, k) is adjusted because the recursive call josephus(n - 1, k) considers
# the original position k%n + 1 as position 1
def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1


def armstrong_number(number):
    digits = []
    temp = number
    while temp != 0:
        digit = temp % 10
        temp //= 10
        digits.append(digit)

    size = len(digits)
    digits_on_pow = []
    for digit in digits:
        digits_on_pow.append(pow(digit, size))

    return sum(digits_on_pow) == number


def find_substring_in_element(target, words):
    for index, word in enumerate(words):
        if target in word:
            return index
    return -1


example = 'In a dishwasher far far away'
example = example.replace('dishwasher', 'galaxy')

url = 'https//www.reddit.com/r/nevertellmethebots'
url = 'https:' + url[5:].replace('bots', 'odds')

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
quote = quote[:21] + 'always takes longer than' + quote[21:]

reversed_text = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"

print(example)
print(url)
print(quote)
print(reversed_text[::-1])

names = []
# empty list evaluates as true
print(not names)

names.append('William')
print(not names)
names.append('John')
names.append('Amanda')

for name in names:
    print(name)

for i in range(0, len(names)):
    print('{}. {}'.format(i + 1, names[i]))

print(names[2])
names.pop(1)

print(names[::-1])

names.clear()

number_map = {}
print(not number_map)

number_map[97] = 'a'
number_map[98] = 'b'
number_map[99] = 'c'
number_map[65] = 'A'
number_map[66] = 'B'
number_map[67] = 'C'

print(number_map.keys())
print(number_map.values())

number_map[68] = 'D'
print(len(number_map.items()))

number_map.pop(97)

print(100 in number_map)

number_map.clear()

fruits = ['Apple', 'Avocado', 'Blueberries', 'Durian', 'Lychee']
list_b = list(fruits)

print('Durian' in fruits)
list_b.remove('Durian')

fruits.insert(4, 'Kivifruit')
print(fruits)

print(fruits.index('Avocado'))
try:
    print(list_b.index('Durian'))
except ValueError:
    print('Not found')

list_b.extend(['Passion Fruit', 'Pummelo'])
print(list_b)

books = {'978-1-60309-452-8': 'A Letter to Jo', '978-1-60309-459-7': 'Lupus',
         '978-1-60309-444-3': 'Red Panda and Moon Bear', '978-1-60309-461-0': 'The Lab'}

for book in books.items():
    key, value = book
    print('{} (ISBN: {})'.format(value, key))

del books['978-1-60309-444-3']
print('978-1-60309-444-3' in books)

books['978-1-60309-453-5'] = 'Why Did We Trust Him?'
print('978-1-60309-453-5' in books)
print(books['978-1-60309-453-5'])

expanses = [500, 1000, 1250, 175, 800, 120]
spent(expanses)
greatest_expanse(expanses)
smallest_expanse(expanses)
avg_spending(expanses)
most_expensive()
print(price_with_more(150))
print(find_substring_in_element("ching", ["this", "is", "what", "I'm", "searching", "in"]))
print(find_substring_in_element("not", ["this", "is", "what", "I'm", "searching", "in"]))
print(armstrong_number(1634))
print(armstrong_number(153))
