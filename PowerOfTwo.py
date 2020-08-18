def powerOfTwo(n):
    a = ((n != 0) and (n & (n-1) == 0))
    if( a ==True):
        print("This is power of 2")
    else:
        print("This is not a power of 2")

def main():
    number=int(input("Enter the number: "))
    powerOfTwo(int(number))
    

if __name__ =="__main__":
    main()