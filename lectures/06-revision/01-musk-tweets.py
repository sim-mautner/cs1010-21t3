from flask import Flask, request, session
from pyhtml import html, p, form, input_, br, table, tr, td
import pandas
import random
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '63dd2825882d764bb2862fbee4bb698a6c078d3549ca23595bf15d3e9e7d746f'

def read_csv_as_list(filename):
    
    # open file
    f = open(filename, 'r')
    csv_reader = csv.reader(f)

    data = []

    # read in lines from file to data list
    for line in csv_reader:
        if line[10] != "tweet":
            data.append(line[10])

    # close the file
    f.close()

    print(data)
    # return the list
    return data

def get_tweets():
    return read_csv_as_list('../../data/elonmusk-full.csv')

#def get_tweets():
#    raw_tweets = pandas.read_csv('https://raw.githubusercontent.com/sim-mautner/cs1010-21t3/main/data/elonmusk-full.csv')
#    return list(map(str, list(raw_tweets.tweet)))

def random_word(words_weight):
    if words_weight == {}:
        return None
    words = random.choices(list(words_weight.keys()), list(words_weight.values()))
    return words[0]

def generate_word_map(tweets):
    word_map = {}
    word_map[tuple()] = {}

    for tweet in tweets:
        prefix = tuple() # (   ,    )
        for word in tweet.split():
            # Have we seen the prefix before?
            if prefix not in word_map:
                word_map[prefix] = {}
            # Prefix is in the map
            # Is our word, in that prefix dictionary?
            if word in word_map[prefix]:
                word_map[prefix][word] += 1
            else:
                word_map[prefix][word] = 1

            # Update the prefix
            # If the prefix was empty --> one word
            if len(prefix) == 0:
                prefix = (word,)
            elif len(prefix) == 1:
                prefix = (prefix[0],word)
            else: # already had 2 words
                prefix = (prefix[1],word)

    return word_map

def generate_tweet(word_map):

    word = random_word(word_map[tuple()])
    prefix = tuple()
    
    tweet = ""
    while word != None and len(tweet + word) < 280:
        tweet += word + " "

        # Update our prefix
        # If the prefix was empty --> one word
        if len(prefix) == 0:
            prefix = (word,)
        elif len(prefix) == 1:
            prefix = (prefix[0],word)
        else: # already had 2 words
            prefix = (prefix[1],word)

        # Update our word
        if prefix in word_map:
            word = random_word(word_map[prefix])
        else:
            word = None
    if word != None:
        tweet = tweet.strip() + '...'
    return tweet.strip()

@app.route('/',methods=["GET","POST"])
def homepage():

    session["correct"] = session.get("correct", None)

    if request.method == "POST":
        assert(session["correct"] != None)
        print(session["correct"])
        if session["correct"] in request.form:
            # Correct
            to_save = [session["real"],session["fake"],"correct"]
        else:
            # Incorrect
            to_save = [session["real"],session["fake"],"incorrect"]
        
        # open file for writing (saving)
        f = open(f'files/responses.csv', 'a')
        csv_writer = csv.writer(f)
        csv_writer.writerow(to_save)
        # close the file
        f.close()

    tweets = get_tweets()
    word_map = generate_word_map(tweets)
    fake_tweet = generate_tweet(word_map)
    real_tweet = random.choice(tweets)

    print("Real: "+real_tweet)
    print("Fake: "+fake_tweet)

    buttons = form(table(tr(td(fake_tweet), td(real_tweet)),
                         tr(td(input_(type="submit",name="Left",value="Left")),td(input_(type="submit",name="Right",value="Right")))))
    session["correct"] = "Right"
    session["real"] = real_tweet
    session["fake"] = fake_tweet
    if random.randint(0,1) == 0:
        buttons = form(table(tr(td(real_tweet), td(fake_tweet)),
                         tr(td(input_(type="submit",name="Left",value="Left")),td(input_(type="submit",name="Right",value="Right")))))
        session["correct"] = "Left"

    return str(html(buttons))


if __name__=="__main__":
    app.run(debug=True)


# NTH / SG: Have a score for the individual user