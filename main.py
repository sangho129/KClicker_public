from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
#import threading

def worker():
    while(True):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("disable-infobars")
            options.add_argument('--blink-settings=imagesEnabled=false')
            options.add_argument("--disable-extensions")
            options.add_argument('incognito')
            options.add_argument('--mute-audio')
            options.add_argument("no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            browser = webdriver.Chrome(chrome_options=options)
            browser.get("https://kschoolclick.netlify.app/")
            browser.execute_script("localStorage.setItem('schoolName', 'KsCtOoL(유성중)');")
            browser.execute_script("localStorage.setItem('schoolCode', '7451054');")
            browser.refresh()
            browser.find_element(By.CSS_SELECTOR, "body > main > div.alert-container.svelte-lsgmqq > div > span.close.fontSize.svelte-lsgmqq").click()
            browser.execute_script("""var event = new KeyboardEvent('keydown', {
    key: 'g',
    ctrlKey: true
    });

    setInterval(function(){
    for (i = 0; i < 100; i++) {
    document.dispatchEvent(event);
    }
    }, 0);""")
            time.sleep(3600)
        except:
            pass
    

def main():
    # 스레드 삭재
    worker()

main()
