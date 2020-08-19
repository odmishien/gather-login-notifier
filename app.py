from flask import Flask, jsonify
from job import get_chrome_driver, get_participants_num

app = Flask(__name__)

@app.route("/participants-num", methods=['GET'])
def participants_num():
    options = Options()
    options.add_argument("--headless")
    driver = get_chrome_driver(options)
    participants_num = get_participants_num(driver)
    if participants_num == 0:
        text = 'バB419には....誰もいません... :crying:'
    else:
        text = f'*{participants_num}人* がバB419にいるよ'
    return jsonify({"text": text})

if __name__ == '__main__':
    app.run()
