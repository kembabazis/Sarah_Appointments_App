#importing flask
from flask import Flask
#app is a flask object, name helps determine the root path
app = Flask(_name_)
# connecting all pages to python function/mapping
@app.route('/')
def index():
#return 'This is the homepage'

# making the website runs when the script is run
# only run the app when this script is run directly(frm ur main file)
if __name__ =="_main_":
    print ("This is the homepage")
    app.run(debug=True)









