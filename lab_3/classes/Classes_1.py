class InputString():
    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        return self.string.upper()
    
str_1 = InputString(str(input()))
print(str_1)
