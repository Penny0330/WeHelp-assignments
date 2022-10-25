from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector

app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

app.secret_key = "secret"

connection = mysql.connector.connect(
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
    # 1.連至資料庫搜尋帳號有沒有一樣的
    # 2.如果沒有，就將資料新增至資料庫
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM `member` WHERE `username` = %s", [account])
    user = cur.fetchone()
    if user != None:
        return redirect(url_for("error", message="帳號已被註冊"))
    else:
        inser = "INSERT INTO `member`(`name`, `username`, `password`) VALUES (%s, %s, %s)"
        val = (name, account, password)
        cur.execute(inser, val)
        connection.commit()
        cur.close()
        return redirect(url_for("home"))


@app.route("/signin", methods=["POST"])
def singin():
    account = request.form["account"]
    password = request.form["password"]
    # 1.比對帳號、密碼是否與資料庫的一致
    # 2.如果一致將 `member` 裡的資料存進 Session
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM `member` WHERE `username` = %s AND `password` = %s", [account, password])
    user = cur.fetchone()
    if user == None:
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))
    else:
        session["id"] = user[0]
        session["name"] = user[1]
        session["account"] = user[2]
        cur.close()
        return redirect(url_for("member", name=user[1]))


@app.route("/member")
def member():
    if "account" in session:
        name = request.args.get("name")
        # 1.取得 `message` 的全部資料後，.fetchall()會返回一個 List
        # 2.將取得的 List 傳遞至樣板引擎中 forloop
        cur = connection.cursor()
        cur.execute(
            "SELECT `name`, `content`, `message`.`time` FROM `member` JOIN `message` ON `member`.`id` = `message`.`member_id` ORDER BY `message`.`time` DESC")
        message = cur.fetchall()
        cur.close()
        return render_template("member.html", name=name, message=message)

    else:
        return redirect(url_for("home"))


@app.route("/message",  methods=["POST"])
def message():
    name = session["name"]
    message = request.form["message"]
    id = session["id"]
    # 1.新增新的留言資料至資料庫
    cur = connection.cursor()
    insert = "INSERT INTO `message`(`member_id`, `content`) VALUES (%s, %s)"
    val = (id, message)
    cur.execute(insert, val)
    connection.commit()
    cur.close()
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
