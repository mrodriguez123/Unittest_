from flask import Flask, request, jsonify
app = Flask(__name__)

# sent the post with postman app- sends json 
dictionary= { "name": " Monica",
    	"school": " University of Wisconsin",
    	"sports": " rowing" }

@app.route("/")
def index():
	return "Welcome to my page"


@app.route('/post', methods= ['POST'])
def index_post():
	facts= {}
	facts['name'] = request.json['name']
	facts['school'] = request.json['school']
	facts['sports'] = request.json['sports']
	return facts

@app.route('/get', methods= ['GET'])
def index_get():
	#result= 'result'
	nums= {'nums' : [0,1,2,3]}
	return jsonify(nums)


if __name__ == '__main__':
    app.run()(debug= True)
