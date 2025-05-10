from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    step = "start"
    if request.method == "POST":
        step = request.form.get("step")
        choice = request.form.get("choice").lower()

        if step == "start":
            if choice == "left":
                step = "swimWait"
                message = "Do you want to swim or wait?"
            else:
                message = "Game Over! Your choice kicked you out of the game."
                step = "end"

        elif step == "swimWait":
            if choice == "swim":
                message = "Attacked by trout. Game Over."
                step = "end"
            else:
                message = "Which door do you want to select: red, blue, or yellow?"
                step = "door"

        elif step == "door":
            if choice == "red":
                message = "Burned by fire. Game Over."
            elif choice == "blue":
                message = "Eaten by beasts. Game Over."
            elif choice == "yellow":
                message = "🎉 Congratulations! You Win!"
            else:
                message = "Invalid door. Game Over."
            step = "end"

    return render_template("index.html", message=message, step=step)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
