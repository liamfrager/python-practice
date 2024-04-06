from datetime import date, timedelta
from calendar import isleap
from flask import Flask, flash, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, login_user, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash
from database import database, db, ListItem, User
from forms import LoginForm, RegisterForm, ThemeColorForm

# APP
app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySeCrEtDaTaBaSeKeY'
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = None
bootstrap = Bootstrap5(app)

# LOGIN MANAGER
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return database.get_user(id=user_id)


# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to-do-list.db'
db.init_app(app)
with app.app_context():
    db.create_all()


# VARIABLES & CLASSES
@app.context_processor
def add_variables():
    return {'today_date': date.today()}


class ToDoList():
    '''
    Parameters:
    title: The name of the list.
    range_start: The number of days from today where your range of data should start.
    range_end: The number of days from today where your range of data should end.
    new_item_due_date: The number of days from today that a newly added item should be due.
    '''

    def __init__(self, title, range_start, range_end):
        self.title = title
        self.query = db.select(ListItem).where(ListItem.due_date >= date.today() + timedelta(days=range_start), ListItem.due_date <
                                               date.today() + timedelta(days=range_end + 1), ListItem.user_id == current_user.id).order_by(ListItem.due_date)
        self.items = db.session.execute(self.query).scalars()
        self.new_item_due_date = date.today() + timedelta(days=range_end)
        self.route = '/'


# ROUTES
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        with app.app_context():
            user = database.get_user(email=form.data['email'])
            if user and check_password_hash(user.password, form.data['password']):
                login_user(user)
                app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = current_user.theme_color
                return redirect(url_for('lists'))
            else:
                flash('Incorrect login.')
                return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('register', form.data)
        try:
            with app.app_context():
                new_user = database.add_user(form.data)
                login_user(new_user)
                app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = current_user.theme_color
            return redirect(url_for('lists'))
        except IntegrityError:
            flash('User already exists with that email.')
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@app.route('/lists', methods=['GET', 'POST'])
def lists():
    list_name = None
    if request.method == 'POST':
        list_item = request.form.to_dict()
        list_name = list(list_item.keys())[0]
        with app.app_context():
            new_list_item = ListItem(
                text=list_item[list_name],
                due_date=date(*(int(n)
                              for n in list_item['new_item_due_date'].split('-'))),
                user_id=current_user.id
            )
            db.session.add(new_list_item)
            db.session.commit()
    with app.app_context():
        today = ToDoList('Today', -365, 0)
        this_week = ToDoList('This Week', 1, 7)
        this_month = ToDoList('This Month', 8, 7*4)
        future = ToDoList('Future', 29, 7*13)
        lists = [today, this_week, this_month, future]
        for lst in lists:
            lst.route = 'lists'
        return render_template('lists.html', lists=lists, editing=request.args.get('edit') if request.args.get('edit') else list_name)


@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
    list_name = None
    if request.method == 'POST':
        list_item = request.form.to_dict()
        list_name = list(list_item.keys())[0]
        with app.app_context():
            new_list_item = ListItem(
                text=list_item[list_name],
                due_date=date(*(int(n)
                              for n in list_item['new_item_due_date'].split('-'))),
                user_id=current_user.id
            )
            db.session.add(new_list_item)
            db.session.commit()
    view = request.args.get('view') if request.args.get('view') else 'week'
    lists = []
    today = date.today()
    days_in_month = [31, 29 if isleap(
        today.year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    match view:
        case 'week':
            for i in range(7):
                todo_list = ToDoList('Today' if i == 0 else (
                    date.today() + timedelta(days=i)).strftime('%A'), i, i)
                todo_list.route = 'calendar'
                lists.append(todo_list)
            id = "#"
        case 'month':
            for i in range(days_in_month[date.today().month - 1]):
                todo_list = ToDoList('Today' if i == today.day - 1 else (today - timedelta(
                    days=today.day) + timedelta(days=i + 1)).strftime('%B %-d'), i, i)
                todo_list.route = 'calendar'
                lists.append(todo_list)
            id = f"#{today.strftime('%B %-d')}"
        case 'year':
            for i in range(12):
                this_month_start = today - timedelta(days=today.day - 1)
                month_start = this_month_start - \
                    timedelta(days=sum([days_in_month[x] for x in range(today.month - 1)])) + \
                    timedelta(days=sum([days_in_month[x] for x in range(i)]))
                todo_list = ToDoList(month_start.strftime(
                    '%B'), -(today - month_start).days, -(today - month_start).days + days_in_month[month_start.month - 1] - 1)
                todo_list.route = 'calendar'
                lists.append(todo_list)
            id = f"#{today.strftime('%B')}"
    return render_template(f'calendar.html', id=id, view=view, lists=lists, editing=request.args.get('edit') if request.args.get('edit') else list_name)


@app.route('/edit/<route>', methods=['GET', 'POST'])
def edit(route):
    if request.method == 'POST':
        data = request.form.to_dict()
        ids = [id.split('_')[1] for id in list(data.keys())[::2]]
        texts = [text for text in list(data.values())[::2]]
        due_dates = [date(*(int(n) for n in due_date.split('-')))
                     for due_date in list(data.values())[1::2]]
        data = [{'id': ids[i], 'text': texts[i], 'due_date': due_dates[i]}
                for i in range(len(ids))]
        with app.app_context():
            for entry in data:
                db.session.query(ListItem).\
                    filter(ListItem.id == entry['id']). \
                    update(entry)
            db.session.commit()
        return redirect(url_for(route, view=request.args.get('view') if request.args.get('view') else 'week'))


@app.route('/delete/<list_item_id>')
def delete(list_item_id):
    with app.app_context():
        list_item = db.session.execute(
            db.select(ListItem).where(ListItem.id == list_item_id)).scalar()
        db.session.delete(list_item)
        db.session.commit()
    return redirect(url_for(request.args.get('route')))


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        theme = None if request.form['theme_color'] == 'default' else request.form['theme_color']
        with app.app_context():
            current_user.theme_color = theme
            db.session.commit()
        app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = theme
    return render_template('settings.html', default_theme=current_user.theme_color)


@app.route('/logout')
def logout():
    logout_user()
    app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = None
    return redirect(url_for('login'))


# RUN SERVER
if __name__ == '__main__':
    app.run(port=4000, debug=True)


# TODO: fix list sizing
# TODO: calendar view