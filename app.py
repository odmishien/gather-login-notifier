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


if __name__ == "__main__":
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(GATHER_SPACE_URL)
        time.sleep(5)
        driver.find_element_by_css_selector(
            "div.horizontal-container.action.test-yes-button").click()
        time.sleep(3)
        driver.find_element_by_css_selector(
            "div.horizontal-container.action.test-yes-button").click()
        time.sleep(5)
        participants_text = driver.find_element_by_css_selector(
            "span.u-header-text").text
        participants_num = re.search(r'\d+', participants_text).group(0)
        notify_slack(int(participants_num) - 1)
    except:
        traceback.print_exc()
    finally:
        driver.quit()
