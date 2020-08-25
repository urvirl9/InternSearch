def HighestPowOfTwo(n):

    result = 0;
    for i in range(n, 0, -1):


        if ((i & (i - 1)) == 0):

            result = i;
            break;

    return result;

def main():
    number=int(input("Enter the number: "))
    prrint(HighestPowOfTwo(int(number)))


if __name__ =="__main__":
    main()
