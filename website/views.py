from flask import Blueprint, render_template, request,redirect, flash, jsonify,url_for
from flask_login import login_required, current_user
# from .models import Note
from .models import User,UserCart
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        pass

    return render_template("home.html", user=current_user)

@views.route('/cart',methods=['GET','POST'])
@login_required
def cart():
    user_id = current_user.id 
    user_cart = UserCart.query.filter_by(user_id=user_id).first()    
    product_list = user_cart.cart_items
    return render_template("cart.html",user=current_user,cart_items=product_list)

@views.route('/add_to_cart/<int:product_id>',methods=['POST','GET'])
@login_required
def add_to_cart(product_id):
    # print(product_id)
 
    user_id = current_user.id 
    user_cart = UserCart.query.filter_by(user_id=user_id).first()
    if not user_cart :
        itemtoinsert = str(product_id)+ ","
        user_cart = UserCart(user_id=user_id, cart_items=itemtoinsert)
        # user_cart.cart_items += str(product_id)+","
        db.session.add(user_cart)
        db.session.commit()
    else:
        user_cart.cart_items += str(product_id)+","
        db.session.add(user_cart)
        db.session.commit()
    flash('Product added to cart successfully!', 'success')
    return redirect(url_for('views.cart'))

