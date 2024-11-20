def fizz_buzz(n):
    for d in range(1, n+1):
        if d % 3 == 0:
            print("Buzz")
            
        elif d % 5 == 0:
            print("Fizz")
            
        elif d % 3 == 0 and d % 5 == 0:
            print ("FizzBuzz")
        
        else: 
            print(d)
fizz_buzz(50)
        
        
            
        


            
        



