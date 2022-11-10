from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from mysql.connector import pooling
from MySQL import MySQLPassword
from flask_bcrypt import Bcrypt


app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

# hash password
bcrypt = Bcrypt(app)

# session
app.secret_key = "secret"

connection_pool = pooling.MySQLConnectionPool(
    pool_name="connection_pool",
    pool_size=5,
    pool_reset_session=True,
    host="localhost",
    user="root",
    password=MySQLPassword(),
    database="website"
)


@app.route("/")
def home():
    if "account" in session:
        name = session["name"]
        return redirect(url_for("member", name=name))
    else:
        return render_template("index.html")


@app.route("/signup", methods=["POST"])
def signup():
    try:
        name = request.form["name"]
        account = request.form["account"]
        password = request.form["password"]
        connection_object = connection_pool.get_connection()
        cur = connection_object.cursor()
        cur.execute(
            "SELECT * FROM `member` WHERE `username` = %s", [account])
        user = cur.fetchone()
        if user != None:
            return redirect(url_for("error", message="帳號已被註冊"))
        else:
            hashed_password = bcrypt.generate_password_hash(password=password)
            insert = "INSERT INTO `member`(`name`, `username`, `password`) VALUES (%s, %s, %s)"
            value = (name, account, hashed_password)
            cur.execute(insert, value)
            connection_object.commit()
            return redirect(url_for("home"))
    except:
        print("There appears to be some error!")
    finally:
        cur.close()
        connection_object.close()


@app.route("/signin", methods=["POST"])
def singin():
    try:
        account = request.form["account"]
        password = request.form["password"]
        connection_object = connection_pool.get_connection()
        cur = connection_object.cursor()
        cur.execute(
            "SELECT * FROM `member` WHERE `username` = %s", [account])
        user_account = cur.fetchone()
        if user_account == None:
            return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))
        else:
            check_password = bcrypt.check_password_hash(
                user_account[3], password)
            if check_password:
                session["id"] = user_account[0]
                session["name"] = user_account[1]
                session["account"] = user_account[2]
                return redirect(url_for("member", name=user_account[1]))
            else:
                return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))
    except:
        print("There appears to be some error!")
    finally:
        cur.close()
        connection_object.close()


@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html", message=message)


@app.route("/member")
def member():
    try:
        connection_object = connection_pool.get_connection()
        cur = connection_object.cursor()
        if "account" in session:
            name = request.args.get("name")
            cur.execute(
                "SELECT `name`, `content`, `message`.`time` FROM `member` JOIN `message` ON `member`.`id` = `message`.`member_id` ORDER BY `message`.`time` DESC")
            message = cur.fetchall()
            return render_template("member.html", name=name, message=message)
        else:
            return redirect(url_for("home"))
    except:
        print("There appears to be some error!")
    finally:
        cur.close()
        connection_object.close()


@app.route("/message",  methods=["POST"])
def message():
    try:
        name = session["name"]
        message = request.form["message"]
        id = session["id"]
        connection_object = connection_pool.get_connection()
        cur = connection_object.cursor()
        insert = "INSERT INTO `message`(`member_id`, `content`) VALUES (%s, %s)"
        value = (id, message)
        cur.execute(insert, value)
        connection_object.commit()
        return redirect(url_for("member", name=name))
    except:
        print("There appears to be some error!")
    finally:
        cur.close()
        connection_object.close()


@app.route("/api/member",  methods=["GET", "PATCH"])
def api_member():
    try:
        connection_object = connection_pool.get_connection()
        cur = connection_object.cursor()
        if request.method == "GET":
            username = request.args.get("username")
            cur.execute(
                "SELECT `id`, `name`, `username` FROM `member` WHERE `username` = %s", [username])
            user = cur.fetchone()
            if user != None:
                return jsonify({
                    "data": {
                        "id": user[0],
                        "name": user[1],
                        "username": user[2]
                    }
                })
            return jsonify({"data": None})

        else:
            if "account" in session:
                username = session["account"]
                print(username)
                update_name = request.json["name"]
                cur.execute(
                    "UPDATE `member` SET `name` = %s WHERE `username` = %s", [
                        update_name, username]
                )
                connection_object.commit()
                session["name"] = update_name
                return jsonify({"ok": True})

            return jsonify({"error": True})
    except:
        print("There appears to be some error!")
    finally:
        cur.close()
        connection_object.close()


@app.route("/signout")
def signout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=3000, debug=True)
