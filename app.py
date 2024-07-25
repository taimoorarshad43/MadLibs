from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def form():

    prompts = stories.story.prompts

    return render_template('form.html', templates = prompts)

@app.route('/story')
def story():

    words = {}

    for (key,value) in request.args.items():
        words[key] = value

    print(words)

    ans = stories.story.generate(words)

    return render_template('story.html', story = ans)