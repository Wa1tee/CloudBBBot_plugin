"""A CloudBot plugin to find out when we last spoke about the company Big Bang Bandalores or BBB for short."""

from cloudbot import hook
import time

occurence = 0
last = 0
biggestDiff = 0

#find out mentions on channel
@hook.regex(r"*bbb*|*BBB*")
def read():
    occurence +=1
    now = gmtime()
    if biggestDiff < last - now:
        biggestDiff = last - now
    last = now 

@hook.command("trackbbb")
def start():
    last = gmtime()
    return "Tracking BBB"

#Return time since last occurence
@hook.command()
def bbb(message):
    now = gmtime()
    x = now - last
    m, s = divmod(x, 60)
    h, m = divmod(m, 60)

    m2, s2 = divmod(biggestDiff, 60)
    h2, m2 = divmod(m2, 60)
    message ("Last occurence of BBB was {} hours, {} minutes and {} seconds ago.\n".format(h, m, s)) 
    message ("The channel has been quiet about BBB at most for {} hours, {} minutes and {} seconds.\n".format(h2, m2, s2))
    message("BBB has been mentioned {} times in total".format(occurence)))
