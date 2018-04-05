#Adventure Game

default_greeting =  "Hello User, This"
default_greeting += " is an adventure"
default_greeting += " game that takes"
default_greeting += " place in a high"
default_greeting += " school setting"
default_greeting += " where you get to"
default_greeting += " experience the choices"
default_greeting += " of a high school teenager."
default_greeting += " Let's begin, what's your name?"
print(default_greeting)
count = 0
if(count == 10):
    s = input('Do you want to exit the Adventure game?\n')
    s = s.strip().lower()
    if((s == "yes")
       or(s == "ya")
       or(s == "sure")
       or(s == "okay")
       or(s == "shore")
       or(s == "hi")
       or(s == "ya")
       or(s == "yuh")
       or(s == "maybe")           or(s == "of course")):
        count = 0
    else:
        if len(uname) < 1:
            print('Good bye, thanks for trying the Adventure Game')
        else:
            print('Good bye, ' + uname + ' and thanks for trying the Adventure Game')

