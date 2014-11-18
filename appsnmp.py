#/usr/bin/python
# -*- coding: utf-8 -*-
#########################
# Application SNMP      #
# Karim Ayari           #
# DSI                   #
# Rectorat de Lyon      #
#########################
 

from flask import Flask,request,render_template,flash,redirect,url_for,make_response
from utils import getsnmp,basetab,fping
from commands import getstatusoutput

import sys, time, os
from daemon import Daemon

class MyDaemon(Daemon):
        def run(self):
                while True:
                        app.run(host='127.0.0.1')

app = Flask(__name__)
app.secret_key='weBaPp'


@app.route('/',methods=['GET','POST'])
def index():
    """
    """
    lst=[]
    getbddata=None
    state_ping=None
    if request.args.get('iprouteur') is not None:
        iprouteur1=request.args['iprouteur']
        getbddata=basetab(iprouteur1)
        resultat=getsnmp(iprouteur1)
	lst.append(iprouteur1)
        for val in resultat:
	    lst.append(val)
	state_ping=fping(lst[2])
    return render_template('snmp.html', titre="Application flask",lst=lst,data=getbddata,state_ping=state_ping)


if __name__ == "__main__":
        daemon = MyDaemon('/var/run/appsnmp.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)
