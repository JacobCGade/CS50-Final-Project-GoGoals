import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///gogoals.db")


@app.route("/")
def frontpage():
    """A frontpage to showcase what GoGoals is about"""

    return render_template("frontpage.html")


@app.route("/home", methods=["GET", "POST"])
@login_required
def home():
    """Show todays goals and what to focus on"""
    if request.method == "GET":
        # First select all goals that are still active
        goals = db.execute("SELECT * FROM goals WHERE user_id = :user_id and done = 'No'", user_id=session["user_id"])

        # Get the number of goals to make sure user have any active goals
        numOfGoals = len(goals)

        steps = []
        currentComple = []
        successions = []
        goalName = []
        goal_id = []
        index = []
        flag = False

        for goal in goals:
            goalName.append(goal["goalName"])
            goal_id.append(goal["goal_id"])
            flag = False
            while flag == False:
                for i in range(1, 11):
                    number = str(i)
                    if goal["successions" + number] == None:
                        flag = True
                        break
                    if goal["currentComple" + number] < goal["successions" + number]:
                        steps.append(goal["step" + number])
                        currentComple.append(goal["currentComple" + number])
                        successions.append(goal["successions" + number])
                        index.append(number)
                        flag = True
                        break

        return render_template("home.html", goalName=goalName, numOfGoals=numOfGoals, goals=goals, steps=steps, currentComple=currentComple, successions=successions, index=index, goal_id=goal_id)
    else:
        # Get the goal ID from form
        goal_id = request.form.get("saveChangesGoal_id")

        # Get the step number so that we know what step to update
        stepNumber = request.form.get("stepNumber")

        # Get current Completions
        currentComple = request.form.get("currentComple")

        # Update the goals table's currentComple column
        db.execute("UPDATE goals SET currentComple" + stepNumber + " = :currentComple WHERE done = 'No' and goal_id = :goal_id", goal_id=goal_id, currentComple=currentComple)

        flash("Step changes has been saved!")
        return redirect("/home")

@app.route("/vision")
@login_required
def vision():
    """Article on how to make your life Vision"""
    return render_template("vision.html")


@app.route("/goals")
@login_required
def goals():
    """Show the current goals with deadlines, subgoals etc."""
    # Selecting all the rows from the goals database that belongs to the user logged in and which isn't marked as done
    goals = db.execute("SELECT * FROM goals WHERE user_id = :user_id and done = 'No'", user_id=session["user_id"])

    # Calculate the length of the goals dict, meaning the number of goals
    numOfGoals = len(goals)


    # Loop through the dict goals and store the values in variables to be used in the HTML

    if numOfGoals == 0:
        return render_template("goals.html", numOfGoals=numOfGoals)
    else:
        for goal in goals:
            goalName = goal["goalName"]
            visionLink = goal["visionLink"]
            deadline = goal["deadline"]
            subgoals = goal["subgoals"]
            step1 = goal["step1"]
            step2 = goal["step2"]
            step3 = goal["step3"]
            step4 = goal["step4"]
            step5 = goal["step5"]
            step6 = goal["step6"]
            step7 = goal["step7"]
            step8 = goal["step8"]
            step9 = goal["step9"]
            step10 = goal["step10"]
            successions1 = goal["successions1"]
            successions2 = goal["successions2"]
            successions3 = goal["successions3"]
            successions4 = goal["successions4"]
            successions5 = goal["successions5"]
            successions6 = goal["successions6"]
            successions7 = goal["successions7"]
            successions8 = goal["successions8"]
            successions9 = goal["successions9"]
            successions10 = goal["successions10"]
            currentComple1 = goal["currentComple1"]
            currentComple2 = goal["currentComple2"]
            currentComple3 = goal["currentComple3"]
            currentComple4 = goal["currentComple4"]
            currentComple5 = goal["currentComple5"]
            currentComple6 = goal["currentComple6"]
            currentComple7 = goal["currentComple7"]
            currentComple8 = goal["currentComple8"]
            currentComple9 = goal["currentComple9"]
            currentComple10 = goal["currentComple10"]
            goal_id = goal["goal_id"]
    return render_template("goals.html", numOfGoals=numOfGoals, goalName=goalName, visionLink=visionLink,
    deadline=deadline, subgoals=subgoals, goals=goals, goal=goal,
    step1=step1, step2=step2, step3=step3, step4=step4, step5=step5, step6=step6, step7=step7, step8=step8, step9=step9, step10=step10,
    successions1=successions1, successions2=successions2, successions3=successions3, successions4=successions4, successions5=successions5,
    successions6=successions6, successions7=successions7, successions8=successions8, successions9=successions9, successions10=successions10, goal_id=goal_id,
    currentComple1=currentComple1, currentComple2=currentComple2, currentComple3=currentComple3, currentComple4=currentComple4, currentComple5=currentComple5,
    currentComple6=currentComple6, currentComple7=currentComple7, currentComple8=currentComple8, currentComple9=currentComple9, currentComple10=currentComple10)


@app.route("/completeGoal", methods=["POST"])
def completeGoal():
    """Change the Done field in the goals DB to Yes"""
    # First get the goal name of completed goal
    goalName = request.form.get("completedGoalName")

    # Update table's done field for that goal
    db.execute("UPDATE goals SET done = 'Yes', completionDate = :completionDate WHERE user_id = :user_id and goalName = :goalName",
    user_id=session["user_id"], goalName=goalName, completionDate=datetime.now().strftime('%Y-%m-%d'))

    # Redirect to current goals page
    flash("Congratulations! You just completed one of your goals!")
    return redirect("/goals")



@app.route("/completedGoals")
@login_required
def completedGoals():
    """Page to see all the users completed goals"""
    # Selecting all the users goals from the goal DB where done equals yes
    goalsDone = db.execute("SELECT * FROM goals WHERE user_id = :user_id and done = 'Yes'", user_id=session["user_id"])

    numOfGoals = len(goalsDone)

    if numOfGoals == 0:
        return render_template("completedGoals.html", numOfGoals=numOfGoals)
    else:
        for goal in goalsDone:
            goalName = goal["goalName"]
            visionLink = goal["visionLink"]
            subgoals = goal["subgoals"]
            completionDate = goal["completionDate"]
    return render_template("completedGoals.html", goalsDone=goalsDone, goalName=goalName, visionLink=visionLink, subgoals=subgoals, completionDate=completionDate, numOfGoals=numOfGoals)


@app.route("/stepSuccesses", methods=["POST"])
def stepSuccesses():
    """Save step count to goals table"""
    # First get the goal ID of the goal that the step changes happened to
    goal_id = request.form.get("saveChangesGoal_id")


    for i in range(1, 11):
        # Variable number used to define what currentComple we are dealing with
        number = str(i)
        currentComple = request.form.get("currentComple" + number)
        # Now updating the goals table for that goal
        db.execute("UPDATE goals SET currentComple" + number + " = :currentComple WHERE done = 'No' and goal_id = :goal_id", goal_id=goal_id, currentComple=currentComple)

    flash("Step changes has been saved!")
    return redirect("/goals")




@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    #Error variable to store and display error messages
    error = None

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            error = 'Username or password is incorrect. Please try again.'
            return render_template("login.html", error=error)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/home")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/addGoal", methods=["GET", "POST"])
@login_required
def addGoal():
    """Making the user able to add goals"""
    if request.method == "GET":
        return render_template("addGoal.html")
    else:
        # Creating variables to store the data from the form in an easier to read way
        user_id = session["user_id"]
        goalName = request.form.get("nameOfGoal")
        visionLink = request.form.get("vision")
        stepsCount = int(request.form.get("stepsCount"))
        subgoals = request.form.get("subgoals")
        deadline = request.form.get("deadline")
        step1 = request.form.get("step1")
        successions1 = request.form.get("numOfSuccesses1")

        # Now insert the variables to the table
        db.execute("INSERT INTO goals (user_id, goalName, visionLink, step1, successions1, subgoals, deadline) VALUES (:user_id, :goalName, :visionLink, :step1, :successions1, :subgoals, :deadline)", user_id=user_id, goalName=goalName,
        step1=step1, successions1=successions1, visionLink=visionLink, subgoals=subgoals, deadline=deadline)

        # Getting the goal_id
        row = db.execute("SELECT * FROM goals WHERE user_id = :user_id ORDER BY goal_id DESC LIMIT 1", user_id=user_id)
        goal_id = row[0]["goal_id"]

        # For loops for inserting the rest of the steps and number of required successions into the goals table
        for i in range(2, stepsCount + 1):
            # Creating variables to store the steps and successions, i is here used to define what step and succession
            number = str(i)
            step = request.form.get("step" + number)
            successions = request.form.get("numOfSuccesses" + number)
            # Inserting the step and succession into the goals table
            db.execute("UPDATE goals SET step" + number + " = :step, successions" + number + " = :successions WHERE goal_id = :goal_id", step=step, successions=successions, goal_id=goal_id)

        # At last redirect the user to the home page, where the goal now should be visible
        return redirect("/goals")




@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    error = False
    usernameError = None
    emailError = None
    passwordError = None

    # If method equals post as by the user is submitting the register form
    if request.method == "POST":

        #Check to see if username is already taken and that emails and passwords match. HTML will check required and pattern
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        if len(rows) == 1:
            error = True
            usernameError = 'Username is already taken'

        if request.form.get("email") != request.form.get("emailConfirm"):
            error = True
            emailError = 'Emails does not match'

        if request.form.get("password") != request.form.get("passwordConfirm"):
            error = True
            passwordError = 'passwords does not match'

        if error == True:
            return render_template("register.html", error=error, usernameError=usernameError, emailError=emailError, passwordError=passwordError)

        # Insert the user into the users table to register them
        db.execute("INSERT INTO users (username, hash, firstName, lastName, email) VALUES (:username, :password, :firstName, :lastName, :email)",
        username=request.form.get("username"), password=generate_password_hash(request.form.get("password")),
        firstName=request.form.get("firstName"), lastName=request.form.get("lastName"), email=request.form.get("email"))

        # Query the database again to now have the registered user
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        #remember which user has logged in/registered
        session["user_id"] = rows[0]["id"]

        username = request.form.get("username")
        registered = True

        return render_template("home.html", registered=registered, username=username)

    else:
        return render_template("register.html")

    return apology("TODO")


@app.route("/profile")
@login_required
def profile():
    """Shows profile information"""
    # Select the logged in users profile information
    users = db.execute("SELECT * FROM users WHERE id = :user_id", user_id=session["user_id"])

    for user in users:
        username = user["username"]
        email = user["email"]
        firstName = user["firstName"]
        lastName = user["lastName"]
        password = user["hash"]
    return render_template("profile.html", username=username, firstName=firstName, lastName=lastName, password=password, email=email, users=users)



@app.route("/editProfile", methods=["GET", "POST"])
@login_required
def editProfile():
    """Edit profile information"""

    error = False
    usernameError = None
    emailError = None
    passwordError = None

    if request.method == "GET":
        # Select the logged in users profile information
        users = db.execute("SELECT * FROM users WHERE id = :user_id", user_id=session["user_id"])

        for user in users:
            username = user["username"]
            email = user["email"]
            firstName = user["firstName"]
            lastName = user["lastName"]
        return render_template("editProfile.html", username=username, firstName=firstName, lastName=lastName, email=email, users=users)
    else:
        # Make sure that error checking only happens when something is typed in
        if request.form.get("username") != '':
            #Check to see if username is already taken and that emails and passwords match. HTML will check required and pattern
            rows = db.execute("SELECT * FROM users WHERE username = :username",
                              username=request.form.get("username"))

            if len(rows) == 1:
                error = True
                usernameError = 'Username is already taken'

        if request.form.get("email") != '':
            email = db.execute("SELECT * FROM users WHERE email = :email", email=request.form.get("email"))

            if len(email) == 1:
                error = True
                emailError = 'Email already taken'
            elif request.form.get("email") != request.form.get("confirmEmail"):
                error = True
                emailError = 'Emails does not match'

        if request.form.get("password") != '':
            if request.form.get("password") != request.form.get("confirmPassword"):
                error = True
                passwordError = 'passwords does not match'

        if error == True:
            return render_template("editProfile.html", error=error, usernameError=usernameError, emailError=emailError, passwordError=passwordError)

        # If no errors was found Update users table
        if request.form.get("username") != '':
            username = request.form.get("username")
            db.execute("UPDATE users SET username = :username WHERE id = :user_id", user_id=session["user_id"], username=username)

        if request.form.get("email") != '':
            email = request.form.get("email")
            db.execute("UPDATE users SET email = :email WHERE id = :user_id", user_id=session["user_id"], email=email)

        if request.form.get("password") != '':
            password = request.form.get("password")
            db.execute("UPDATE users SET hash = :password WHERE id = :user_id", user_id=session["user_id"], password=generate_password_hash(password))

        if request.form.get("firstName") != '':
            firstName = request.form.get("firstName")
            db.execute("UPDATE users SET firstName = :firstName WHERE id = :user_id", user_id=session["user_id"], firstName=firstName)

        if request.form.get("lastName") != '':
            lastName = request.form.get("lastName")
            db.execute("UPDATE users SET lastName = :lastName WHERE id = :user_id", user_id=session["user_id"], lastName=lastName)

        return redirect("/profile")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
