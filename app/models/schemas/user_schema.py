from app.config.db_config import *
from app.models.tables.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude=['re_password']