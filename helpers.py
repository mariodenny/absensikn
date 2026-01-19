from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(role=None):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if 'user_id' not in session:
                flash("Please login first", "warning")
                return redirect(url_for('auth.login'))
            if role and session.get('role') != role:
                flash("Access denied", "danger")
                return redirect(url_for('home'))
            return f(*args, **kwargs)
        return decorated
    return wrapper