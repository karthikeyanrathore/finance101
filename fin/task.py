from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from fin.auth import parent_login_required
from fin.db import get_db

bp = Blueprint('task', __name__ , url_prefix ='/task')

def get_goal(id, check_author=True):
    goal = get_db().execute(
        'SELECT task_name , task_amt , task_count , go.goal_id , bonus , goal_saving'
        ' FROM goal go JOIN child c ON go.author_id = c.child_id'
        ' WHERE go.goal_id = ?',
        (id,)
    ).fetchone()

    if goal is None:
        abort(404, "Post id {0} doesn't exist.".format(id))


    return goal 



@bp.route('/index' ,  methods = ('GET' , 'POST'))
@parent_login_required
def index():
    db = get_db()
    goals = db.execute(
        'SELECT go.goal_id , child_username , goal_amt , goal_name , saving_amt , bonus , time_left , author_id '
        ' FROM goal go JOIN child u ON go.author_id = u.child_id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('task/index.html', goals=goals)



@bp.route('/<int:id>/display' ,  methods = ('GET' , 'POST'))
@parent_login_required
def display(id):

    goal = get_goal(id)
    db = get_db()
    error = None

    goals = db.execute(
            'SELECT go.goal_id , task_name , task_amt , task_count , task_author , goal_name , author_id , c.child_id , bonus'
            ' FROM goal go JOIN child c ON go.author_id = c.child_id'
            ' WHERE go.goal_id = ?',
            (id , )
            ).fetchall()
    db.commit()

    if error is not None:
        flash(error)

    if goals is None:
        error = "NOT RIGHT"

    return render_template('task/display.html' , goals=goals)




@bp.route('/<int:id>/create' ,  methods = ('GET' , 'POST'))
@parent_login_required
def create(id):
    goal = get_goal(id)
    if request.method == "POST":
        task_name = request.form['task_name']
        task_amt = int(request.form['task_amt'])
        task_count = 0
        error = None


        
        if not task_name:
            error = "Task Name required"

        if error is not None:
            flash(error)

        else:
            db = get_db()
            db.execute(
                    'UPDATE goal SET task_name = ?, task_amt = ? , task_count =?'
                    ' WHERE goal_id=?' ,  
                    (task_name , task_amt , task_count , id)
                    )
            db.commit()
            return redirect(url_for('task.display'  , id = id))


    return render_template('task/create.html' ,goal=goal )






@bp.route('/<int:id>/count' ,  methods = ('GET' , 'POST'))
@parent_login_required
def count(id):
    goal = get_goal(id)
    db = get_db()
    #CC = db.execute('SELECT task_count  FROM goal WHERE goal_id = ?' , (id, )).fetchone()
    CC = goal['task_count']
    bonus = goal['bonus']
    task_amt = goal['task_amt']

    goal_saving = goal['goal_saving']


    #task_count = int(CC)
    #print(bonus + 1)
    bonus += task_amt
    task_count = CC
    #bonus = BB
    
    task_count += 1

    goal_saving += bonus

    db = get_db()
    db.execute(
            'UPDATE goal SET task_count =? , bonus = ? , goal_saving = ?'
            ' WHERE goal_id=?',  
            (task_count  , bonus, goal_saving, id)
            )
    db.commit()
    return redirect(url_for('task.display'  , id = id))












