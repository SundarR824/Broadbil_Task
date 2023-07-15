import os
current_dir = os.getcwd()

from app import app

if __name__ == '__main__':
    app.run(debug=True)
