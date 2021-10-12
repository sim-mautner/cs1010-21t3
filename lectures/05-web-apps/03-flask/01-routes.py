from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello World!"
    
@app.route('/another_route')
def some_other_function():
    return "This is the webpage associated "+ \
           "with <code>another_route</code>."
    
@app.route('/list_desserts')
def desserts():
    return "Cake, Popcorn, Brownies"

if __name__ == "__main__":
    app.run(debug=True)