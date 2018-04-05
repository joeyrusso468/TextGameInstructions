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
generic_responses = ["Hmmmmm", "Interesting, tell me more.", "You don't say?"]
while(count < 7):
    s = s.strip().lower()
    if 'mother' in s:
        s = input("mother do you have a large family?\n")
    elif 'father' in s:
        s = input("sister do you have a large family?\n")
    elif 'sister' in s:
        s = input("do you have a large family?\n")
    elif 'brother' in s:
        s = input("do you have a large family?\n")
    elif 'what up' in s:
        s = input("What's your name?\n")
    elif 'hello' in s:
        s = input("What's your name?\n")
    elif 'hey there' in s:
        s = input("What is your name?\n")
    elif 'sports' in s:
        s = input("What is your favorite NFL Sports Team?\n")
    elif 'patriots' in s:
        s = input("Oh that team is garbage. I like the New York Giants and they beat the Patriots twice in the Superbowl.\n")
    elif 'giants' in s:
        s = input("The Giants are the Goat\n")
    elif 'eli manning' in s:
        s = input("that commerical with OBJ was actually amazing.\n")
    elif 'odell beckham jr' in s:
        s = input("that commercial with Eli was actually amazing.\n")
    elif 'fortnite' in  s:
        s = input("I love fortnite. I am a sweaty nerd for it.\n")
    elif 'food' in s:
        s = input("What's your favorite food?\n")
    elif 'pizza' in s:
        s = input("I love pizza too. You like jazz?\n")
    elif 'what is my name' in s:
        s = input("Your name is ' + uname + ' tough guy!\n")
        uname = s
    else:
        if count_generic_response < 2:
            count_generic_response += 1
        else:
            count_generic_response = 0
        s = input(generic_responses[count_generic_response] +"\n")
        
    count += 1
