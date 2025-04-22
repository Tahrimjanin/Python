# Local Scope
def local_scope():
    print("\n Local Scope")
    def myfunc():
        x = 300
        print("Inside myfunc:", x)
    myfunc()
    

#Function Inside Function
def function_inside_function():
    print("\n Function Inside Function")
    def myfunc():
        x = 300
        def myinnerfunc():
            print("Inside myinnerfunc:", x)
        myinnerfunc()
    myfunc()
   

# Example 3: Global Scope
def global_scope():
    print("Example 3: Global Scope")
    global x
    x = 300
    def myfunc():
        print("Inside myfunc:", x)
    myfunc()
    print("Outside function:", x)
    print("-" * 30)

# Example 4: Local vs Global Variable
def local_vs_global():
    print("Example 4: Local vs Global Variable")
    x = 300
    def myfunc():
        x = 200
        print("Inside myfunc (local x):", x)
    myfunc()
    print("Outside myfunc (global x):", x)
    print("-" * 30)

# Example 5: Using global keyword to create global variable
def global_keyword_create():
    print("Example 5: global keyword to CREATE global variable")
    def myfunc():
        global x
        x = 300
    myfunc()
    print("x after global creation:", x)
    print("-" * 30)

# Example 6: Using global keyword to MODIFY global variable
def global_keyword_modify():
    print("Example 6: global keyword to MODIFY global variable")
    global x
    x = 300
    def myfunc():
        global x
        x = 200
    myfunc()
    print("x after modification:", x)
    print("-" * 30)

# Example 7: Using nonlocal keyword
def nonlocal_keyword():
    print("Example 7: nonlocal keyword")
    def myfunc1():
        x = "Jane"
        def myfunc2():
            nonlocal x
            x = "hello"
        myfunc2()
        return x
    result = myfunc1()
    print("Value of x after nonlocal change:", result)
    print("-" * 30)

# Call each example one by one
local_scope()
function_inside_function()
global_scope()
local_vs_global()
global_keyword_create()
global_keyword_modify()
nonlocal_keyword()
