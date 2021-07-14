from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/validate/<name>')
def check_user(name):
    if name == 'Mikayla':
        return redirect(url_for('admin_page', name=name))
    elif name == 'Godwin':
        return redirect(url_for('user_page', name=name))
    else:
        if name == 'Guest':
            return redirect(url_for('guest_pge', name=name))


@app.route('/user/<name>')
def user_page(name):
    return 'Hello user %s ' % name


@app.route('/admin/<name>')
def admin_page(name):
    return 'Welcome to the admin page %s ' % name


@app.route('/Guest/<name>')
def guest_page(name):
    return 'Welcome to the guest page %s' % name


@app.route('/currency/<float:salary>')
def salary_check(salary):
    if salary < 10500.50:
        return redirect('https://www.sahomeloans.com/%27')
    else:
        return redirect('https://www.fnb.co.za/%27')


if __name__ == '__main__':
    app.debug = True
    app.run()
