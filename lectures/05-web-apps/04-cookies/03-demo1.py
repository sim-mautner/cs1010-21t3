from flask import Flask, request, session
from pyhtml import html, form, input_, p

app = Flask(__name__)

app.config['SECRET_KEY'] = '63dd2825882d764bb2862fbee4bb698a6c058d3549ba23595bf15d3e9e7d746f'

@app.route('/', methods=["GET", "POST"])
def homepage():

    # If a form was submitted
    if request.method == "POST":
        # Get data from form
        item = request.form['item']
        # Save into session
        session['item'] = item

    # Check if 'item' is a key in the session
    if 'item' in session:
        # If it is, get the value
        item = session['item']
        display = f"Your last entry was: {item}."
    else:
        # Otherwise create default text
        display = f"No last entry."

    # If the key 'item' is in the session,
    # put the value into item variable.
    # Otherwise, let item variable equal "nothing".
    item = session.get('item', 'nothing')
    display2 = item

    response = html(
        p(display),
        p(display2),
        form(action="/")(
            input_(type="text", name="item"),
            input_(type="submit")
            )
        )
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)