from flask import Flask
from flask import render_template
from flask import request
from random import randint

app = Flask(__name__)

south1 = ['地锅鸡', '干锅鸡', '石锅拌饭', '喜多多', '酸汤酥肉']
south2 = ['犀米家', '黄焖鸡', '肉糟饭', '饺子', '快餐', '香扒饭', '焗饭']


@app.route('/eating', methods=['GET', 'POST'])
def eating():
    choice = request.form.get('canteen')
    dish = "今天中午吃啥呢~~"
    if choice is '1':
        length = len(south1)
        num = randint(0, length - 1)
        dish = south1[num]
    elif choice is '2':
        length = len(south2)
        num = randint(0, length - 1)
        dish = south2[num]
    elif choice is '3':
        length = len(south1) + len(south2)
        num = randint(0, length - 1)
        if num < len(south1):
            dish = south1[num]
        else:
            dish = south2[num - len(south1)]
    return render_template('eating.html', dish=dish)


if __name__ == '__main__':
    app.run()
