from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory data storage (replace with a proper database in production)
assessments = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store_assessment', methods=['POST'])
def store_assessment():
    data = request.json

    # Store the assessment data (replace with actual data storage mechanism)
    assessments.append(data)

    return jsonify({'message': 'Assessment data received successfully'})

if __name__ == "__main__":
    app.run(debug=True)
