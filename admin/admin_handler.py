from functools import wraps
from flask import session, redirect, url_for
from models import Knot



def admin_handler(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if session:
			if session['username']:
				try:
					user = Knot.query.filter(Knot.username==session['username'])
					if user.admin:
						return f(*args, **kwargs)
				except:
					return redirect(url_for('posts.index'))
		return redirect(url_for('login.log_in'))
	return decorated_function