from flask import Flask, request
from pyhtml import html, head, body, title, h1, p, form, input_, select, option, label

app = Flask(__name__)

RANGE_HIGH_START = 100
RANGE_LOW_START = 0

@app.route('/', methods=["GET","POST"]) # now accepting POST for the 'new game' form submission
def homepage():
    response = html(
        head(
            title('Guess My Number')
        ),
        body(
            h1('Guess My Number'),
            p('I will guess your number and each time you tell me: H for higher, L for lower or C for correct'),
            form(action="game_page")(
                label("Low end: ", input_(type="number", name="low_start")),
                label("High end: ", input_(type="number", name="high_start")),
                input_(type="submit", name="start_playing_button", value="Start Playing")
            )
        )
    )
    return str(response)

'''
User sends a request (from their browser) to our server.
The request will always contain a route (which web page to go to next).
The request can be a GET or POST (or a couple other things, not being covered today).

If the request is a POST request, it also has information from a form which was submitted.

Each route has an associated function, and specifies which types of requests it will accept.
'''

@app.route('/game_page', methods=["POST"])
def game_page():
    
    # If just started playing, set up variables
    if "start_playing_button" in request.form:
        range_high = int(request.form.get('high_start'))
        range_low = int(request.form.get('low_start'))
        guess = int((range_high+range_low)/2)
    else: # if they submitted feedback

        # get feedback out of form
        feedback = request.form.get('feedback')
        print(f"{feedback=}")

        # Get hidden information from the form
        guess = int(request.form.get('guess'))
        range_high = int(request.form.get('range_high'))
        range_low = int(request.form.get('range_low'))

        # If need to go lower, make high = guess - 1
        if feedback == 'L':
            range_high = guess - 1
        elif feedback == 'H':
            # lowest possible number is guess + 1
            range_low = guess + 1
        guess = int((range_high+range_low)/2)

    feedback_options = ['H','L','C']
    feedback_options_pyhtml = []
    for opt in feedback_options:
        # option(opt): 'H' --> '<option>H</option>' so it's ready to go into the html
        feedback_options_pyhtml.append(option(opt))

    # Display to continue playing vs finished game
    display = []
    if "start_playing_button" in request.form or feedback != 'C':
        display = [p('My guess is: '+str(guess)),
            form(action="game_page")(
                input_(type="hidden", name="guess", value=guess),
                input_(type="hidden", name="range_high", value=range_high),
                input_(type="hidden", name="range_low", value=range_low),
                select(name="feedback")(feedback_options_pyhtml),
                input_(type="submit", name="confirm_button", value="Confirm"),
            )
            ]
    else: # if the game is finished
        display = [p('I guessed your number! Good game. :)')]

    print(display)

    response = html(
        head(
            title('Guess My Number')
        ),
        body(
            h1('Guess My Number'),
            display,
            form(action='/')(
                input_(type="submit", name="new_game", value="New Game")
            )
        )
    )

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)

    # TODO MVP what to do when they enter C --> done
    # TODO NTH button to restart the game --> done
    # TODO NTH dropdown menu for the user to enter feedback --> done
    # TODO NTH/SG user can select the starting range (input where they can only enter numbers) --> done
    # TODO NTH/SG score is how many steps it took to guess the number
    # TODO SG high scores table