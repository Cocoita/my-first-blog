if 3>2:
    print("It works!")
if 5>2:
    print("5 is indeed greater than 2")
else:
    print("5 is not greater than 2")
name = "Cocoa"
if name == "Mariza":
    print("Hey Mariza")
elif name == "Cocoa":
    print("Hey Cocoa!")
else:
    print("Hey anonymous!")
volume = 57
#Change the volume if it's too loud or too quiet
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 60:
    print("It's nice for backgroundmusic")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :-(")

#Change the volume if it's too loud or too quiet
if volume < 20 or volume >80:
    volume = 50
    print("That's better!")

def hi():
    print("Hi there!")
    print("How are you?")

hi()

def hello(name):
    if name == "Cocoa":
        print("Hi Cocoa")
    elif name == "Mariza":
        print ("Hi Mariza")
    else:
        print("Hi Anonymous")

hello(name)
hello("Cocoa")
hello("Mariza")
hello("Ana")

def hola(name):
    print("Hi " + name + "!")

hola("Cocoita")
