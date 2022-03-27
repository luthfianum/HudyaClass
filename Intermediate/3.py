fruits = ["mango", "apple", "banana", "orange", "strawberry", "guava"]
fruits_2 = ["strawberry", "guava", "avocado", "durian"]

for item in fruits:
    print(item)
    for item_2 in fruits_2: 
        if item == item_2:
            print(f"In this fruit_2 loop, {item_2} is equals to loop in fruits")
        else:
            print(f"In this fruit_2 loop, {item_2} is not equals to loop in fruits")