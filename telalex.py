__author__ = 'ak-rh'
__version__= '0.2'
# doc: https://github.com/nickoala/telepot


import telepot
import inspect
import time
import pprint
import telegram_token

# pprint.pprint (dir(telepot.Bot))

TOKEN = telegram_token.TOKEN
id    = telegram_token.id

bot = telepot.Bot(TOKEN)

# response = bot.getUpdates()
# print("response = "),
# pprint(response)


def ini_telalex():
    print (" - telepot Anfang - ")
    print bot.getMe()
    print 'nach getme'


def milchflaschenalarm():
    mf = 7 #   milchflasche
    for mf in range (7,1, -1) :
        print mf
        if mf <= 3:
            # print "Es gibt zu wenig Milch!"
            nachricht = "Es gibt zu wenig Milch, nur noch " + str(mf)  + ' Flaschen'
            bot.sendMessage(id, nachricht )

def handle(msg):
    print '###################'
    pprint.pprint(msg)
    # pprint.pprint(msg['text'])
    # print msg['text']
    print '-------------------'
    for key in msg:
        print key, ':', msg[key]
    # content_type, chat_type, chat_id = telepot.glance(msg)
    # print (content_type, chat_type, chat_id)
    # # Do your stuff here ...


if __name__ == '__main__':
    ini_telalex()
    print 'message_loop'
    bot.message_loop(handle)

    print ('Listening ...')
    #  Keep the program running.
    while 1:
        time.sleep(10)
