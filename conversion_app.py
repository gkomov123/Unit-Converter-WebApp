from flask import Flask, render_template, request

app = Flask(__name__)

#Conversion rules dict
conversions = {
    "temperature": {
        "CtoF": {"func": lambda x:round(x * 9/5 + 32),
                 "unit": "°F"},
        "FtoC": {"func": lambda x:round((x - 32) * 5/9),
                 "unit": "°C"}
    },
    "weight": {
        "kgToLb": {"func": lambda x:x * 2.205,
                 "unit": "lb"},
        "lbToKg": {"func": lambda x:x * 0.4536,
                 "unit": "kg"}},

    "length": {
        "mToFt": {"func": lambda x:x * 3.28084,
                 "unit": "ft"},
        "ftToM": {"func": lambda x:x * 0.3048,
                 "unit": "m"},
        "mmtToCm": {"func": lambda x:x / 10,
                 "unit": "cm"},
        "cmtToMm": {"func": lambda x:x * 10,
                 "unit": "mm"}}
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    unit_label = None
    if request.method == "POST":
        value = float(request.form["value"])
        conversion_category = request.form["category"]
        conversion_type = request.form["unit"]

        conversion = conversions[conversion_category][conversion_type]
        result = conversion["func"](value)
        unit_label = conversion["unit"]
    return render_template('index.html', result=result, unit_label=unit_label)

if __name__ == "__main__":
    app.run(debug=True)