# app.py
from flask import Flask, render_template, request
from chat import chat
import asyncio
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def home():
    user_input = ""
    response = ""

    if request.method == 'POST':
        user_input = request.form['input_text']
        response = await chat(user_input)
        print(response)
    return render_template('index.html', user_input=user_input, response=response)

if __name__ == '__main__':
    app.run(debug=True)

