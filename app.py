from flask import Flask, render_template, request, flash
import requests
from dashboards_with_tables import get_dashboards_with_tables

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        grafana_url = request.form.get('grafana_url', '').rstrip('/')
        api_token = request.form.get('api_token', '')
        
        try:
            # Modify the get_dashboards_with_tables function to accept parameters
            results = get_dashboards_with_tables(grafana_url, api_token)
        except Exception as e:
            flash(f"Error: {str(e)}", 'error')
    
    return render_template('index.html', results=results)

if __name__ == '__main__':
    # Update these parameters to allow external access
    app.run(host='0.0.0.0', port=5000, debug=True) 