import functools

from flask import ( Blueprint ,flash , g ,  redirect , render_template  ,  request , session ,url_for)
from werkzeug.security import check_password_hash , generate_password_hash

from fin.db import get_db
bp  = Blueprint("auth" ,__name__, url_prefix= "/auth")

@bp.route("/parent_register"  , methods=('GET', 'POST'))
def  parent_register():
    if request.method == "POST":
        parent_username = request.form['parent_username']
        parent_email = request.form['parent_email']
        parent_password = request.form['parent_password']
        db = get_db()
        error = None

        if not parent_username:
            error = 'Username is required'
        elif not parent_email:
            error = 'Email is required'
        elif not parent_password :
            error = 'Password is required'

        elif db.execute(
                'SELECT parent_id FROM parent WHERE parent_username = ?',(parent_username,)).fetchone() is not None:
                error = 'USER {} is already registered'.format(parent_username)

        if error is None:
            db.execute('INSERT INTO parent (parent_username , parent_email ,parent_password) VALUES (? ,? , ?)' , (parent_username , parent_email , generate_password_hash(parent_password)))
            db.commit()
            return redirect(url_for('auth.parent_login'))

        flash(error)

    return render_template('auth/parent_register.html')



@bp.route('/parent_login' , methods =('GET' , 'POST'))
def parent_login():
    if request.method == 'POST':
        parent_username = request.form['parent_username']
        child_username = request.form['child_username']
        parent_password = request.form['parent_password']
        db = get_db()

        error = None
        parent = db.execute('SELECT * FROM parent WHERE parent_username =?', (parent_username,)).fetchone()
        child = db.execute('SELECT * FROM child WHERE child_username =?', (child_username,)).fetchone()


        if child is None :
            error = 'Your Child is not registered.'

        if parent is None :
            error = 'Incorrect username.'
        elif not check_password_hash(parent['parent_password'] , parent_password):
            error = "incorret password"

        if error is None:
            session.clear()
            session['parent_id'] = parent['parent_id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/parent_login.html')

@bp.before_app_request
def load_logged_in_parent():
    parent_id = session.get('parent_id')

    if parent_id is None:
        g.parent = None
    else:
        g.parent = get_db().execute(
            'SELECT * FROM parent WHERE parent_id = ?', (parent_id,)
        ).fetchone()



@bp.route('/parent_logout')
def parent_logout():
    session.clear()
    return redirect(url_for('index'))

def parent_login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.parent is None:
            return redirect(url_for('auth.parent_login'))

        return view(**kwargs)

    return wrapped_view



@bp.route("/child_register"  , methods=('GET', 'POST'))
def  child_register():
    if request.method == "POST":
        child_username = request.form['child_username']
        parent_email = request.form['parent_email']
        child_password = request.form['child_password']
        db = get_db()
        error = None

        parent = db.execute('SELECT * FROM parent WHERE parent_email =?', (parent_email,)).fetchone()

        if not child_username:
            error = 'Username is required'
        elif not parent_email:
            error = 'Email is required'
        elif not child_password :
            error = 'Password is required'

        elif db.execute(
                'SELECT child_id FROM child WHERE child_username = ?',(child_username,)).fetchone() is not None:
                error = 'USER {} is already registered'.format(child_username)

        elif parent is None:
            error = 'Parent  is not  registered Yet.'


        if error is None:
            db.execute('INSERT INTO child (child_username , parent_email ,child_password) VALUES (? ,? , ?)' , (child_username , parent_email , generate_password_hash(child_password)))
            db.commit()
            return redirect(url_for('auth.child_login'))

        flash(error)

    return render_template('auth/child_register.html')



@bp.route('/child_login' , methods =('GET' , 'POST'))
def child_login():
    if request.method == 'POST':
        child_username = request.form['child_username']
        child_password = request.form['child_password']
        db = get_db()

        error = None
        child = db.execute('SELECT * FROM child WHERE child_username =?', (child_username,)).fetchone()



        if child is None :
            error = 'Incorrect username.'
        elif not check_password_hash(child['child_password'] , child_password):
            error = "incorret password"

        if error is None:
            session.clear()
            session['child_id'] = child['child_id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/child_login.html')

@bp.before_app_request
def load_logged_in_child():
    child_id = session.get('child_id')

    if child_id is None:
        g.child = None
    else:
        g.child = get_db().execute(
            'SELECT * FROM child WHERE child_id = ?', (child_id,)
        ).fetchone()



@bp.route('/child_logout')
def child_logout():
    session.clear()
    return redirect(url_for('index'))

def child_login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.child is None:
            return redirect(url_for('auth.child_login'))

        return view(**kwargs)

    return wrapped_view
