
#you can figuire out everything thats missing im not going to baby you
@app.route('/yoururl', methods=['POST'])
def receive_prices():
    global prices
    prices = request.json
