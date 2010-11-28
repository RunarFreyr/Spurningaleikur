#!/usr/bin/python
#encoding: utf-8

from subprocess import call, Popen
import os
import urllib2
import threading
import sys
from time import sleep
class ServerThread(threading.Thread):
    def run(self):
        call(["python","%s/kaka/manage.py"  % os.getcwd(), "runserver", "127.0.0.1:8000"])

if __name__ == "__main__":
    print os.getcwd()
    try:
        import django
    except:
        print "Django ekki installað... set upp Django"
        call(["python", os.getcwd()+"/djangoinstall/setup.py", "install"])
    else:
        print "Django er installað..."
    
    print "Set réttar slóðir inn í settings skjalið"
    f = open('%s/kaka/settings.py' % os.getcwd(), 'r')
    settings_file = f.read()
    f.close()
    f = open('%s/kaka/settings.py' % os.getcwd(), 'w')
    f.write(settings_file.replace("OUR_TEMPLATE_DIR", os.getcwd()+"/kaka/templates/"))
    f.close()
    print "Búinn að setja réttar slóðir inn í settings skjal"
    
    print "Keyri Unit Test... Prufar bæði business logic og UI test líka"
    print "Keyri: %s/kaka/manage.py test" % os.getcwd()
    call(["python", "%s/kaka/manage.py" % os.getcwd(),"test"])
    
    #edit settings skjalið með slóð að templates
    print "Keyri code coverage"
    print "Keyri upp kerfi og athuga hvort það virki ekki"
    t = ServerThread()
    t.start()
    sleep(3)
    try:
        response = urllib2.urlopen('http://127.0.0.1:8000')
    except:
        print "Villa, vefþjónninn keyrði sig ekki rétt upp"
        sys.exit(0)
    else:
        print "Vefþjónn keyrði sig upp fínt"
        sys.exit(0)