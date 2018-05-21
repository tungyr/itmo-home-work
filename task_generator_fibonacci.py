def fibonacci(qtty):
    current = 1
    previous = 1
    while qtty > 0:
        yield previous
        temp = previous
        previous = current
        current = current + temp
        qtty -= 1
    return current

for i in fibonacci(10):
    print(i)
