def foo(num):
    return num+1

def call_foo_with_arg(foo, arg):
    #Functions can be passed around just like
    #any other argument
    return foo(arg)

print(call_foo_with_arg(foo, 4))


#Nested Functions

def parent():
    def first_child():
        return("Printing from the first_child")

    def second_child():
        return ("Printing from the second_child")

    print(first_child())
    print(second_child())

#Whenever we call parent functions sibling functions will be called because of scoping
parent()

#Returning Functions
#Functions can be returned from the other Functions


def sumof_fun(fun, x, y):
    return fun(x) + fun(y)


print(sumof_fun(len, "anand", "advika"))
