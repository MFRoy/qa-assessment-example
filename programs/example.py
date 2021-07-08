    # <QUESTION 1>

    # Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

    # <EXAMPLES>

    # endsPy("ilovepy") → True
    # endsPy("welovepy") → True
    # endsPy("welovepyforreal") → False
    # endsPy("pyiscool") → False

    # <HINT>

    # What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
def endsPy(input):
    a = input.lower()
    b = a[-2:0]
    for character in b:
        if b == 'py':
            return True
    # input= input.lower()
    # input=input[-2:0]
    # if input =="py":
    #     return True

input = "apy"
print(endsPy(input))

