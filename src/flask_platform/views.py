from flask import render_template
from flask_platform import app
import systeminfo
from systeminfo import info

@app.route('/')
def index():
	returnDict={}
	returnDict['user']=info.get_platform_info()
	returnDict['title']='home'
	return render_template("index.html",**returnDict)

