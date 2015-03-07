#!/usr/bin/python

import sys
import base


com = base.Controller()
first = sys.argv[0]

if (first == 'addkey'):
    if(len(sys.argv) != 3):
        print "Incorrect number of parameters"
        return
    user = sys.argv[1]
    key = sys.argv[2]

    con.addsshkey(user, key)
    return

elif (first == 'removekey'):
    if(len(sys.argv) != 2):
        print "Incorrect number of parameters"
        return

    user = sys.argv[1]

    con.deleteallkeys(user)
    return

elif (first == 'changekey'):
    if(len(sys.argv) != 3):
        print "Incorrect number of parameters"
        return
    user = sys.argv[1]
    key = sys.argv[2]

    con.modifykey(user, key)
    return

