import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sys
import getpass
import threading
from time import sleep
from random import randint

k='''
your message is here
'''


class SenderTherad(threading.Thread):
    def __init__(self,to):
        threading.Thread.__init__(self)
        self.to=to

    def run(self):
        i=0
        try:
            form=''   #your email address
            msg=MIMEMultipart()
            msg['from']=form
            msg['to']=self.to
            msg['subject']='message::' #your subject
            number=randint(0,5)

            smtp_obj=smtplib.SMTP('smtp.gmail.com',587) #smtp conncetion for any maul service
            #password=getpass.getpass(prompt='Password: ')
            smtp_obj.starttls()
            password=''    #your email password
            smtp_obj.login(form,password)
            print '\n'
            while(i<50):  #update 50 for for your usage
                body=MIMEText(k)
                msg.attach(body)
                smtp_obj.sendmail(form,self.to,msg.as_string())
                #time.sleep(5)
                print i,self.to,'\n'
                i+=1
            print '\n'

        except:
            print "error::",sys.exc_info()[1],' ::',sys.exc_info()[0]
        finally:
            smtp_obj.quit()



def main():
    try:
    	# temp.123@exmaple.com
        p='' #this will contain @example.com
        to=[''] #this will contain temp.123 or more can be added to it 
        k=len(to)
        l=list()
        for i in range(k):
            l.append(SenderTherad(to[i]+p))
            l[i].start()

        for i in range(k):
            l[i].join()

        print "finished"


    except:
        print "error::",sys.exc_info()[1],' ::',sys.exc_info()[0]
    finally:
        print 'end'
        sleep(600)
        main()
        #smtp_obj.quit()

if __name__ == '__main__':
    main()
