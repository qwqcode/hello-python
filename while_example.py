pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
pets_b = pets[:]
print(str(pets))
while 'dog' in pets:
    pets.remove('dog')
print('All dogs was removed:\n' + str(pets))

print('\nBreak')
print(str(pets_b))
while 'dog' in pets_b:
    pets_b.remove('dog')
    break
print('Only remove the first dog:\n' + str(pets_b))

print('\nShow Number 1~10')
num_str = []
num_max = 10
num_min = 1
while num_max >= num_min:
    num_str.append(num_max)
    num_max = num_max-1
print(str(
    num_str[::-1]  # 倒序
))
