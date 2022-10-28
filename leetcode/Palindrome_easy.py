

def isPalindrome(x):
        rev = 0
        init_n = x
        if( x < 0):
            return False
        while x != 0:
               
                rev = (rev*10) +  x % 10 
                print(rev)
                x = int(x / 10)
                #print(x)
                
                
        if(rev == init_n):
            #print(rev)
            return True 
        return False
            
test = isPalindrome(1221)
#print(test)
        



print(2%10)
