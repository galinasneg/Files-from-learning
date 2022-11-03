import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service('C:/PyTest/chromedriver.exe')
driver = webdriver.Chrome(service=s)

class PasVal:
    def __init__(self, path_css,path_x,path_id,value):
        self.path_css = path_css
        self.path_x = path_x
        self.path_id = path_id
        self.value = value

sname = PasVal("","","surname","Филимонов")
name = PasVal("","","name","Олег")
fname = PasVal("","","patronymic","Геннадьевич")
pseria = PasVal("","","passportSeries","1234")
pnum = PasVal("","","passportNumber","123456")
pcode = PasVal("","","code","123456")
snils = PasVal("","","cardId","12345678901")
codepodr = PasVal("","","issued","Отдел уфмс такой-то")
phone = PasVal("","","phone","1234567890")
checkBox = PasVal("","","privacy","")
adress = PasVal(".vue-dadata__input","//*[@id='address']/div/div/input","","г Новосибирск, ул Новогодняя, д 47, кв 4")

dateBithday = PasVal("#birthday .mx-input","","","11.11.2001")
dateGive = PasVal("#dateOfIssue .mx-input","","","01.01.2018")
filePasport = PasVal(".upload-widget > input","","","C:\\1564-герб-золото.png")

formPassport = [sname,name,fname,pseria,pnum,pcode,snils,codepodr,phone,dateBithday,dateGive,adress]

# Зайти на сайт
driver.get("https://qa.neapro.site/login")
# Размер окна установить 1/2 моего экрана
driver.set_window_size(955,1060)
# Ввод логина/пароля пользователя с документами в статусе ожидания
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("gsnegireva@ngs.ru")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("1010101088")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(5)
# Открыть форму Паспорт
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
time.sleep(1)
# Заполнение полей формы паспорта
i = 0
while i < len(formPassport):
    # Fill Fields by ID
    if formPassport[i].path_id != "":
        driver.find_element(By.ID, formPassport[i].path_id).clear()
        driver.find_element(By.ID, formPassport[i].path_id).send_keys(formPassport[i].value)
        time.sleep(1)
        i += 1
    # Fill Fields by CSS
    elif formPassport[i].path_css != "":
        driver.find_element(By.CSS_SELECTOR, formPassport[i].path_css).clear()
        driver.find_element(By.CSS_SELECTOR, formPassport[i].path_css).send_keys(formPassport[i].value)
        time.sleep(1)
        i += 1

# Подтвердить адрес (кликнуть по строке в выпавшем списке)
driver.find_element(By.CSS_SELECTOR, "#address mark").click()
time.sleep(1)
# Прикрепить файл паспорта
driver.find_element(By.CSS_SELECTOR, filePasport.path_css).send_keys(filePasport.value)
driver.execute_script("window.scrollTo(0, 1080)")
# Send Form
driver.find_element(By.CSS_SELECTOR, ".fill").click()