import time

from core.sender import send_message

def notifiProfs(options, profs, messages):    
  profsNotContacted = profs.query("Contatado_ou_entregue==False & Exportado==True & Impresso==True")

  print("🎰 Iniciando mensagens...")

  done = []
 
  for id, prof in profsNotContacted.iterrows():
    phone = str(f'{prof["Telefone (opcional)"]:.0f}')

    if (prof["Gostaria de ser notificado pelo WhatsApp? "] == "Sim") and (len(phone) > 0):
      shortName = " ".join([][:2])

      print("<--------------->")
      print("🎯 " + prof["Nome completo"])

      try:
        # send_message(
        #   options,
        #   messages=[messages[0].format(name=shortName), messages[1], messages[2]], 
        #   phone="+55{phone}".format(phone=phone),
        #   timeOutPerMessage=3
        # )
        print(prof["Nome completo"].split(sep=" "))

        done.append(prof["Nome completo"])

        time.sleep(3)
      except Exception as e:
        print(e)
      
    print(done)