from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from eapp import db, app
from eapp.models import Product, Category

admin = Admin(app=app, name="e-Commerce's Admin")
admin.add_view(ModelView(Product, db.session, name="Sản phẩm"))
admin.add_view(ModelView(Category, db.session, name="Danh mục"))
