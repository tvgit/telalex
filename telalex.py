

__author__ = 'rh'
# doc: https://github.com/nickoala/telepot

import telepot
import inspect
import time
import pprint

inspect.getmembers(telepot, predicate=inspect.ismethod)

pprint.pprint (dir(telepot.Bot))


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

TOKEN = '209638089:AAH6KrKt8kU6VC-nAQlpXgp-wsyUycMMiBs'
id = '209638089'

# bot = telepot.Bot('209638089:AAH6KrKt8kU6VC-nAQlpXgp-wsyUycMMiBs')
bot = telepot.Bot(TOKEN)
print bot.getMe()
print 'nach getme'

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
            bot.sendMessage(id, nachricht )
def handle(msg):
    #pprint.pprint(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    print (content_type, chat_type, chat_id)
    # Do your stuff here ...

print 'message_loop'
bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)






