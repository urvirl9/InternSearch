def rus_algo(a,b):
    x = a; y = b
    mul_result = 0
    while x > 0:
        if x % 2 == 1: mul_result += y
        y = y << 1
        x = x >> 1
    return mul_result

def main():
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print(rus_algo(num1 , num2))


if __name__ =="__main__":
    main()
