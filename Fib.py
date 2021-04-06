def fibonacci(n):
    if n == 0:
      return 0
    elif n == 1:
      return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
def main():
    el = input('Введите номер искомого элемента : ')
    el = int(el)
    val = fibonacci(el)
    print(str(el)+' элемент последовательности равен ' + str(val))
if __name__ == '__main__':
    main()