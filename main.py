import sys
import pandas as pd
import time

from PyQt5.QtWidgets import QApplication, QFileDialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from core.sender import send_message
from core.notification import notifiProfs


messages = [
  "Olá {name}, aqui é o José T.I. da Unific.",
  "Estou entrando em contato para informar que seu crachá já foi confeccionado e está disponível para retirada.",
  "A retirada pode ser realizada no financeiro da instituição."
]

BASE_URL = "https://web.whatsapp.com/"

def main():
  browser = webdriver.Chrome()

  options={browser,Keys,By,expected_conditions}

  file = QFileDialog.getOpenFileName(caption="CSV", filter="CSV (*.csv)")[0]

  allProfs = pd.read_csv(file, sep=",")

  notifiProfs(options, allProfs, messages)




app = QApplication(sys.argv)

# main()

proff = ['Pablo', 'tiburcio', 'sobreira', 'da', 'Cruz', '']

print(" ".join([proff][:2]))