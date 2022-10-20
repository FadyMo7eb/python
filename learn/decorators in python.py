def uppercase_decorator(function):
    def warapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return warapper
def split_string(function):
    def warapper():
        func=function()
        splitted_string=func.split()                                       # when you make fun inside it make it in pritn def() but if it only fun make it fun in print 
        return splitted_string
    return warapper
def make_it_for(function):
    def fr ():
        return tuple(function())
    return fr 
def make_it_stringg(function):
    def make_it_a_string():
        global rr
        rr=str(function())
    make_it_a_string()
    def repet_it():
        ss=rr+"HELLO,AGAIN"
        return ss
    return repet_it
@make_it_stringg        # 4
@make_it_for            # 3
@split_string           # 2
@uppercase_decorator    # 1
def say_hi():
    return "hello,fady"
print(say_hi())

