from flask import redirect
from .. import app, db
from api.models.user import User


@app.route('/<string:username>')
def index(username):
    user = User.query.filter_by(username=username).first()
    token = user.generate_auth_token(expiration=3600)

    user.token = token
    db.session.add(user)
    print(token)
    return redirect('/static/index.html')
