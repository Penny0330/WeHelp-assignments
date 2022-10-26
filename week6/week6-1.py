from flask import Flask, render_template, request, redirect, session, url_for
from mysql.connector import pooling

app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

app.secret_key = "secret"

# create a Connection pool
connection_pool = pooling.MySQLConnectionPool(
    pool_name="connection_pool",
    pool_size=5,
    pool_reset_session=True,
    host="localhost",
    user="root",
    password="123456",
    database="website"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    account = request.form["account"]
    password = request.form["password"]

    # Get connection object from a pool
    connection_object = connection_pool.get_connection()
    cur = connection_object.cursor()
    cur.execute(
        "SELECT * FROM `member` WHERE `username` = %s", [account])
    user = cur.fetchone()
    if user != None:
        return redirect(url_for("error", message="帳號已被註冊"))
    else:
        inser = "INSERT INTO `member`(`name`, `username`, `password`) VALUES (%s, %s, %s)"
        val = (name, account, password)
        cur.execute(inser, val)
        connection_object.commit()
        # close connection
        cur.close()
        connection_object.close()
        return redirect(url_for("home"))


@app.route("/signin", methods=["POST"])
def singin():
    account = request.form["account"]
    password = request.form["password"]

    connection_object = connection_pool.get_connection()
    cur = connection_object.cursor()
    cur.execute(
        "SELECT * FROM `member` WHERE `username` = %s AND `password` = %s", [account, password])
    user = cur.fetchone()
    cur.close()
    connection_object.close()
    if user == None:
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))
    else:
        session["id"] = user[0]
        session["name"] = user[1]
        session["account"] = user[2]
        return redirect(url_for("member", name=user[1]))


@app.route("/member")
def member():
    if "account" in session:
        name = request.args.get("name")
        connection_object = connection_pool.get_connection()
        cur = connection_object.cursor()
        cur.execute(
            "SELECT `name`, `content`, `message`.`time` FROM `member` JOIN `message` ON `member`.`id` = `message`.`member_id` ORDER BY `message`.`time` DESC")
        message = cur.fetchall()
        cur.close()
        connection_object.close()
        return render_template("member.html", name=name, message=message)
    else:
        return redirect(url_for("home"))


@app.route("/message",  methods=["POST"])
def message():
    name = session["name"]
    message = request.form["message"]
    id = session["id"]
    connection_object = connection_pool.get_connection()
    cur = connection_object.cursor()
    insert = "INSERT INTO `message`(`member_id`, `content`) VALUES (%s, %s)"
    val = (id, message)
    cur.execute(insert, val)
    connection_object.commit()
    cur.close()
    connection_object.close()
    return redirect(url_for("member", name=name))


@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html", message=message)


@app.route("/signout")
def signout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=3000, debug=True)
