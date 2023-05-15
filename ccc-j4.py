import re

books = input()

counter = 0
place = 0

bookList = []

sortedBooksAlpha = ''.join(sorted(books))

x = sortedBooksAlpha.split()

y = books.split()

for i in range(5):
    if x[place] != y[place]:
        counter += 1
        place += 1

print(counter)