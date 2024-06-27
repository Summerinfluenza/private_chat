# app.py
from flask import Flask, render_template, request
from chat import chat
from image import generate_image
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def home():
    user_input = ""
    response = ""
    generation_type =""

    if request.method == 'POST':
        user_input = request.form['input_text']
        generation_type = request.form['generation_type']

        if generation_type == "text":
            response = await chat(user_input)
        elif generation_type == "image":
            response = await generate_image(user_input)
    print(response)
    return render_template(
        'index.html', 
        user_input=user_input, 
        response=response, 
        generation_type=generation_type)

if __name__ == '__main__':
    app.run(debug=True)

