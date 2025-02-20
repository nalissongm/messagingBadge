import sys
import pandas as pd

from PyQt5.QtWidgets import QApplication, QFileDialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

app = QApplication(sys.argv)

# def send_m0essage(self, messages, phone):
#   for message in messages:



def get_contact():
  file = QFileDialog.getOpenFileName(caption="CSV", filter="CSV (*.csv)")[0]

  allProfs = pd.read_csv(file, sep=",")

  profsNotContacted = allProfs.query("Contatado_ou_entregue==False & Exportado==True & Impresso==True")

  for id, prof in profsNotContacted.iterrows():
    print(prof["Nome completo"])

    phone = str(f'{prof["Telefone (opcional)"]:.0f}')

    if prof["Gostaria de ser notificado pelo WhatsApp?"] == "Sim" & phone.count() > 0:
      



get_contact()