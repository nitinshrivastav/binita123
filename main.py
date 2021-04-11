from flask import Flask,render_template,request
from flask_mysql import MySQL
app=Flask(__name__)
@app.route("/")
def xyz():
    return render_template("sum.html")
@app.route("/su",methods=['GET','POST'])

def dfg():
    if(request.method=='POST'):
        num1=int(request.form['a'])
        num2=int(request.form['b'])
        total=num1+num2
        
        return  render_template('sum.html',s=total)
if __name__=='__main__':
    app.run()




