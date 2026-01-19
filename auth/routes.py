from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from auth.controller import login_user

auth_bp = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = login_user(email, password)
        if user:
            session['user_id'] = user['id']
            session['name'] = user['name']
            session['role'] = user['role']
            flash(f"Welcome {user['name']}!", "success")
            # redirect ke dashboard sesuai role
            if user['role'] == 'ADMIN':
                return redirect(url_for('admin.dashboard'))
            elif user['role'] == 'TEACHER':
                return redirect(url_for('teacher.dashboard'))
            elif user['role'] == 'SA':
                return redirect(url_for('sa.dashboard'))
            else:
                return redirect(url_for('home'))
        else:
            flash("Invalid email or password", "danger")
    return render_template('auth/login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully", "info")
    return redirect(url_for('auth.login'))
