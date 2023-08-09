from flask import render_template, url_for, flash, redirect, request
from business_flow_tracker import app, db, bcrypt
from business_flow_tracker.forms import RegistrationForm, LoginForm, CashFlowForm, WorkflowForm, AllocationForm, PaymentForm
from business_flow_tracker.models import User, CashFlow, Workflow, Allocation, Payment
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/cashflow", methods=['GET', 'POST'])
@login_required
def cashflow():
    form = CashFlowForm()
    if form.validate_on_submit():
        cashflow = CashFlow(amount=form.amount.data, user=current_user)
        db.session.add(cashflow)
        db.session.commit()
        flash('Your cashflow has been added!', 'success')
        return redirect(url_for('home'))
    return render_template('cashflow.html', title='CashFlow', form=form)

@app.route("/workflow", methods=['GET', 'POST'])
@login_required
def workflow():
    form = WorkflowForm()
    if form.validate_on_submit():
        workflow = Workflow(description=form.description.data, user=current_user)
        db.session.add(workflow)
        db.session.commit()
        flash('Your workflow has been added!', 'success')
        return redirect(url_for('home'))
    return render_template('workflow.html', title='Workflow', form=form)

@app.route("/allocation", methods=['GET', 'POST'])
@login_required
def allocation():
    form = AllocationForm()
    if form.validate_on_submit():
        allocation = Allocation(amount=form.amount.data, user=current_user)
        db.session.add(allocation)
        db.session.commit()
        flash('Your allocation has been added!', 'success')
        return redirect(url_for('home'))
    return render_template('allocation.html', title='Allocation', form=form)

@app.route("/payment", methods=['GET', 'POST'])
@login_required
def payment():
    form = PaymentForm()
    if form.validate_on_submit():
        payment = Payment(amount=form.amount.data, user=current_user)
        db.session.add(payment)
        db.session.commit()
        flash('Your payment has been added!', 'success')
        return redirect(url_for('home'))
    return render_template('payment.html', title='Payment', form=form)
