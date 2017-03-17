import os, time
from selenium import webdriver

def register(user_id, user_pass, mess_no, do_not_disturb):
	#select the driver
	if do_not_disturb == True:
		driver = webdriver.PhantomJS()
	else:
		driver = webdriver.Chrome()
	#open registration site, send your id, pass, mess no and hit enter
	driver.get("http://swd.bits-hyderabad.ac.in/mess.php")
	try:
		break_variable = 1
		f201yxxx = driver.find_element_by_name('login')
		f201yxxx.send_keys(user_id)

		passw = driver.find_element_by_name('password')
		passw.send_keys(user_pass)

		mess1 = driver.find_element_by_xpath('//option[@value=1]')
		mess2 = driver.find_element_by_xpath('//option[@value=2]')

		if mess_no == 1:
			mess1.click()
		elif mess_no == 2:
			mess2.click()

		submit_button = driver.find_element_by_xpath('//button[contains(text(), "Submit")]')
		submit_button.click()
		break_variable = 0
		driver.close()
	except:
		#if error occurs during registration process
		break_variable = 1
	
	return break_variable,driver

def try_to_register(user_id, user_pass, mess_no, do_not_disturb=False):
	print("Registration process started...")
	while(1):
		break_variable, driver = register(user_id,user_pass, mess_no, do_not_disturb)
		if break_variable == 0:
			print("REGISTERED TO MESS: " + str(mess_no))
			break
		else:
			driver.close()
		time.sleep(10)

if __name__ == '__main__':
	"""
	::>::enter your id in place of user_id
	::>::enter your password in place of user_pass
	::>::enter mess no to register to; 	Enter:	1 (for Mess 1)
					   		2 (for Mess 2)	
	::>::to turn on do not disturb mode:
		     *	in dnd mode, you    > would be registered to your mess
				              without any chrome pop outs (occuring
					      every 10 seconds) 
					    > won't be able to see how fast you are
					      registed to mess :p
		     *	write: True  to enable  dnd mode
			       False to disable dnd mode
			       'T' and 'F' in capitals
	::>::EXP: 
			try_to_register('f201yxxx','*****', 1, True)
			id no and password IN quotes
			mess no and True/False are WITHOUT quotes
	"""
	
	try_to_register('user_id','user_pass', 1, True)
