# a variable is visible is accessible
# LEGB rank: Local -> Enclosed -> Global -> Built-in


def func1():
    x = 1

    def func2():
        print(x)
    func2()



func1()

