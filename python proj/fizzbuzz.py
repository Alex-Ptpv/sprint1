def fizz_buzz():
    for num in range(100):
        if num % 5 == 0 and num % 8 != 0:
            print("Fizz")
        elif num % 8 == 0 and num % 5 != 0:
            print("Buzz")
        elif num % 5 == 0 and num % 8 == 0:
            print("FizzBuzz")
        else:
            print(num)

fizz_buzz()