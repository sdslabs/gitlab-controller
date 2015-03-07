#!/usr/bin/python

import sys
import base


if(len(sys.argv) < 2):
    print """Available commands are:
    addkey <username> <key>
    removekey <username>
    changekey <username> <key>"""
    sys.exit()

first = sys.argv[1]
con = base.Controller()
print first
if (first == 'addkey'):
    if(len(sys.argv) != 4):
        print "Incorrect number of parameters"
        sys.exit(1)
    user = sys.argv[2]
    key = sys.argv[3]
    print "Adding key for " + user

    con.addsshkey(user, key)
    sys.exit()

elif (first == 'removekey'):
    if(len(sys.argv) != 3):
        print "Incorrect number of parameters"
        sys.exit(1)

    user = sys.argv[2]
    print "Removing key for " + user

    con.deleteallkeys(user)
    sys.exit()

elif (first == 'changekey'):
    if(len(sys.argv) != 4):
        print "Incorrect number of parameters"
        sys.exit(1)
    user = sys.argv[2]
    key = sys.argv[3]
    print "Changing key for " + user

    con.modifykeys(user, key)
    sys.exit()
