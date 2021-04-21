from flask import Flask, render_template,redirect,url_for
from forms.addCountry import addCountry
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="TPA"
)
mycursor = mydb.cursor()






app.config["SECRET_KEY"]="amir123"



@app.route('/', methods=['GET', 'POST'])
def generalDomain():
   form = addCountry()

   mycursor.execute("SELECT * FROM country")
   myresult = mycursor.fetchall()

   if form.validate_on_submit():

      status = form.status.data
      country_name = form.cname.data
      code = form.code.data
      s_c_name = form.s_c_name.data
      sql = "INSERT INTO country (cname,code,s_c_name,status) VALUES (%s, %s, %s, %s)"
      val = (country_name,code,s_c_name,status)
      mycursor.execute(sql, val)

      mydb.commit()
      return redirect(url_for('generalDomain'))



   return render_template('generalDomain.html', form=form,result = myresult)

if __name__ == '__main__':
   app.run(debug = True)