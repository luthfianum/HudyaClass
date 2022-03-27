fruits = ["mango", "apple", "banana", "orange", "strawberry", "guava"]
fruits_2 = ["strawberry", "guava", "avocado", "durian"]

_temp = []
for item in fruits_2:
    if item in fruits:
        _temp.append(item)

print(_temp)