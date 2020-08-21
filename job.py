import time
import re
import os
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import slackweb

SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')
GATHER_SPACE_URL = os.environ.get('GATHER_SPACE_URL')

def notify_slack(participants_num):
    if participants_num == 0:
        return
    slack = slackweb.Slack(url=SLACK_WEBHOOK_URL)
    message = f'*{participants_num}人* がバB419にいるよ'
    slack.notify(text=message, mrkdwn=True)
    print(f'send message successfully: {message}')

def get_chrome_driver(options):
    return webdriver.Chrome(options=options)

def get_participants_num(driver):
    driver.get(GATHER_SPACE_URL)
    time.sleep(20)
    driver.find_element_by_css_selector("div.GameBody-finish").click()
    time.sleep(3)
    participants_text = driver.find_element_by_css_selector(
        "div.u-header-text").text
    participants_num = re.search(r'\d+', participants_text).group(0)
    return int(participants_num) - 1

if __name__ == "__main__":
    options = Options()
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
    options.add_argument("--headless")
    driver = get_chrome_driver(options)
    try:
        notify_slack(get_participants_num(driver))
    except:
        traceback.print_exc()
    finally:
        driver.quit()
