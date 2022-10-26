




#>---- when something is a Palindrome ----< 
# x = 1221 
print(1221%10) #---> this is 1 
print((1221/10)%10) # ---> this is 2   
#It's like saying swapping 21 to 12 and if first two sequence = last two sequence => Palindrome 




#>---- when something is not a Palindrome ----< 

# x = -1221 
#print(-1221%10) 







def isPalindrome(x):
        rev = 0
        init_n = x
        if( x < 0):
            return False
        while x != 0:
                rev = (rev*10) +  x % 10
                x = x // 10 
        
        if(rev == init_n):
                    
            return True 
        return False
            
test = isPalindrome(1331)
print(test)
        




