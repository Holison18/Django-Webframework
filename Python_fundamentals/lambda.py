# Python Lambda function is a small anonymous function.
# A lambda function can take any number of expressions but have just one expression
# syntax: lambda argument(s) : expression

# increment x by 10
x = lambda a:a+10
print(x(10))

# lambda function with more than one arguments
m = lambda a,b: a*b
print(m(2,4))

# conditional checking using lambda function
format_numeric = lambda num: f"{num:e}" if isinstance(num,int) else f"{num:,.2f}"
print("Int formatting: ",format_numeric(100000))
print("Float formatting: ",format_numeric(999999.745334324))

# check if the string a user enters matches the require string
require = "name@123"
check = lambda response: "Correct Input" if response == require else "Wrong Input"
print(check("name@123"))
print(check("name@1"))
