import digitprop
import random

def check():
    isSpecial = False
    special =[]
    non_special=[]
    for i in range(100,351):
        if(digitprop.has_small_digits(i,2)or digitprop.is_antipalindrome(i)):
            special.append(i)
        else:
            non_special.append(i)

    print(non_special)
    
    for i in non_special:
        for k in range(2,351):
            d = i**k
            if(digitprop.has_small_digits(d,2)or digitprop.is_antipalindrome(d)):
                print(i,k,d)

def main():
    # Main loop
    check()
if __name__=="__main__":
    # We are the main program, not an import
    main()
