from flask import Flask, render_template, request, session, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = 'secretkey123'  # Needed to use sessions

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'roll_count' not in session:
        session['roll_count'] = 0
    if 'history' not in session:
        session['history'] = []

    dice_results = []
    error = None

    if request.method == 'POST':
        try:
            num_dice = int(request.form['num_dice'])
            if num_dice <= 0:
                error = "Number of dice must be at least 1."
            elif num_dice > 10:
                error = "You can roll a maximum of 10 dice at a time."
            else:
                dice_results = [random.randint(1, 6) for _ in range(num_dice)]
                session['roll_count'] += 1
                session['history'].append(dice_results)
        except ValueError:
            error = "Invalid input. Please enter a number."

    return render_template(
        'index.html',
        results=dice_results,
        count=session['roll_count'],
        history=session['history'],
        error=error
    )

@app.route('/reset')
def reset():
    session.pop('roll_count', None)
    session.pop('history', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
