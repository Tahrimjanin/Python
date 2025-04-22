# Original string
text = "  hello, Python World!  "

print("Original:", repr(text))

# capitalize()
print("capitalize():", text.capitalize())

# casefold()
print("casefold():", text.casefold())

# center()
print("center(30):", text.center(30, '-'))

# count()
print("count('o'):", text.count('o'))

# encode()
print("encode():", text.encode())

# endswith()
print("endswith('World!'):", text.endswith("World!"))

# expandtabs()
tabbed = "Hello\tWorld"
print("expandtabs():", tabbed.expandtabs(4))

# find()
print("find('Python'):", text.find("Python"))

# format()
name = "Tahrim"
print("format():", "My name is {}".format(name))

# index()
print("index('Python'):", text.index("Python"))

# isalnum()
print("'Hello123'.isalnum():", "Hello123".isalnum())

# isalpha()
print("'Hello'.isalpha():", "Hello".isalpha())

# isascii()
print("'Hello'.isascii():", "Hello".isascii())

# isdecimal()
print("'123'.isdecimal():", "123".isdecimal())

# isdigit()
print("'1234'.isdigit():", "1234".isdigit())

# isidentifier()
print("'my_var'.isidentifier():", "my_var".isidentifier())

# islower()
print("'hello'.islower():", "hello".islower())

# isnumeric()
print("'12345'.isnumeric():", "12345".isnumeric())

# isprintable()
print("'Hello\\n'.isprintable():", "Hello\n".isprintable())

# isspace()
print("'   '.isspace():", "   ".isspace())

# istitle()
print("'Hello World'.istitle():", "Hello World".istitle())

# isupper()
print("'HELLO'.isupper():", "HELLO".isupper())

# join()
print("join(['a','b','c']):", "-".join(['a', 'b', 'c']))

# ljust()
print("ljust(20):", "Hello".ljust(20, '*'))

# lower()
print("lower():", text.lower())

# lstrip()
print("lstrip():", text.lstrip())

# maketrans() + translate()
table = str.maketrans("ae", "12")
print("translate():", "apple".translate(table))

# partition()
print("partition('Python'):", text.partition("Python"))

# replace()
print("replace('Python', 'Java'):", text.replace("Python", "Java"))

# rfind()
print("rfind('o'):", text.rfind('o'))

# rindex()
print("rindex('o'):", text.rindex('o'))

# rjust()
print("rjust(20):", "Python".rjust(20, '-'))

# rpartition()
print("rpartition('o'):", text.rpartition('o'))

# rsplit()
print("rsplit():", text.rsplit())

# rstrip()
print("rstrip():", text.rstrip())

# split()
print("split():", text.split())

# splitlines()
multi_line = "Line1\nLine2\nLine3"
print("splitlines():", multi_line.splitlines())

# startswith()
print("startswith('  hello'):", text.startswith("  hello"))

# strip()
print("strip():", text.strip())

# swapcase()
print("swapcase():", text.swapcase())

# title()
print("title():", text.title())

# upper()
print("upper():", text.upper())

# zfill()
print("'42'.zfill(5):", "42".zfill(5))
