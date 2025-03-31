from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to SecureFeedback!"

@app.route('/feedback', methods=['POST'])
def feedback():
    user_feedback = request.form.get('feedback')
    # Insecure for now – we'll fix that later
    with open("feedback.txt", "a") as f:
        f.write(user_feedback + "\n")
    return "Feedback received securely!"

if __name__ == "__main__":
    app.run(debug=True)
