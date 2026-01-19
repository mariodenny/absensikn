from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from admin.controller import admin_dashboard


admin_bp = Blueprint('admin',__name__,template_folder='templates',url_prefix='/admin')

@admin_bp.route("/dashboard",methods=["GET","POST"])
def dashboard():
    return render_template("admin/dashboard.html")