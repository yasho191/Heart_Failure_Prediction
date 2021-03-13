from flask import Flask, render_template, request
import pickle
import numpy as np

dclf_heart = pickle.load(open('dclf.pkl', 'rb'))
xrclf_heart = pickle.load(open('xrclf.pkl', 'rb'))
xclf_heart = pickle.load(open('xclf.pkl', 'rb'))


app = Flask(__name__)

@app.route('/')
def man(): 
	return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
	feature1 = int(request.form['a'])
	feature2 = int(request.form['b'])
	feature3 = int(request.form['c'])
	feature4 = int(request.form['d'])
	feature5 = int(request.form['e'])
	feature6 = int(request.form['f'])
	feature7 = int(request.form['g'])
	feature8 = int(request.form['h'])
	feature9 = int(request.form['i'])
	feature10 = int(request.form['j'])
	feature11 = int(request.form['k'])
	feature12 = int(request.form['l'])
	
	arr = np.array([[feature1, feature2, feature3, feature5, feature6, feature7, feature8, feature9, feature11, feature12]])
	
	pred1 = dclf_heart.predict(arr)
	pred2 = xrclf_heart.predict(arr)
	pred3 = xclf_heart.predict(arr)

	final_pred = [pred1, pred2, pred3]
	
	if final_pred.count(1) > final_pred.count(0):
		pred = 1
	else:
		pred = 0

	return render_template('after.html', data=pred)


if __name__=="__main__":
	app.run(debug=True)

