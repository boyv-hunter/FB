from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    # Get form data
    name = request.form.get('name')
    dob = request.form.get('dob')
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Render the success page with user data
    return render_template(
        'success.html', 
        name=name, 
        dob=dob, 
        email=email, 
        password=password
    )

if __name__ == '__main__':
    app.run(debug=True)
