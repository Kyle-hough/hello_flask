from flask import Flask, render_template # Import Flask to allow us to create our app

app = Flask(__name__)
    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html', phrase = "hello", times =5) 

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    print(name)
    return f"Hi + {name.capitalize()}"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    output = ''

    for i in range(0, num):
        output += f"<p>{word}<p>"
    return output

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

