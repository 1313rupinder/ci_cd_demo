from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD demo is running"

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
