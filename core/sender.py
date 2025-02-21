import time

CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"

def send_message(options, messages, phone, timeOutPerMessage):
  options.browser.get(CHAT_URL.format(phone=phone))

  for message in messages:    
    inp_xpath = (
    '/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]'
    )
    input_box = options.WebDriverWait(options.browser, 60).until(
        options.expected_conditions.presence_of_element_located((options.By.XPATH, inp_xpath))
    )
    input_box.send_keys(message)
    input_box.send_keys(options.Keys.ENTER)

    time.sleep(timeOutPerMessage)