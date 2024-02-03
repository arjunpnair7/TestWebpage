from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
  # Optional: You can pass data to the template here for dynamic content
  data = {"message": "Hello from Python!"}
  return render_template("index.html", data=data)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=False)
