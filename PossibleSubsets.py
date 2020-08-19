def Subsets(arr , n):
    print("All possible subsets of an array are: ")
    for i in range(2**n):
        print()
        for j in range(n):
            if (i & (1 << j)) != 0:
                print(str(arr[j]), end =" ")
                
                
    
def main():
    number=int(input("Enter the size of the set: "))
    print("Enter the elements of set")
    arr = []
    for i in range(0,number):
        elements = int(input())
        arr.append(elements)
    total_subsets = 2**number
    print("The total number of subsets are: "+ str(total_subsets))
    Subsets(arr , number)
    

if __name__ =="__main__":
    main()