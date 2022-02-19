from flask import Flask, render_template
import requests as req

global all_posts


app = Flask(__name__)


@app.route('/')
def home():

    global all_posts

    a_response = req.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = a_response.json()

    return render_template("index.html", posts=all_posts)


@app.route('/blog/<int:post_id>')
def post(post_id):

    global all_posts

    a_title = ''
    a_subtitle = ''
    a_body = ''

    for a_post in all_posts:

        if a_post['id'] == post_id:

            a_title = a_post['title']
            a_subtitle = a_post['subtitle']
            a_body = a_post['body']
            break

    # Asserting.
    assert a_title != '', 'Blog post must have a title.'

    return render_template('post.html', a_title=a_title, a_subtitle=a_subtitle, a_body=a_body)


if __name__ == "__main__":
    app.run(debug=True)
