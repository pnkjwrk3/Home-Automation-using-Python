import RPi.GPIO as GPIO
import urllib2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
true = 1
while(true):
                try:
                        response = urllib2.urlopen('http://192.168.0.105/buttonStatus.php')
                        status = response.read()
                except urllib2.HTTPError, e:
                                        print e.code

                except urllib2.URLError, e:
                                        print e.args                        
                if status=='ON1':
                        print status
                        GPIO.output(11,true)
                elif status=='OFF1':
                        print status
                        GPIO.output(11,false)
                elif status=='ON2':
                        print status
                        GPIO.output(12,true)
                elif status=='OFF2':
                        print status
                        GPIO.output(12,false)
                elif status=='ON3':
                        print status
                        GPIO.output(13,true)
                elif status=='OFF3':
                        print status
                        GPIO.output(13,false)
                elif status=='ON4':
                        print status
                        GPIO.output(15,true)
                elif status=='OFF4':
                        print status
                        GPIO.output(15,false)
