def MSB(n):


    n |= n>>1
    n |= n>>2
    n |= n>>4
    n |= n>>8
    n |= n>>16
       
    n = n + 1
    return (n >> 1)

def main():
    number=int(input("Enter the number: "))
    print(MSB(int(number)))


if __name__ =="__main__":
    main()
