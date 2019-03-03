from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('layout.html')

@app.route('/submission_test_form.html', methods = ['POST', 'GET'])
def test_form():
    if request.method == 'POST':
        results = request.form
        return render_template("submission_test_form.html", results = results)
    return render_template("submission_test_form.html")

if __name__ in '__main__':
    app.run(host='0.0.0.0')
