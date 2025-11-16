from eapp.models import User, Product, Category
import hashlib
from eapp import app
def load_categories():
    return Category.query.all()
def load_products(cate_id=None, kw=None, page=1):
    query = Product.query
    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))
    if page:
        start = (page - 1)*app.config['PAGE_SIZE']
        query = query.slice(start, start + app.config['PAGE_SIZE'])
    return query.all()

def count_products():
    return Product.query.count()
#lau user
def get_user_by_id(id):
    return User.query.get(id)

def auth_user(username, password):
    password= str((hashlib.md5(password.strip().encode('utf-8')).hexdigest()))
    return User.query.filter(User.username==username.strip(),
                             User.password==password).first()

