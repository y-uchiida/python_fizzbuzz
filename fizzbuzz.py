def fizz_buzz(num):
    return "Buzz" * (num % 5 == 0) or str(num)


print("\n".join(fizz_buzz(num) for num in range(1, 101)))
