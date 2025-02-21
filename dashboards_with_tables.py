import requests
import json

def get_dashboards_with_tables(grafana_url, api_token):
    # Create auth header with token
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    # Get all dashboards
    search_url = f"{grafana_url}/api/search"
    response = requests.get(search_url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to get dashboards: {response.status_code}")

    dashboards_with_tables = []
    
    # Iterate through each dashboard
    for dashboard in response.json():
        dashboard_uid = dashboard.get('uid')
        if not dashboard_uid:
            continue
            
        # Get detailed dashboard info
        dashboard_url = f"{grafana_url}/api/dashboards/uid/{dashboard_uid}"
        dash_response = requests.get(dashboard_url, headers=headers)
        
        if dash_response.status_code != 200:
            continue
            
        dash_data = dash_response.json()
        dashboard_model = dash_data['dashboard']
        
        # Function to recursively search for table panels
        def find_table_panels(panels):
            table_queries = []
            for panel in panels:
                if panel.get('type') == 'table':
                    # Extract queries from the panel
                    for target in panel.get('targets', []):
                        if 'expr' in target:  # For Prometheus
                            table_queries.append(target['expr'])
                        elif 'query' in target:  # For other datasources
                            table_queries.append(target['query'])
                
                # Check nested panels if they exist
                if 'panels' in panel:
                    table_queries.extend(find_table_panels(panel['panels']))
            return table_queries

        # Find all table panels and their queries
        table_queries = find_table_panels(dashboard_model.get('panels', []))
        
        if table_queries:
            # Get folder information
            folder_title = dashboard.get('folderTitle', 'General')
            if folder_title == '':
                folder_title = 'General'
                
            dashboards_with_tables.append({
                'name': dashboard['title'],
                'folder': folder_title,
                'url': f"{grafana_url}/d/{dashboard_uid}",
                'table_queries': table_queries
            })
    
    return dashboards_with_tables 