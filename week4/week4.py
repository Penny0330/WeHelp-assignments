from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

app.secret_key = "secret"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def singin():
    # 取得 form input 的值
    account = request.form["account"]
    password = request.form["password"]
    # 帳號&密碼接正確
    if account == "test" and password == "test":
        session["account"] = account
        return redirect(url_for("member"))
    # 其中之一為空
    elif account == "" or password == "":
        return redirect(url_for("error", message="請輸入帳號、密碼"))
    # 帳號&密碼都有輸入，其一有誤
    elif account != "test" or password != "test":
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))


@app.route("/member")
def member():
    # 如帳號已存在，就可直接連到會員頁面，否則直接跳回首頁
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect(url_for("home"))


@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html", message=message)


@app.route("/signout")
def signout():
    # 刪除 session 裡的帳號紀錄，並跳回首頁
    session.pop("account", None)
    return redirect(url_for("home"))


# Optional

@app.route("/square/<num>")
def square(num):
    num = int(num)
    squareNum = num * num
    return render_template("square.html", num=num, squareNum=squareNum)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
