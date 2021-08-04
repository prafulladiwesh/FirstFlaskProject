from flask import Flask

from routes import initialize_routes

app = Flask(__name__)


# URL -> invoke function
# 1. decorator
# 2. function call

# 1.
# @app.route('/api/hello')

initialize_routes(app)


# main trick
if __name__ == "__main__":
    app.run(debug=True)

