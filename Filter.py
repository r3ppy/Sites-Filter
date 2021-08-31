import requests, os, time, colored
from colored import fg, bg, attr
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from multiprocessing.pool import ThreadPool

# // drupal: /user/register - /user/login
# // Joomla: /administrator/index.php
# // WP:     /wp-login.php

os.system('cls')

print "%s%s\n\t\t  /\     /\\%s" % (fg(34), bg(0), attr(0)); time.sleep(0.1)
print "%s%s\t\t {  `---'  }%s" % (fg(34), bg(0), attr(0)); time.sleep(0.1)
print "%s%s\t\t {  O   O  }%s" % (fg(34), bg(0), attr(0)); time.sleep(0.1)
print "%s%s\t\t ~~>  V  <~~%s" % (fg(34), bg(0), attr(0)); time.sleep(0.1)
print "%s%s\t\t  \  \|/  /%s" % (fg(34), bg(0), attr(0)); time.sleep(0.1)
print "%s%s\t\t   `-----'____%s" % (fg(34), bg(0), attr(0)); time.sleep(0.1)
print '%s%s\t\t   /     \    \_     "R3ppy Sites Filter"%s' % (fg(34), bg(0), attr(0)); time.sleep(0.1)
print "%s%s\t\t  {       }\  )_\_   _\t 192.168.1.1%s" % (fg(34), bg(0), attr(0)); time.sleep(0.1)
print "%s%s\t\t  |  \_/  |/ /  \_\_/ )%s" % (fg(34), bg(0), attr(0)); time.sleep(0.1)
print "%s%s\t\t   \__/  /(_/     \__/%s" % (fg(34), bg(0), attr(0)); time.sleep(0.1)
print "%s%s\t\t     (__/\n%s" % (fg(34), bg(0), attr(0)); time.sleep(0.1)

ASK_FOR_FILE = open(raw_input("%s%sR3ppy Domains #~/ %s" % (fg(34), bg(0), attr(0))), "r").read().split("\n")

WP = 0
JO = 0
DU = 0
OT = 0

def Chk(URL_):
    global WP, JO, DU, OT
    if "https://" not in URL_ and "http://" not in URL_:
        URL_ = "https://"+URL_+""
    elif "https://" in URL_ or "http://" in URL_:
        URL_ = URL_
    else:
        pass
    # //////////////////////////////////////////////////
    SITE = ""
    try:
        Drupal = requests.get(URL_, timeout=5)
        if "Drupal.settings" in Drupal.content or "https://www.drupal.org" in Drupal.content:
            print "%s%s{}%s".format(URL_) % (fg(15), bg(0), attr(0)) + "%s%s [Drupal]%s" % (fg(34), bg(0), attr(0))
            DU+=1
            os.system("title "+ "@R3ppy Filter - Joomla: {}, drupal: {}, WordPress: {}, Other: {}".format(JO, DU, WP, OT))
            open("drupal.txt", "a+").write(URL_+"\n")
            SITE = "drupal"
    except:
        pass
    try:
        Joomla = requests.get(URL_, timeout=5)
        if 'content="joomla' in Joomla.content:
            print "%s%s{}%s".format(URL_) % (fg(15), bg(0), attr(0)) + "%s%s [Joomla]%s" % (fg(160), bg(0), attr(0))
            JO+=1
            os.system("title "+ "@R3ppy Filter - Joomla: {}, drupal: {}, WordPress: {}, Other: {}".format(JO, DU, WP, OT))
            open("Joomla.txt", "a+").write(URL_+"\n")
            SITE = "Joomla"
    except:
        pass
    try:
        WordPress = requests.get(URL_+"/wp-login.php", timeout=5)
        if "Powered by WordPress" in WordPress.content: 
            print "%s%s{}%s".format(URL_) % (fg(15), bg(0), attr(0)) + "%s%s [WordPress]%s" % (fg(6), bg(0), attr(0))
            WP+=1
            os.system("title "+ "@R3ppy Filter - Joomla: {}, drupal: {}, WordPress: {}, Other: {}".format(JO, DU, WP, OT))
            open("WordPress.txt", "a+").write(URL_+"\n")
            SITE = "WP"
    except:
        pass
    if SITE == "":
        # print "%s%s{}%s".format(URL_) % (fg(15), bg(0), attr(0)) + "%s%s [Other]%s" % (fg(15), bg(0), attr(0))
        OT+=1
        os.system("title "+ "@R3ppy Filter - Joomla: {}, drupal: {}, WordPress: {}, Other: {}".format(JO, DU, WP, OT))
    else:
        pass
    
if __name__ == '__main__':
	pool = ThreadPool(100)
	for _ in pool.imap_unordered(Chk, ASK_FOR_FILE):
		pass
