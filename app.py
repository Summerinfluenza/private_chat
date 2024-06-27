from flask import Flask, render_template, request
from chat import chat
from image import generate_image
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def home():
    user_input = ""
    response = ""
    generation_type =""

    try:
        if request.method == 'POST':
            # Escape user input to protect against injections
            user_input = escape(request.form['input_text'])
            generation_type = escape(request.form['generation_type'])

            # Validate generation_type
            if generation_type not in ["text", "image"]:
                return "Invalid generation type", 400

            if generation_type == "text":
                response = await chat(user_input)
            elif generation_type == "image":
                response = await generate_image(user_input)

    except Exception as e:
        # Log the error (you can customize this to log to a file or monitoring system)
        print(f"Error occurred: {e}")
        response = "An error occurred while processing your request. Please try again."

    return render_template(
        'index.html', 
        user_input=user_input, 
        response=response, 
        generation_type=generation_type
    )

if __name__ == '__main__':
    app.run(debug=True)

