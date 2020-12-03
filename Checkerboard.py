from flask import Flask,render_template
app = Flask(__name__)    

@app.route('/')          
def rebeat():
    return render_template('mkd.html', x=8 ,y=8, color1="red" ,color2="black")

@app.route('/<int:x>') 
def rebeat_x(x):
    return render_template('mkd.html', x=x ,y=8, color1="red" ,color2="black" )

@app.route('/<int:x>/<int:y>') 
def rebeat_y(x,y):
    return render_template('mkd.html', x=x ,y=y, color1="red" ,color2="black" )

@app.route('/<int:x>/<int:y>/<color1>/<color2>') 
def rebeat_c(x,y,color1,color2):
    return render_template('mkd.html', x=x ,y=y, color1=color1,color2=color2 )

# @app.route('/say/<name>') 
# def hello(name):
#     print(name)
#     return "Hi " + name

# @app.route('/rebeat/<num>/<name>')
# def rebeat(num,name):
#     return name*int(num)


if __name__=="__main__":     
    app.run(debug=True)   
