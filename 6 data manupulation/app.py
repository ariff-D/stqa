from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)
@app.route('/')
def main():
   df = pd.read_excel('students.xlsx')
   data = df.to_dict('records')
   return render_template('index.html', data=data)
if __name__=="__main__":
   app.run(debug=True, port=8008)