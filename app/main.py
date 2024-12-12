from flask import Flask
from app.routes import register_routes

import torch
print(torch.__version__)

app = Flask(__name__)

# Register routes
register_routes(app)

@app.route('/')
def home():
    return {"message": "Welcome to the Hugging Faces API"}

if __name__ == "__main__":
    app.run(debug=True)
