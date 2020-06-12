from flask import Flask , render_template
app = Flask(__name__)
# __name__ is name of module = __main__
# so flask knows where to find things
# https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app

posts= [
	{
		'author': 'Moni Rodriguez',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'June 9, 2020'
	},
	{
		'author': 'Moni Rodriguez',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'June 9, 2020'
	}
]

#both of these work with / and /home
@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html', posts= posts) # default title


#creates another route to other page
# /about
@app.route("/about")
def about():
	return render_template('about.html', title= "About") # specify title


# only true when ran directly from py
if __name__ == '__main__':
	app.run(debug=True)