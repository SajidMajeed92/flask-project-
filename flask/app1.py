from flask import Flask ,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/form",methods=['GET' ,'POST'])
def form():
    if request.method =='GET':
        return render_template('index.html')
    else:
        num1 = float(request.form['num1']) 
        num2 = float(request.form['num2']) 
        num3 = float(request.form['num3']) 
        average = (num1+num2+num3)/3
        
        return render_template('index.html',score =average)


if __name__ == "__main__":
    app.run(debug=True)
