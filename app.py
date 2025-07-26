from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pizza():
    if request.method == 'POST':
        category = request.form.get('category')
        ptype = request.form.get('type')
        cheese = request.form.get('cheese')
        topping = request.form.get('topping')
        water = int(request.form.get('water', 0))
        ketchup = int(request.form.get('ketchup', 0))
        softdrinks = int(request.form.get('softdrinks', 0))
        takeaway = request.form.get('takeaway')

        # Pricing
        v, nv, dv, dnv = 300, 400, 600, 800
        ch, top, bo, kt, sd, twc = 100, 100, 20, 5, 75, 20

        t = 0

        # Base price
        if category == 'normal':
            t += v if ptype == 'veg' else nv
        elif category == 'deluxe':
            t += dv if ptype == 'veg' else dnv

        # Add-ons
        if cheese: t += ch
        if topping: t += top
        t += water * bo
        t += ketchup * kt
        t += softdrinks * sd
        if takeaway: t += twc

        # GST and total
        gst = (t * 18) / 100
        total = t + gst

        return render_template('pizza.html', total=total, gst=gst, t=t)

    return render_template('pizza.html', total=None)

if __name__ == '__main__':
    app.run(debug=True)

