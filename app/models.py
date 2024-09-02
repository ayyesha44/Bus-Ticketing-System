import app
import sqlalchemy
from flask_login import UserMixin


class User(UserMixin, app.db.Model):
    id: sqlalchemy.orm.Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True)
    username: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(sqlalchemy.String(64), index=True, unique=True)
    email: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(sqlalchemy.String(150), index=True, unique=True)
    password: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(sqlalchemy.String(300))

@app.login.user_loader
def load_user(id):
    return app.db.session.get(User, int(id))