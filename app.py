
from startup import *
app = create_app("production")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
