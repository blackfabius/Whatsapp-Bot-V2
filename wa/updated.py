from selenium import webdriver

chromedriver = "chromedriver.exe"

driver = webdriver.Chrome(chromedriver)
driver.get("https://web.whatsapp.com/")

name = input("Spammopfer : ")
msg = input("Nachricht : ")
count = int(input("Wie viele Nachrichten? : "))
finish = 0

input("Enter drücken nach dem Qr-Code scan")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name("_2S1VP")

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name("_2lkdt")
    button.click()
    finish += 1
    print(finish)

if finish == count:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("----------------")
        print("Fertig!")
        print("----------------")
        exit()