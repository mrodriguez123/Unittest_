from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods= ['POST'])
def index_post():
	facts= {}
	facts['name'] = request.json['name']
	facts['school'] = request.json['school']
	facts['sports'] = request.json['sports']
	return facts

@app.route('/get', methods= ['GET'])
def index_get():
	result= 'result'
	return jsonify({'key' : [0,1,2,3]})


if __name__ == '__main__':
    app.run()(debug= True)
