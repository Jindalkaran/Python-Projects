from flask import Flask,render_template,request
from vsearch import search4letters
app=Flask(__name__)

@app.route('/')
def hello()->str:
	return 'Hello world from flasdk!!'

@app.route('/entry')
def entry()->'html':
	return render_template('entry.html',the_title='WELCOME')

@app.route('/search4',methods=['POST'])
def result()->'html':
	phrase=request.form['phrase']
	letters=request.form['letters']
	title="RESULTS IS!!"
	results=search4letters(phrase,letters)
	return render_template('results.html',the_title=title,the_phrase=phrase,the_letters=letters,the_results=results)
	
app.run(debug=True)
	
