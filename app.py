from flask import Flask, jsonify
from selenium.webdriver.chrome.options import Options
from job import get_chrome_driver, get_participants_num

app = Flask(__name__)

@app.route("/participants-num", methods=['GET'])
def participants_num():
    options = Options()
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
    options.add_argument("--headless")
    driver = get_chrome_driver(options)
    participants_num = get_participants_num(driver)
    if participants_num == 0:
        text = 'バB419には....誰もいません... :crying:'
    else:
        text = f'*{participants_num}人* がバB419にいるよ'
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run()
