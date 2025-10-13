from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from utils import FormData, send_email
# from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# load_dotenv()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            form_data = FormData(
                name=request.form.get('name'),
                email=request.form.get('email'),
                subject=request.form.get('subject'),
                message=request.form.get('message')
            )

            send_email(form_data=form_data)
            
            # Check if it's an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({
                    'success': True, 
                    'message': 'Your message has been sent successfully!'
                })
            else:
                flash("Your message has been sent successfully!", "success")
                return redirect(url_for('home'))
                
        except Exception as e:
            # Handle errors for AJAX requests
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({
                    'success': False, 
                    'message': 'Failed to send message. Please try again.'
                }), 500
            else:
                flash("Failed to send message. Please try again.", "error")
                return redirect(url_for('home'))

    return render_template('index.html', is_message_sent=False)


if __name__ == '__main__':
    app.run(debug=True)