'''routes for pharmacy operations'''

from flask import (
    Blueprint, 
    render_template, 
    request,
    jsonify,
    redirect,
    url_for,
    flash)
from flask_mail import Message
from models import (
    db,
    Pharmacy,
    )
from .utils import (
    hash_pwd,
    check_pwd,
    gen_uuid,
    send_email,
    get_cur_time
    )
#create a blueprint
pharmacy_bp = Blueprint('pharmacy', __name__)

#registration endpoint
@pharmacy_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        #collects the pharmacy registration details and save to the db
        name = request.form['name']
        location = request.form['location']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        #hash the password
        hashed_pwd = hash_pwd(password)
        #create a new user
        new_pharm = Pharmacy(
            pharm_name = name,\
            pharm_location = location,\
            email = email,\
            contact = contact,\
            password = hashed_pwd,\
            pharm_uuid = gen_uuid(),\
            reg_date = get_cur_time()
        )

        try:
            db.session.add(new_pharm)
            db.session.commit()
            # #send an email to the user confirming registration
            # mail = create_mail_object()
            # msg = Message('VIRTUAL DOCTOR REGISTRATION', sender='naismart@franksolutions.tech', recipients=[email])
            # msg.body = 'Thank You for registering with us!\nYour health matters to us'
            # mail.send(msg)
            # '''
            # #send an email to the admin informing of a new user
            # users = session.query(Customers).filter_by(email=email).first()
            # msg = Message('New user', sender='naismart@franksolutions.tech', recipients=['francischege602@gmail.com'])
            # msg.body = f'{users.first_name} {users.last_name}\n\n\n'
            # mail.send(msg)
            # '''
            flash('Registration was successful')
            return redirect(url_for('public.sign_in', portal='pharmacy'))
        #errors arising due to unique constraint violation
        except:
            db.session.rollback()
            flash('Number or email already exists!')
            return render_template('/private/pharmacy_portal/pharmacy_sign_up.html')
    else:
        #render the registration page
        return render_template('/private/pharmacy_portal/pharmacy_sign_up.html')

# sign_in endpoint
@pharmacy_bp.route('/sign_in', methods=['POST'])
def sign_in():
    """Checks if the entered password matches the one stored in the database for the pharmacy"""
    email = request.form['email']
    password = request.form['password']
    hashed_pwd = db.session.query(Pharmacy.password).filter_by(email=email).first()
    
    if hashed_pwd is not None:
        correct_pwd = check_pwd(password, hashed_pwd[0])
        if correct_pwd:
            return jsonify('Signed in successfully as pharmacy!')
        else:
            flash('Wrong password! Please try again.')
            return redirect(url_for('public.sign_in', portal='pharmacy'))
    else:
        flash('Email does not exist! Please try again.')
        return redirect(url_for('public.sign_in', portal='pharmacy'))

