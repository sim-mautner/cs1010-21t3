from flask import Flask, request, session
from pyhtml import html, form, input_, p, li, ul, br

app = Flask(__name__)

app.config['SECRET_KEY'] = '63dd2825882d764bb2862fbee4bb698a6c058d3549ba23595bf15d3e9e7d746f'

@app.route('/', methods=["GET", "POST"])
def homepage():

    # If a form was submitted
    if request.method == "POST":
        # If they clicked "Clear List"
        if "clear" in request.form:
            session.clear()
        # Otherwise they must want to add to the list
        else:
            # Get data from form
            item = request.form['item']
            # Save into session, at the end of the list
            if 'item_list' not in session:
                session['item_list'] = []
            session['item_list'].append(item)
            session.modified = True

    # Get list from session
    # Create html for the items in it
    my_list = session.get('item_list', [])
    my_list_pyhtml = []
    for item in my_list:
        my_list_pyhtml.append(li(item))

    response = html(
        ul(my_list_pyhtml), # put the items into an unordered list
        form(action="/")(
            input_(type="text", name="item"),
            input_(type="submit", name="add", value="Add Item"),
            br(),
            input_(type="submit", name="clear", value="Clear List")
            )
        )
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)