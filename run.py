#!/usr/bin/python

import sys
import base


con = base.Controller()
first = sys.argv[0]

if (first == 'addkey'):
    if(len(sys.argv) != 3):
        print "Incorrect number of parameters"
        sys.exit(1)
    user = sys.argv[1]
    key = sys.argv[2]
    print "Adding key for " + user

    con.addsshkey(user, key)
    sys.exit()

elif (first == 'removekey'):
    if(len(sys.argv) != 2):
        print "Incorrect number of parameters"
        sys.exit(1)

    user = sys.argv[1]
    print "Removing key for " + user

    con.deleteallkeys(user)
    sys.exit()

elif (first == 'changekey'):
    if(len(sys.argv) != 3):
        print "Incorrect number of parameters"
        sys.exit(1)
    user = sys.argv[1]
    key = sys.argv[2]
    print "Changing key for " + user

    con.modifykey(user, key)
    sys.exit()
else:
    print """Available commands are:
    addkey <username> <key>
    removekey <username>
    changekey <username> <key>"""

