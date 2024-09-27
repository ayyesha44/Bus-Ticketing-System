import app
import sqlalchemy
from flask_login import UserMixin
import sqlalchemy.orm as so
from sqlalchemy import ForeignKey


class User(UserMixin, app.db.Model):
    id: sqlalchemy.orm.Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True)
    username: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(sqlalchemy.String(64), index=True, unique=True)
    email: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(sqlalchemy.String(150), index=True, unique=True)
    password: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(sqlalchemy.String(300))

class Seat(app.db.Model):
    id: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(primary_key=True)
    selected: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(sqlalchemy.Boolean, unique=False, default=True)

class Tickets(app.db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_id: so.Mapped[int] = so.mapped_column(ForeignKey("user.id"))
    seat_id: so.Mapped[str] = so.mapped_column(ForeignKey("seat.id"))
    seat_type: so.Mapped[str] = so.mapped_column(sqlalchemy.String(64), index=True, unique=False)




@app.login.user_loader
def load_user(id):
    return app.db.session.get(User, int(id))