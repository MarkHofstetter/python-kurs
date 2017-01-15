import random


numbers = []
# print(random.randint(1, 45))
for i in range(1, 45):
  numbers.append(i)

numbers_shuffle = numbers
numbers_sample = numbers
random.shuffle(numbers_shuffle)

for i in range(1, 7):
  l = len(numbers) - 1
  r = random.randint(1, l)
  # print(i, r, l)
  print(i, numbers.pop(r))

print('shuffle')

for i in range(1, 7):
  print(i, numbers_shuffle.pop())

print('sample')
print(random.sample(numbers_sample, 6))
