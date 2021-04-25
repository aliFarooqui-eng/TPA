from flask import Flask, render_template,redirect,url_for,request,flash
from forms.addCountry import addCountry,Religion,Area,Tongue,BloodGroup
from forms.academicDomain import Category

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
def country():
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
      return redirect(url_for('country'))

   return render_template('country.html', form=form,result = myresult)

@app.route('/religion', methods=['GET', 'POST'])
def religion():
   form = Religion()

   mycursor.execute("SELECT * FROM religion")
   myresult = mycursor.fetchall()


   if form.validate_on_submit():


      religion_name = form.rname.data

      status = form.status.data

      sql = "INSERT INTO religion (rname,status) VALUES (%s, %s)"
      val = (religion_name,status)
      mycursor.execute(sql, val)

      mydb.commit()
      return redirect(url_for('religion'))

   else:
      return render_template('religion.html', form=form, result=myresult)


@app.route('/area', methods=['GET', 'POST'])
def area():
   form = Area()

   mycursor.execute("SELECT * FROM area")
   myresult = mycursor.fetchall()


   if form.validate_on_submit():


      area_name = form.aname.data

      status = form.status.data

      sql = "INSERT INTO area (aname,status) VALUES (%s, %s)"
      val = (area_name,status)
      mycursor.execute(sql, val)

      mydb.commit()
      return redirect(url_for('area'))

   else:
      return render_template('area.html', form=form, result=myresult)


@app.route('/tongue', methods=['GET', 'POST'])
def tongue():
   form = Tongue()

   mycursor.execute("SELECT * FROM tongue")
   myresult = mycursor.fetchall()


   if form.validate_on_submit():


      tongue_name = form.tname.data

      status = form.status.data

      sql = "INSERT INTO tongue (tname,status) VALUES (%s, %s)"
      val = (tongue_name,status)
      mycursor.execute(sql, val)

      mydb.commit()
      return redirect(url_for('tongue'))

   else:
      return render_template('tongue.html', form=form, result=myresult)


@app.route('/blood', methods=['GET', 'POST'])
def blood():
   form = BloodGroup()

   mycursor.execute("SELECT * FROM bloodgroup")
   myresult = mycursor.fetchall()


   if form.validate_on_submit():


      blood_name = form.bname.data

      status = form.status.data

      sql = "INSERT INTO bloodgroup (b_name,status) VALUES (%s, %s)"
      val = (blood_name,status)
      mycursor.execute(sql, val)

      mydb.commit()
      return redirect(url_for('blood'))

   else:
      return render_template('bloodGroup.html', form=form, result=myresult)

@app.route('/class', methods=['GET', 'POST'])
def classAcad():
    mycursor.execute("SELECT * FROM category WHERE status = 1")
    cat_result = mycursor.fetchall()

    mycursor.execute("SELECT class.className,class.status,category.cat_name FROM class INNER JOIN category ON category.cat_id = class.cat_id")
    myresult = mycursor.fetchall()




    if request.method == 'POST':

        class_name = request.form["class_name"]
        cat_select = request.form["category_select"]
        status = request.form["status"]

        if cat_select == "N":
            flash('Please select Category', 'error')
            return redirect(url_for('category'))

        elif class_name == "":
            flash('Please Enter Class Name', 'error')
            return redirect(url_for('category'))
        else:
            sql = "INSERT INTO class (className,status,cat_id) VALUES (%s, %s, %s)"
            val = (class_name, status,cat_select)
            mycursor.execute(sql, val)

            mydb.commit()

            return redirect(url_for('classAcad'))

    else:
        return render_template('class.html', result=myresult, result_category = cat_result)

@app.route('/category', methods=['GET', 'POST'])
def category():
   form = Category()

   mycursor.execute("SELECT * FROM category")
   myresult = mycursor.fetchall()


   if form.validate_on_submit():


      cat_name = form.catName.data

      status = form.status.data

      sql = "INSERT INTO category (cat_name,status) VALUES (%s, %s)"
      val = (cat_name,status)
      mycursor.execute(sql, val)

      mydb.commit()
      return redirect(url_for('category'))

   else:
      return render_template('category.html', form=form, result=myresult)



if __name__ == '__main__':
   app.run(debug = True)