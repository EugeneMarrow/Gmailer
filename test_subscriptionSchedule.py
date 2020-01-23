#coding: utf-8 
from conftest import *

class Email:
    def __init__(self, recepient, subject,body):
        self.recepient = recepient
        self.subject = subject
        self.body = body

def randstring():
    rands=[] 
    for x in range(2):
        rands.append(''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)]))
    return rands

def create_message():
	rands=randstring()
	message=Email(log,rands[0],rands[1])
	return message

def send_message(driver,msg):
	global message
	message=msg
	find(By.XPATH,"//*[contains(text(), 'Compose') and @role='button']",driver).click()
	find(By.XPATH,"//*[@name='to' and @role='combobox']",driver).send_keys(message.recepient)
	find(By.XPATH,"//*[@name='subjectbox' and @placeholder='Subject']",driver).send_keys(message.subject)
	find(By.XPATH,"//*[@role='textbox' and @aria-label='Message Body']",driver).send_keys(message.body)
	find(By.XPATH,"//*[@role='button' and @aria-label='Send ‪(Ctrl-Enter)‬']",driver).click()
	sleep(5)


def check_message(driver):
	global subj, text, messages
	messages=driver.find_elements(By.XPATH,".//tr[@role='row']")
	subj=messages[1].find_element(By.XPATH,"//tr[1]/td[6]/div/div/div/span/span").text
	text=messages[1].find_element(By.XPATH,"//tr[1]/td[6]/div/div/span").text[4:]
	assert messages[1].find_element(By.XPATH,"//tr[1]/td[5]/div[2]/span/span").get_attribute("email")==message.recepient
	assert subj in message.subject
	message.body=message.body.replace("\n","")
	message.body=message.body.replace(" ","")
	text=text.replace(" ","")
	assert text in message.body

def send_summary(driver,dicto_messages):
	summarytext=""
	for key in dicto_messages:
		letters=re.findall(r'[A-Za-z]', dicto_messages[key])
		numbers=re.findall(r'\d', dicto_messages[key])
		summarytext=summarytext+"Received mail on theme: " +key+ " with message: " +dicto_messages[key]+". \nIt contains " +str(len(letters))+" letter(s) and "+str(len(numbers))+" number(s)\n\n"
	summary=Email(log,"Summary",summarytext)
	send_message(driver,summary)
	check_message(driver)
	

def test_landing(driver):
	msgdict={}
	for i in range(15):
		send_message(driver,create_message())
		check_message(driver)
		print "Successfully sent message #"+str(i+1)
		msgdict[subj]=text
	encoded_msgdict={ str(key):str(value) for key,value in msgdict.items() }
	send_summary(driver,encoded_msgdict)
	print "Successfully sent summary"
	i=1
	while i<=15:
		sel_button=messages[i].find_element(By.XPATH,".//td[2]/div")
		driver.execute_script("arguments[0].scrollIntoView();", sel_button)
		sel_button.click()
		i+=1
		if i==16:
			find(By.XPATH,"/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div/div[2]/div[3]",driver).click()
	print "Deleted"+ str(i-1) +"messages"
	sleep(5)