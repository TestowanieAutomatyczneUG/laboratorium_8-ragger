class FizzBuzz:
    def game(self, n):
        if isinstance(n, (int,float)):
            if n % 5 == 0 and n % 3 == 0:
                return "FizzBuzz"
            elif (n % 5) == 0:
                return "Buzz"
            elif (n % 3) == 0:
                return "Fizz"
            else:
                return str(n)
        else:
            raise TypeError("not a number")