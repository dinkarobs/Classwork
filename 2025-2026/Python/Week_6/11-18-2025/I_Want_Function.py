def Subtract_2(num1, num2):
    return num1 - num2

def Add_2(one, two):
    return one + two


def Multiply_2(first, second):
    return first * second

def main():
    results=Multiply_2(1,67)
    results_2=Multiply_2(33.5,2)
    results_3 = Add_2(60, 7)
    results_4 = Subtract_2(69,2)
    print(results_4)
    print(results_3)
    print(results)
    print(results_2)
if __name__ == '__main__':
    main()
