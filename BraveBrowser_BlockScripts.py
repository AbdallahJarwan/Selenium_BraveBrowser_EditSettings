
from seleniumwire import webdriver # to be able to use proxy
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

browser.get('brave://settings/shields')
''' Go to to brave://settings/shields
    Go to Block scripts toggle and inspect element
    Find the knob -> right-click -> copy -> JS_path
''' 
element_JS_path = 'document.querySelector("body > settings-ui").shadowRoot.querySelector("#main").shadowRoot.querySelector("settings-basic-page").shadowRoot.querySelector("#basicPage > settings-section:nth-child(7) > settings-default-brave-shields-page").shadowRoot.querySelector("#noScriptControlType").shadowRoot.querySelector("#control").shadowRoot.querySelector("#knob")'
browser.execute_script(f'return {element_JS_path}').click()

# Continue your work on the same brwoser
# browser.get('your webpage')
