
from flask import Flask,render_template,request
app=Flask(__name__,template_folder="project")

@app.route('/')
def home():
	return render_template('demo.html')

def get_prediction(n1):
 	import pickle
 	import os
 	p = os.path.dirname(__file__)
 #filepath = os.path.join(p,'model.data')
 	with open('model.data','rb') as f:
  		model=pickle.load(f)
 	y_pred = model.predict([[n1]])
 	return y_pred[0]
 
 
@app.route('/calc',methods=['get','post'])
def calc():
    	MSRP = request.form['Engine HP']
  
    	p = get_prediction(int(MSRP))
         
    	return  "Answer " + str(p)

if __name__ == "__main__":
    	print("Starting Python Flask Server For car Prediction...")
    	app.run(debug=True)


 


 
   	