__author__ = 'rh'
# doc: https://github.com/nickoala/telepot

import telepot
import inspect
from pprint import pprint

inspect.getmembers(telepot, predicate=inspect.ismethod)

dir(telepot)

def handle(msg):
    pprint(msg)

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
# bot.message_loop(handle)
# bot.message_loop(handle)
print bot.getMe()

response = bot.getUpdates()

pprint(response)

mf = 7 #   milchflasche
for mf in range (7,1, -1) :
    print mf
    if mf <= 3:
        # print "Es gibt zu wenig Milch!"
        nachricht = "Es gibt zu wenig Milch, nur noch " + str(mf)  + ' Flaschen'
        bot.sendMessage(217727356, nachricht )







