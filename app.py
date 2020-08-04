import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)


rf = pickle.load(open('reg1.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    
    format = request.args.get('format')
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = rf.predict(final_features)
    output = round(prediction[0],2)
    '''
    if request.method == 'POST':
        a = request.form['store']
        b = request.form['dept']
        c = request.form['holiday']
        data = []
        data.append(a)
        data.append(b)
        data.append(c)

        prediction = rf.predict(data).toarray()
        output = round(prediction[0],2)

    '''
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)
    '''

    if(format == 'json'):
        return jsonify({'salary': output})

    return render_template('index.html', prediction_text='weekly sales should be $ {}'.format(output))
    
    
    
    
    if __name__ == "__main__":
      app.run(debug=True)  # auto-reload on code change
