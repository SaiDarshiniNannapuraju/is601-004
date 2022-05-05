from flask import Flask, render_template, request
from AdvCalc import AdvCalc
import csv
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/load_basic_csv/<operation>')
def load_mixed_csv(operation):
    html_content = ["<html>"]
    with open("Unity_Test_Addition.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()
        cal = AdvCalc()
        for row in csv_reader:
            v1 = int(row[0])
            v2 = int(row[1])
            if operation == "add":
                print("Performing addition")
                cal.addition(v1, v2)
            elif operation == "sub":
                print("Performing Subtraction")
                cal.subtraction(v1, v2)
            elif operation == "div":
                cal.division(v1, v2)
                print("Performing division")
            elif operation == "mult":
                cal.multiplication(v1, v2)
                print("Performing multiplication")
            data = "{0} {1} {2} = {3}".format(v1, operation, v2, cal.ans)
            #print(data)
            html_content.append("<p>{}</p>".format(data))
    html_content.append("</html>")
    return "".join(html_content)

@app.route('/load_adv_csv/')
def load_advance_csv(op):
    df = pd.read_csv ('CSV file path')
    mean = df['Value1'].mean()
    median = df['Value1'].median()
    mode = df['Value1'].mode()
    std = df['Value1'].std()
    print("Mean: "+str(mean))
    print("Median: "+str(median))
    print("Mode: "+str(mode))
    print("Standard Deviation: "+str(std))

@app.route('/result/', methods=['POST'])
def result():
    """Route where we send calculator form input"""

    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name= "
    first_input = request.form['input'].strip(',')
    operation = request.form['operation']

    try:
        adv_cal_obj = AdvCalc()
        inputvalues  = [float(num) for num in first_input.split(',')]

        if operation == "mean":
            result = adv_cal_obj.mean(data=inputvalues)
            msg = "Mean for {} is: {}".format(first_input, result)
        elif operation == "median":
            result = adv_cal_obj.median(data=inputvalues)
            msg = "Median for {} is: {}".format(first_input, result)
        elif operation == "mode":
            result = adv_cal_obj.mode(data=inputvalues)
            msg = "Mode for {} is: {}".format(first_input, result)
        elif operation == "std_dev":
            result = adv_cal_obj.standard_deviation(data=inputvalues)
            msg = "Standard Deviation for {} is: {}".format(first_input, result)
        else:
            operation = "z_score"
            result = adv_cal_obj.z_score(data=inputvalues)
            msg = "Z score for {} is: {}".format(first_input, result)
        return render_template(
                'index.html',
                message = msg,
                calculation_success=True
                )
    except ValueError:
        return render_template(
                'index.html',
                message = "Please check you input data {}".format(first_input),
                calculation_success=False
                )

if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0")
