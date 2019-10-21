"""
imports
"""

from app import create_app
from app.settings import *


def run():
    app = create_app(DEVELOPMENT)
    app.run(debug=APP_DEBUG)


if __name__ == '__main__':
    run()
