def fizzBuzz(answer):
    for i in range(1, answer):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
answer = int(input("Enter Value")) + 1
fizzBuzz(answer)