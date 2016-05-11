__author__ = 'rh'
# doc: https://github.com/nickoala/telepot

import telepot
import inspect
import time
import pprint

# inspect.getmembers(telepot, predicate=inspect.ismethod)

dir(telepot)


# vvv
# (zeichenkette)  = "ich heisse alessio"
# print(zeichenkette)
# print(type(zeichenkette))
# new name

# print(type(a))
# a = 1.6
# print(type(a))


# ----------------------------------------------------

print (" ------------ telepot Anfang ")

bot = telepot.Bot('209638089:AAH6KrKt8kU6VC-nAQlpXgp-wsyUycMMiBs')
print bot.getMe()

# response = bot.getUpdates()
# print("response = "),
# pprint(response)

def milchflaschenalarm():
    mf = 7 #   milchflasche
    for mf in range (7,1, -1) :
        print mf
        if mf <= 3:
            # print "Es gibt zu wenig Milch!"
            nachricht = "Es gibt zu wenig Milch, nur noch " + str(mf)  + ' Flaschen'
            bot.sendMessage(217727356, nachricht )

def handle(msg):
    pprint.pprint(msg)
    # Do your stuff here ...

bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)






