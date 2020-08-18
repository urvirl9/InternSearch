def Ith_Bit(n , i):
    if n & (1 << (i - 1)): 
        print("The i-th bit is set") 
    else: 
        print("The i-th bit is not set")
def main():
    number=int(input("Enter the number: "))
    set_bit=int(input("Enter the i-th bit: "))
    Ith_Bit(number , set_bit)
    

if __name__ =="__main__":
    main()