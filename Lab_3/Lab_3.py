from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"
if __name__ == '__main__':
    app.run()

from flask import render_template, request

@app.route ('/form', methods = ['GET', 'POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return 'Hello'+ name
    return render_template ('form.html')

from flask import render_template, request

@app.route ('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()
    if request.method ==['POST']:
        form.Validate_on_submit()
    name =form.name.data
    return 'Hello'+ name
    return render_template ('form.html', form=form)
