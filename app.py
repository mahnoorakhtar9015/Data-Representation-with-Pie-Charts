from flask import Flask,render_template,request

app=Flask(__name__)


@app.route('/', methods=['POST','GET'])

def get_data__show_chart():
    if request.method == 'POST': 
        title = request.form.get('title') 
        height = request.form.get('ht') 
        width = request.form.get('wt') 
    
        activity_1 = request.form.get('act1') 
        time1 = request.form.get('t1') 
    
        activity_2 = request.form.get('act2') 
        time2 = request.form.get('t2') 
    
        activity_3 = request.form.get('act3') 
        time3 = request.form.get('t3') 
    
        return render_template('chart.html',  
                                act1=activity_1,  
                                act2=activity_2,  
                                act3=activity_3,  
                                t1=time1, 
                                t2=time2, t3=time3,  
                                ht=height, wt=width,  
                                title=title) 
  
    return render_template('form.html', name='form') 


if __name__==('__main__'):
    app.run(debug=True)