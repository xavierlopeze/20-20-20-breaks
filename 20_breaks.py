import webbrowser
import time
import random
import threading

urls = ['https://www.youtube.com/watch?v=TKl6wLHdnRI',
		'https://www.youtube.com/watch?v=J8UBdolwpkI',
		'https://www.youtube.com/watch?v=iVJxDkD3X8Y',
		'https://www.youtube.com/watch?v=Bcow0tAjrhU',
		'https://www.youtube.com/watch?v=44AIJANDG90']
startingTime = 0
#webbrowser.open_new_tab(url + 'doc/')

def quit():
	if(input() =='q' ):
		endingTime = time.time();
		
		seconds = endingTime-startingTime
		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)

		print("\nEnding time: " + time.ctime(endingTime) )                                                                                         
		print("\nTotal time : {}h {}m {}s"  .format(h,m,s) )
		return

def perdiodicBrowserLaunch():
	while(1):
		url = random.choice(urls)
		webbrowser.open_new(url)
		time.sleep(20*60*60)

def init():
	
	print("\nUse the 20-20-20 rule. Every 20 minutes, take a 20-second break and focus your eyes on something at least 20 feet (6 meters) away .")
	print("\n'20_break.py' will open a browser every 20 min, press 'q' to quit")
	
	global startingTime
	startingTime = time.time()
	print("\nStarting time: " + time.ctime(startingTime) )


pbl = threading.Thread(target = perdiodicBrowserLaunch)
qt = threading.Thread(target = quit)

#The entire Python program exits when no alive non-daemon threads are left.
qt.setDaemon(False)
pbl.setDaemon(True)

init()
qt.start()
pbl.start()




