from flask import Flask, render_template
from tester import test

app = Flask(__name__)

@app.route("/")
def hello():
  # Optional: You can pass data to the template here for dynamic content
  return test()

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=False)
