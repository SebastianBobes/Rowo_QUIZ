from flask import Flask, render_template, request, redirect, url_for, session
import authentification as auth
import questions as q
from datetime import datetime
import timer
import score_calculator
app = Flask(__name__)



app = Flask(__name__)
app.secret_key = 'rowo2025'
@app.route('/')
def first_function():
    score_calculator.calculate_final_score()
    username1=score_calculator.read_ranking()[0][0]
    score1=score_calculator.read_ranking()[0][1]
    username2=score_calculator.read_ranking()[1][0]
    score2=score_calculator.read_ranking()[1][1]
    username3=score_calculator.read_ranking()[2][0]
    score3=score_calculator.read_ranking()[2][1]
    username4=score_calculator.read_ranking()[3][0]
    score4=score_calculator.read_ranking()[3][1]
    username5=score_calculator.read_ranking()[4][0]
    score5=score_calculator.read_ranking()[4][1]
    username6=score_calculator.read_ranking()[5][0]
    score6=score_calculator.read_ranking()[5][1]
    username7=score_calculator.read_ranking()[6][0]
    score7=score_calculator.read_ranking()[6][1]
    username8=score_calculator.read_ranking()[7][0]
    score8=score_calculator.read_ranking()[7][1]
    username9=score_calculator.read_ranking()[8][0]
    score9=score_calculator.read_ranking()[8][1]
    username10=score_calculator.read_ranking()[9][0]
    score10=score_calculator.read_ranking()[9][1]
    username11=score_calculator.read_ranking()[10][0]
    score11=score_calculator.read_ranking()[10][1]
    username12=score_calculator.read_ranking()[11][0]
    score12=score_calculator.read_ranking()[11][1]
    username13 = score_calculator.read_ranking()[12][0]
    score13 = score_calculator.read_ranking()[12][1]
    username14 = score_calculator.read_ranking()[13][0]
    score14 = score_calculator.read_ranking()[13][1]
    username15 = score_calculator.read_ranking()[14][0]
    score15 = score_calculator.read_ranking()[14][1]
    username16 = score_calculator.read_ranking()[15][0]
    score16 = score_calculator.read_ranking()[15][1]
    username17 = score_calculator.read_ranking()[16][0]
    score17 = score_calculator.read_ranking()[16][1]

    return render_template('Home.html',username1=username1,score1=score1,username2=username2,score2=score2,username3=username3,score3=score3,
                           username4=username4,score4=score4,username5=username5,score5=score5,username6=username6,score6=score6,
                           username7=username7,score7=score7,username8=username8,score8=score8,username9=username9,score9=score9,
                           username10=username10,score10=score10,username11=username11,score11=score11,username12=username12,score12=score12,
                           username13=username13,score13=score13,username14=username14,score14=score14,username15=username15,score15=score15,
                           username16=username16,score16=score16,username17=username17,score17=score17)

@app.route("/logout")
def logout():
    score_calculator.calculate_final_score()
    session.pop('username', None)
    return redirect(url_for('first_function'))


@app.route('/logged_in')
def logged_in_function():
    username = session.get('username')
    score_calculator.calculate_final_score()
    username1 = score_calculator.read_ranking()[0][0]
    score1 = score_calculator.read_ranking()[0][1]
    username2 = score_calculator.read_ranking()[1][0]
    score2 = score_calculator.read_ranking()[1][1]
    username3 = score_calculator.read_ranking()[2][0]
    score3 = score_calculator.read_ranking()[2][1]
    username4 = score_calculator.read_ranking()[3][0]
    score4 = score_calculator.read_ranking()[3][1]
    username5 = score_calculator.read_ranking()[4][0]
    score5 = score_calculator.read_ranking()[4][1]
    username6 = score_calculator.read_ranking()[5][0]
    score6 = score_calculator.read_ranking()[5][1]
    username7 = score_calculator.read_ranking()[6][0]
    score7 = score_calculator.read_ranking()[6][1]
    username8 = score_calculator.read_ranking()[7][0]
    score8 = score_calculator.read_ranking()[7][1]
    username9 = score_calculator.read_ranking()[8][0]
    score9 = score_calculator.read_ranking()[8][1]
    username10 = score_calculator.read_ranking()[9][0]
    score10 = score_calculator.read_ranking()[9][1]
    username11 = score_calculator.read_ranking()[10][0]
    score11 = score_calculator.read_ranking()[10][1]
    username12 = score_calculator.read_ranking()[11][0]
    score12 = score_calculator.read_ranking()[11][1]
    username13 = score_calculator.read_ranking()[12][0]
    score13 = score_calculator.read_ranking()[12][1]
    username14 = score_calculator.read_ranking()[13][0]
    score14 = score_calculator.read_ranking()[13][1]
    username15 = score_calculator.read_ranking()[14][0]
    score15 = score_calculator.read_ranking()[14][1]
    username16 = score_calculator.read_ranking()[15][0]
    score16 = score_calculator.read_ranking()[15][1]
    username17 = score_calculator.read_ranking()[16][0]
    score17 = score_calculator.read_ranking()[16][1]
    if username == None:
        return render_template("Home.html",username1=username1,score1=score1,username2=username2,score2=score2,username3=username3,score3=score3,
                           username4=username4,score4=score4,username5=username5,score5=score5,username6=username6,score6=score6,
                           username7=username7,score7=score7,username8=username8,score8=score8,username9=username9,score9=score9,
                           username10=username10,score10=score10,username11=username11,score11=score11,username12=username12,score12=score12,
                           username13=username13,score13=score13,username14=username14,score14=score14,username15=username15,score15=score15,
                           username16=username16,score16=score16,username17=username17,score17=score17)
    else:
        return render_template('Logged_in.html',username1=username1,score1=score1,username2=username2,score2=score2,username3=username3,score3=score3,
                           username4=username4,score4=score4,username5=username5,score5=score5,username6=username6,score6=score6,
                           username7=username7,score7=score7,username8=username8,score8=score8,username9=username9,score9=score9,
                           username10=username10,score10=score10,username11=username11,score11=score11,username12=username12,score12=score12,
                           username13=username13,score13=score13,username14=username14,score14=score14,username15=username15,score15=score15,
                           username16=username16,score16=score16,username17=username17,score17=score17)

@app.route("/quiz")
def second_function():
    username = session.get('username')
    if auth.check_starting_time(username) == False:
        return render_template('Logged_in.html', username=username)
    else:
        starting_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        auth.update_starting_time(starting_time=starting_time,username=username)
        return render_template("Quiz.html", action="/quiz")

@app.route("/submit", methods=['POST', 'GET'])
def submit_form():
    username = session.get('username')
    if auth.check_time(username):
        ans_dict = {}
        for i in range(1, 61, 1):
            print(request.form.get(f'Q{i}'))
            ans_dict[f'{i}'] = request.form.get(f'Q{i}')
        print(ans_dict)
        score = q.read_qa(ans_dict)
        submission_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        starting_time=auth.read_start_time(username)
        time = timer.calculate_time_difference(starting_time,submission_time)
        auth.update_total_time(time,username)
        score_calculator.calculate_final_score()
        ranking = score_calculator.read_ranking()
        print(ranking)
        auth.update_score(ans_dict=ans_dict,score=score,submission_time=submission_time,username=username)
        return render_template('Logged_in.html', username=username, score=score, time=time, ranking=ranking)
    else:
        score = auth.read_score(username)
        time = timer.calculate_time_difference(auth.read_start_time(username), auth.read_end_time(username))
        auth.update_total_time(time, username)
        score_calculator.calculate_final_score()
        ranking = score_calculator.read_ranking()
        return render_template("Logged_in.html", username=username, score=score, time=time, ranking=ranking)




@app.route("/login", methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form["Name"]
        password = request.form["Password"]
        if auth.check_password(name, password):
            session['username']=name
            print(session['username'])
            return redirect(url_for('logged_in_function'))
    return render_template('Login.html')

if __name__ == '__main__':
    app.run(debug=True)

