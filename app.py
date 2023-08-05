from flask import Flask, render_template, request
import ibm_db

app= Flask(__name__)

conn=ibm_db.connect("DATABASE=bludb; HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;UID=mwd16443;PWD=7S3kSGkS8b4fy7jw; SECURITY= ssl; SSLSERVERCERTIFICATE=DigiCertGlobalRootCA.crt;",'','')
print(ibm_db.active(conn))
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        uname=request.form['username']
        pword = request.form['password']
        print(uname, pword)
        sql = 'SELECT * FROM  REGISTER WHERE USERNAME=?'
        stmt=ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, uname)
        ibm_db.bind_param(stmt, 2, pword)
        ibm_db.execute(stmt)
        out=ibm_db.fetch_assoc(stmt)
        print(out)
        if out == 'flase':
            msg = "Invalid Credentails"
            return render_template("login.html", login_message = msg)
        else:
            role= out ['ROLE']
            if role == 0:
                return render_template("profile.html")
            elif role ==1:
                return render_template("")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
