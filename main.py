from flask import Flask, render_template, request, redirect
app = Flask('app')

contacts = [
  {'title': 'João da Silva' },
  {'title': 'Maria Souza'}
]

@app.route('/create', methods=['POST'])
def create():
  title = request.form.get('title')
  contacts.append({'title': title})
  return redirect('/')

@app.route('/')
def index():
  return render_template('index.html',contacts=contacts)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)