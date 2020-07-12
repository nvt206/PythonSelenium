from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://quizlet.com/vi")
username=""#username account quizlet
password=""#password quizlet

try:
    linkSignin = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".SiteHeader-signIn"))
    )
    linkSignin.click()
    u = driver.find_element_by_id('username')
    p = driver.find_element_by_id('password')
    b = driver.find_element_by_css_selector('button[type="submit"]')
    u.send_keys(username)
    p.send_keys(password)
    b.click()
    createLink = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"SiteNav-menuItemTitle") and contains(text(),"Thư mục")]'))
    )
    createLink.click()

    # UILinkBox =WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"UILinkBox-link") and contains(text(),"Từ vựng")]'))
    # )
    # UILinkBox.click()
    driver.get("https://quizlet.com/create-set?inFolder=79649889")
    time.sleep(1)
    buttonClose = driver.find_element_by_css_selector('.UILink.UILink--revert[type="button"]')
    buttonClose.click()
    time.sleep(1)
    header = driver.find_element_by_css_selector('.AutoExpandTextarea-textarea[tabindex="5"]')
    header.send_keys("700 bài code thiếu nhi")
    description = driver.find_element_by_css_selector('.AutoExpandTextarea-textarea[tabindex="6"]')
    description.send_keys("code code code and code")

    jsonWords = [{"eng": "article", "vi": "bài báo"}, {"eng": "schedule", "vi": "lịch trình / lên lịch"},
                 {"eng": "attend", "vi": "tham dự"}, {"eng": "according to", "vi": "theo như"},
                 {"eng": "during", "vi": "trong suốt"}, {"eng": "deliver", "vi": "giao (hàng...)"},
                 {"eng": "there is", "vi": "có"}, {"eng": "expect", "vi": "trông đợi"},
                 {"eng": "director", "vi": "giám đốc"}, {"eng": "advertise", "vi": "quảng cáo"},
                 {"eng": "charge", "vi": "phí / tính phí"}, {"eng": "mention", "vi": "đề cập"},
                 {"eng": "quality", "vi": "chất lượng"}, {"eng": "publish", "vi": "xuất bản"},
                 {"eng": "arrive", "vi": "đến"}, {"eng": "discuss", "vi": "bàn bạc / thảo luận"},
                 {"eng": "opportunity", "vi": "cơ hội"}, {"eng": "guest", "vi": "khách"}, {"eng": "rent", "vi": "thuê"},
                 {"eng": "president", "vi": "chủ tịch"}, {"eng": "convenient", "vi": "tiện lợi"},
                 {"eng": "look forward", "vi": "trông đợi"}, {"eng": "in order to", "vi": "để (làm gì đó)"},
                 {"eng": "reduce", "vi": "giảm"}, {"eng": "serve", "vi": "phục vụ"}, {"eng": "parking", "vi": "đỗ xe"},
                 {"eng": "seminar", "vi": "hội thảo"}, {"eng": "regular", "vi": "thường xuyên / thường"},
                 {"eng": "soon", "vi": "sớm"}, {"eng": "invest", "vi": "đầu tư"},
                 {"eng": "compete", "vi": "cạnh tranh"}, {"eng": "produce", "vi": "sản xuất / tạo ra"},
                 {"eng": "around", "vi": "xung quanh / khoảng"}, {"eng": "attach", "vi": "đính kèm"},
                 {"eng": "prepare", "vi": "chuẩn bị"}, {"eng": "encourage", "vi": "khuyến khích"},
                 {"eng": "decide", "vi": "quyết định (v)"}, {"eng": "stay", "vi": "ở"},
                 {"eng": "theater", "vi": "nhà hát / rạp phim"}, {"eng": "presentation", "vi": "buổi thuyến trình"},
                 {"eng": "government", "vi": "chính phủ"}]
    lengtWords = len(jsonWords)
    while lengtWords > 5:
        btnAddCard = driver.find_element_by_xpath('//button[@aria-label="+ Thêm thẻ"]')
        btnAddCard.click()
        time.sleep(1)
        lengtWords -= 1
    pTag = driver.find_elements_by_css_selector('.ProseMirror[tabindex="7"]>p')
    print(len(pTag))
    for x in range(len(jsonWords)):
        driver.execute_script("arguments[0].textContent = arguments[1];", pTag[2 * x], jsonWords[x]["eng"])
        driver.execute_script("arguments[0].textContent = arguments[1];", pTag[2 * x + 1], jsonWords[x]["vi"])

    time.sleep(3)
    btnSubmit = driver.find_element_by_xpath('//button[@class="UIButton UIButton--hero"][@type="button"]')
    btnSubmit.click()
    # time.sleep(1)
    # choose = driver.find_element_by_xpath(
    #     '//div[@class="LanguageBarSide has-error"]')
    # choose.click()
    # en = driver.find_element_by_xpath(
    #     '//div[@select="UILink is-Popover is-Tooltip UIOverlayTrigger-target"][@tabindex="-1"]/option[@value = "en"]')
    # en.click()
    # time.sleep(10)
finally:
    time.sleep(10)
    driver.quit()
