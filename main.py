import sys
import pandas as pd
import time

from PyQt5.QtWidgets import QApplication, QFileDialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

app = QApplication(sys.argv)

messages = [
  "Olá {name}, aqui é o José T.I. da Unific.",
  "Estou entrando em contato para informar que seu crachá já foi confeccionado e está disponível para retirada.",
  "A retirada pode ser realizada no financeiro da instituição."
]

browser = webdriver.Chrome()

BASE_URL = "https://web.whatsapp.com/"
CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"

def send_message(messages, phone):
  browser.get(CHAT_URL.format(phone=phone))
  time.sleep(3)

  for message in messages:
    print("Message: " + message)
    
    inp_xpath = (
    '/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]'
    )
    input_box = WebDriverWait(browser, 60).until(
        expected_conditions.presence_of_element_located((By.XPATH, inp_xpath))
    )
    input_box.send_keys(message)
    input_box.send_keys(Keys.ENTER)

    time.sleep(3)


def main():
  file = QFileDialog.getOpenFileName(caption="CSV", filter="CSV (*.csv)")[0]

  allProfs = pd.read_csv(file, sep=",")

  profsNotContacted = allProfs.query("Contatado_ou_entregue==False & Exportado==True & Impresso==True")

  print(profsNotContacted)

  print("🎰 Iniciando mensagens...")

  done = []
 
  for id, prof in profsNotContacted.iterrows():
    phone = str(f'{prof["Telefone (opcional)"]:.0f}')

    if (prof["Gostaria de ser notificado pelo WhatsApp? "] == "Sim") and (len(phone) > 0):
      print("<--------------->")
      print("🎯 " + prof["Nome completo"])

      arrName = str(prof["Nome completo"]).split(sep=" ")

      shortname = "{name} {lastname}".format(name=arrName[0], lastname=arrName[1])

      try:
        send_message(
          [messages[0].format(name=shortname), messages[1], messages[2]], 
          phone="+55{phone}".format(phone=phone)
        )

        done.append(prof["Nome completo"])

        time.sleep(3)
      except Exception as e:
        print(e)
      
    print(done)



main()