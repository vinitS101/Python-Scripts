#Script for sending raids in the browser game www.travian.com
#The script uses pyautogui instead of selenium, etc so as to avoid bot detection by the game
#Make sure not to run the script at set intervals as that pattern can be detected

import pyautogui, webbrowser, time

#If not already logged in, refer to the login script to know how to do it and just add it here.
#Open tab for farmlist. (Change URL depending on your game server and domain.)
webbrowser.open('https://ts4.travian.com.au/build.php?tt=99&id=39')

#move scroll and click "N" number of times to get to the bottom of the Farmlist
time.sleep(6)

pyautogui.moveTo(1911,1006, duration = 0.5)

i = 1

while (i<=37):
	pyautogui.click()
	time.sleep(0.8)
	i=i+1

#move to check all and hit raid for 1st list.
pyautogui.moveTo(618, 803, duration = 0.7)
pyautogui.click()

pyautogui.moveTo(660, 884, duration = 0.8)
pyautogui.click()

time.sleep(3.5)

#move to the rest of the farmlists that have to be sent and repeat.
i = 1

while (i<=4):
	pyautogui.moveTo(1913, 110, duraion = 0.5)     #move to scroll and click to get to next FL
	pyautogui.click()
	pyautogui.moveTo(617, 829, duration = (0.12 + i*0.3))   #move to and click check all
	pyautogui.click()
	pyautogui.moveTo(655,908, duration = (i*0.3 + 0.2))      #move to and click Send Raid
	pyautogui.click()
	time.sleep(i*2+2)
	i=i+1




