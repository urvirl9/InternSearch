def NumOfOnes(n):
    count=0
    while(n!=0):
        n &=(n-1)
        count+=1
    print("The number of ones is: "+str(count))

def main():
    number=int(input("Enter the number: "))
    NumOfOnes(int(number))
    

if __name__ =="__main__":
    main()