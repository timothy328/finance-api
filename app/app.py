from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

@app.route('/health_check')
def health_check():
  """Simple health check endpoint."""
  return jsonify({'status': 'healthy'})

@app.route('/random_decimal')
def get_random_decimal():
  """Generates a random decimal number between -1 and 1 (inclusive)."""
  random_number = random.uniform(-100, 100) 
  variable = 'HELLO'
  with open('output/random_decimals.txt', 'a') as f:
    f.write(str(random_number) + '\n')
  return jsonify({'random_decimal': random_number})



# Function with 3 arguments
@app.route('/multiply_and_add', methods=['POST'])
def multiply_and_add_json():
  """API endpoint for multiply_and_add function using JSON data."""
  data = request.get_json()  # Get JSON data from request body
  x = data.get('x')
  y = data.get('y')
  z = data.get('z')
  
  # x = float(request.form['x'])  # Access form data by key
  # y = float(request.form['y'])
  # z = float(request.form['z'])
  
  # Error handling (optional)
  if not all([x, y, z]):
      return jsonify({'error': 'Missing arguments'}), 400  # Bad request

  result = float(x) * float(y) + float(z)
  return jsonify({'result': result})

@app.route('/form')
def show_form():
  return render_template('form.html')  # Render the form template




if __name__ == '__main__':
  app.run(debug=True)


# Use GET for retrieving data.
# Use POST for creating new resources.
# Use PUT for complete updates or replacements.
# Use PATCH for partial updates.
# Use DELETE for removing resources.