class MyClassA:
    def func1():
        var = 100
        if var < 200:
           print("Expression value is less than 200")
           if var == 150:
              print("Which is 150")
           elif var == 100:
              print("Which is 100")
           elif var == 50:
              print("Which is 50")
           elif var < 50:
              print("Expression value is less than 50")
        else:
           print("Could not find true expression")

        print("Good bye!")

    def func2():
        def func3():
            courses1=["java","python"]
            courses2=["pandas","java","python"]
            for x in courses1:
                 for y in courses2:
                     if x==y:
                         break
                     print(x ,y)

class MyClassB:
    async def func1():
        print("Prime numbers in the range 2 to 100 are,")
        for x in range(2,101):
            isPrime = True
            # Checking if x is a prime number or not
            for y in range(2,x):
                # Checking if any number in the range [2, x-1] completely divides x
                if x%y==0:
        	    # If the number completely divides x then x is not a prime number
                    isPrime = False
                    break

            # If isPrime is true print x
            if isPrime:
                print(x,end=" ")

            async for idx in range(1,10):
                pass
