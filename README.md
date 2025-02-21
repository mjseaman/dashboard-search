Grafana Dashboard Table Scanner
==============================

A web application that scans a Grafana instance for dashboards containing table panels and displays their queries. This tool helps you inventory and analyze table queries across your Grafana dashboards.

FEATURES
--------
* Web interface for easy access
* Scans all dashboards in a Grafana instance
* Identifies dashboards containing table panels
* Extracts and displays queries from table panels
* Supports both Prometheus queries and other data sources
* Direct links to original dashboards

INSTALLATION
-----------
1. Clone the repository:
   git clone https://github.com/yourusername/grafana-dashboard-scanner.git
   cd grafana-dashboard-scanner

2. Create and activate a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install required packages:
   pip install -r requirements.txt

USAGE
-----
1. Start the web server:
   python app.py

2. Open your web browser and navigate to:
   http://localhost:5000

3. Enter your Grafana details:
   - Grafana URL (e.g., http://your-grafana-instance)
   - API Token (create one in Grafana under Configuration > API Keys)

4. Click "Get Dashboards" to view the results

GETTING A GRAFANA API TOKEN
--------------------------
1. Log into your Grafana instance
2. Go to Configuration > API Keys
3. Click "Add API key"
4. Give it a name and select "Viewer" role
5. Click "Add"
6. Copy the generated token (you won't be able to see it again)

PROJECT STRUCTURE
---------------
grafana-dashboard-scanner/
├── app.py                    # Flask web application
├── dashboards_with_tables.py # Grafana scanning logic
├── requirements.txt         # Python dependencies
└── templates/
    └── index.html          # Web interface template

CONTRIBUTING
-----------
Contributions are welcome! Please feel free to submit a Pull Request.

LICENSE
-------
This project is licensed under the MIT License - see the LICENSE file for details.