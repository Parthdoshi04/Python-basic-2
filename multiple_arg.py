def myfu(*arg):
    for ar in arg:
        print(ar)
myfu('Hows','The','Josh?','\nHigh Sir')

def my(**kwargs):
    for x in kwargs.items():
        print(x)
my(e1="Namaskar",e2="Bhaiyo",e3="Ache Din",e4="Aaayege")
