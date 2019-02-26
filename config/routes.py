import os
from app import app
from controllers import users, ingredients, recipes

app.register_blueprint(users.api, url_prefix='/api')
app.register_blueprint(ingredients.api, url_prefix='/api')
app.register_blueprint(recipes.api, url_prefix='/api')

@app.route('/', defaults={'path': ''}) # homepage
@app.route('/<path:path>') # any other path
def catch_all(path):

    if os.path.isfile('dist/' + path): # if path is a file, send it back
        return app.send_static_file(path)

    return app.send_static_file('index.html') # otherwise send back the index.html file
