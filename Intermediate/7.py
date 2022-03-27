def say_hello(name, gender):
    if gender.lower() == "male":
        first_word = "Mr. "
    elif gender.lower() == "female":
        first_word = "Ms. "
    else:
        return "Gender is not found!"
    return "Hello, {} {}".format(first_word, name) 

name = "Hudya"
gender = "male"
say_1 = say_hello(name, gender)
print(say_1)

name = "Ayu"
gender = "FEMALE"
say_2 = say_hello(name, gender)
print(say_2)

name = "Dhana"
gender = "nfdsnjfdsnjdfs"
say_3 = say_hello(name, gender)
print(say_3)