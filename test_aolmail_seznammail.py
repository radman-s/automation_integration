from pages.drivers import Drivers
from pages.aol_mail_page import AolMailPage
from pages.seznam_page import SeznamPage
import time

# test descriptions
# send email from aol.mail using FIREFOX to seznam.mail using CHROME
# validate receiver's email, email subject and email message.

#  TEST DATA
user_aol = 'test.integrate_30100'
pw_aol = '123852_pw'
email_seznam = 'test.integrate20@seznam.cz'
user_seznam = 'test.integrate20'
pw_seznam = 'testpw_02'
subject = 'test'
msg = 'TEST TEST'

# open FIREFOX browser for AOL Mail
browser1 = Drivers('--start-maximized').firefox()
amp = AolMailPage(driver=browser1)

# test start
amp.go()

# login to AOL Mail
amp.aol_user_input.input_text(user_aol)
amp.user_next_button.click()
amp.aol_pw_input.input_text(pw_aol)
amp.pw_next_button.click()
amp.mail_button.click()

# switch to new tab opened
browser1.switch_to.window(browser1.window_handles[1])

# compose new email
amp.compose_button.click()
amp.to_input.input_text(email_seznam)
amp.subject_input.input_text(subject)
amp.message_input.input_text(msg)
amp.send_button.click()
# time sleep for the email load to sent folder
time.sleep(2)

# go to sent folder
amp.sent_button.click()
amp.aol_select_email.click()

# collect data from sent folder
aol_sub = amp.aol_text_subject.text
aol_to = amp.aol_text_to.text
aol_msg = amp.aol_text_msg.text
aol_dat_tim = amp.aol_date_time.text

# delete email from sent folder
amp.aol_delete.click()

# open CHROME browser for  SEZNAM Mail
browser2 = Drivers('--start-maximized').chrome()
sp = SeznamPage(driver=browser2)

sp.go()

# login to SEZNAM Mail
sp.s_user_input.input_text(user_seznam)
sp.s_pw_input.input_text(pw_seznam)
sp.s_toemail_button.click()

# open email received from AOL Mail
sp.s_select_email.click()

# collect data: RECIVER EMAIL, EMAIL SUBJECT, EMAIL CONTENT(msg)
s_to = sp.s_text_to.text
s_sub = sp.s_text_subject.text
s_msg = sp.s_text_msg.text

# delete email
sp.s_delete_mail.click()

assert aol_to == s_to
assert aol_sub == s_sub
assert aol_msg == s_msg

print(f'receiver email: {aol_to} = {s_to}')
print(f'email subject:  {aol_sub} = {s_sub}')
print(f'email content:  {aol_msg} = {s_msg}')
print()
print('test passed')

browser1.quit()
browser2.quit()












