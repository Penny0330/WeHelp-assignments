from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(
    __name__,
    static_folder="templates",
    static_url_path="/"
)

app.secret_key = "any string but secret"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def singin():
    account = request.form["account"]
    password = request.form["password"]
    if account == "test" and password == "test":
        session["account"] = account
        return redirect("/member")
    elif account == "" or password == "":
        return redirect("/error?message=請輸入帳號、密碼")
    elif account != "test" or password != "test":
        return redirect("/error?message=帳號、或密碼輸入錯誤")


@app.route("/member")
def member():
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect("/")


@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html", message=message)


@app.route("/signout")
def signout():
    del session["account"]
    return redirect("/")


# Optional

@app.route("/square")
def square():
    # num = request.form["num"]
    # num = int(num)
    num = request.args.get("num", type=int, default=0)
    squareNum = num*num
    return render_template("square.html", squareNum=squareNum, num=num)

# @app.route("/square", methods=["POST", ])
# def square():
#     nums = request.form["num"]
#     return redirect(url_for("square1", num=nums))


# @app.route("/square/<num>")
# def square1(num):
#     num = int(num)
#     squareNum = num * num
#     return render_template("square.html", num=num, squareNum=squareNum)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
