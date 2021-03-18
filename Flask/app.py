from flask import Flask, render_template, request
import pickle
import numpy as np

dclf_heart = pickle.load(open('dclf.pkl', 'rb'))
xrclf_heart = pickle.load(open('xrclf.pkl', 'rb'))
xclf_heart = pickle.load(open('xclf.pkl', 'rb'))


app = Flask(__name__)

@app.route('/')
def man(): 
	return render_template('PredictionForm.html')


@app.route('/predict', methods=['POST'])
def home():
	feature1 = int(request.form['Age'])
	feature2 = int(request.form['Gender'])
	feature3 = int(request.form['Anaemia'])
	feature4 = int(request.form['Ejection Fraction'])
	feature5 = int(request.form['Serum Sodium'])
	feature6 = int(request.form['Serum Creatinine'])
	feature7 = int(request.form['Creatinine Phosphokinase'])
	feature8 = int(request.form['Smoking'])
	feature9 = int(request.form['Follow-Up Time'])
	feature10 = int(request.form['Platelets'])
	feature11 = int(request.form['High Blood Pressure'])
	feature12 = int(request.form['Diabetes'])
	
	arr = np.array([[feature1, feature3, feature7, feature12, feature4, feature11, feature10, feature6, feature5, feature2]])
	print(arr)
	
	pred1 = dclf_heart.predict(arr)
	pred2 = xrclf_heart.predict(arr)
	pred3 = xclf_heart.predict(arr)

	final_pred = [pred1, pred2, pred3]
	
	if final_pred.count(1) > final_pred.count(0):
		pred = 1
	else:
		pred = 0

	print(pred)

	return render_template('message.html', data=pred)


if __name__=="__main__":
	app.run(debug=True)

