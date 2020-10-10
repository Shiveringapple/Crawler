from selenium.webdriver import Chrome
driver = Chrome("./chromedriver")
# 打開網址
driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F%253Fgl%253DTW%2526hl%253Dzh-tw&hl=zh-TW&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
# find -> find_element
# find_all -> find elements
driver.find_element_by_id("identifierId").send_keys("imnovice8888@gmail.com")
driver.find_element_by_id("identifierNext").click() 



