#!/usr/bin/env python3
"""basic Flask app
"""

from flask import Flask, render_template


app = Flask("my_beautiful_app")


@app.route("/", strict_slashes=False)
def root() -> str:
    """root endpoint
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
