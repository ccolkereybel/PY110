numbers = [1, 2, 3, 4]
numbers[0] = numbers[0] + 1
numbers[1] = numbers[1] + 1
numbers[2] = numbers[2] + 1
numbers[3] = numbers[3] + 1


print(numbers)

dict1 = {
    'apple': 'Produce',
    'carrot': 'Produce',
    'pear': 'Produce',
    'broccoli': 'Produce',
}

dict1['apple'] = 'Fruit'
dict1['carrot'] = 'Vegetable'
dict1['pear'] = 'Fruit'
dict1['broccoli'] = 'Vegetable'
dict1['watermelon'] = 'Fruit'

del dict1['carrot']

print(dict1)