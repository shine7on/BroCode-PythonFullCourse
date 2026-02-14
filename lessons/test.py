def isValid(s: str):

        stack = []

        for char in s:
            # first in, last out
            if char == '{' or char == "(" or char == "[":
                stack.append(char)
                print(stack)
            elif char == "}" and stack.pop() != "{":
                return False
            elif char == ")" and stack.pop() != "(":
                return False
            elif char == "]" and stack.pop() != "[":
                return False
        
        return True

s = "[()]"
print(isValid(s))


s="Was it a car or a cat I saw?"

s = s.replace(" ", "").lower()
print(s)
for char in s:
    if char.isalpha() == False and char.isdigit() == False:
        s = s.replace(char, "")
        print(s)

rev = ""
for i in range(len(s)-1, 0, -1):
            rev += s[i]

print(rev)




