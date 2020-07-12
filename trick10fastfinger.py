from selenium import webdriver  # import cái webdriver về
from selenium.webdriver.common.keys import Keys  # import Keys để gửi các kí tự lên web
import time  # time để spleep đợi load web

PATH = "C:\Program Files (x86)\chromedriver.exe"  # cái path này là vô chorme download chormedriver theo đúng phiên bản rồi vứt vô Files x86
driver = webdriver.Chrome(PATH)  # to chrome
driver.get("https://10fastfingers.com/typing-test/vietnamese")  # get cái link
time.sleep(3)  # đợi load trang web
while True:
    try:
        hightligtText = driver.find_element_by_css_selector("div#row1>span.highlight").text  # get cái text hightligh về
        input = driver.find_element_by_css_selector("#inputfield")  # get cái element để nhập từ khóa
        input.send_keys(hightligtText)  # gửi lên cái từ cần nhập
        input.send_keys(Keys.SPACE)  # gửi thêm cái nút space
    except:
        break
time.sleep(5)
driver.quit()
