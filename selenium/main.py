from selenium import webdriver
#webdriver allows us to drive the web through code
chrome_browser = webdriver.Chrome("./chromedriver")
#./chromedriver is the path to the chromedriver.exe file
#if this is on a hard drive and not Replit, it would be
#restofpath.chromedriver_win32/chromedriver.exe
print(chrome_browser)
#chrome_browser.maximize_window_()
#maximizes the browser window