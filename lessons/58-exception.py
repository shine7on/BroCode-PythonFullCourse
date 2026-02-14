# exception
# an event that interrupts the flow of a program
# zero division error, type error, value error
# STEP: try -> except -> finally


try:
    number = int(input("Enter your number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can not divide by zero")
except ValueError:
    print("Enter only numbers")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup")

