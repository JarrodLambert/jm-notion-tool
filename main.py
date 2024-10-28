import os
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Notion client with your integration token from environment variables
notion = Client(auth=os.getenv("NOTION_API_TOKEN"))

# Function to retrieve entries from a source database with specific filters
def get_entries_from_source_database(source_database_id, project_value):
    response = notion.databases.query(
        database_id=source_database_id,
        filter={
            "and": [
                {
                    "property": "Project",
                    "select": {
                        "equals": project_value
                    }
                },
                {
                    "property": "Client Facing",
                    "checkbox": {
                        "equals": True
                    }
                }
            ]
        }
    )
    return response.get('results', [])

# Function to delete all entries in the target database
def clear_target_database(target_database_id):
    response = notion.databases.query(database_id=target_database_id)
    entries = response.get('results', [])
    for entry in entries:
        notion.pages.update(page_id=entry['id'], archived=True)

# Function to map multi-select values from source to target
def map_multi_select_values(source_tags, mapping_dict=None):
    if mapping_dict is None:
        # If no mapping dictionary is provided, use the source names directly
        return [{"name": tag['name']} for tag in source_tags]
    else:
        # Map each source tag to its corresponding target tag using the mapping dictionary
        return [{"name": mapping_dict.get(tag['name'], tag['name'])} for tag in source_tags]

# Function to copy entries to a target database
def copy_entries_to_target_database(entries, target_database_id):
    # Example mapping dictionary for multi-select values
    multi_select_mapping = {
        "MOD Forever - Evelyn": "Evelyn",
        "MOD Forever - Gene": "Gene",
        "MOD Forever - Joi": "Joi"
    }
    
    for entry in entries:
        # Extract properties from the source entry
        source_properties = entry['properties']
        
        # Debugging: Print the entire properties dictionary
        print("Source properties:", source_properties)
        
        # Corrected property name for Interactive
        interactive_tags = source_properties.get("Interactive", {}).get("multi_select", [])
        print("Source multi-select values for 'Interactive':", [tag['name'] for tag in interactive_tags])
        
        # Map properties to the target database format
        target_properties = {
            "Issue": source_properties.get("Name"),
            "JM Notes (Notes)": source_properties.get("Notes"),
            "Status": {
                "select": {
                    "name": source_properties.get("Status", {}).get("select", {}).get("name", "")
                }
            },
            "Metahuman": {
                "multi_select": map_multi_select_values(interactive_tags, multi_select_mapping)
            },
            "MOD Notes / Suggested Solution": source_properties.get("Client Notes")
            # Add more properties as needed
        }
        
        try:
            # Create a new page in the target database with the mapped properties
            notion.pages.create(
                parent={"database_id": target_database_id},
                properties=target_properties
            )
        except Exception as e:
            print(f"Error creating page for entry: {e}")

def main():
    source_database_id = "12d5b5537b898016a724e78fc81494be"
    target_database_id = "12d5b5537b8980e5ab31fc73c108738a"
    project_value = "mod-forever"  # Replace with the actual project value you want to filter by
    
    # Clear the target database
    clear_target_database(target_database_id)
    
    # Get entries from the source database with specific filters
    entries = get_entries_from_source_database(source_database_id, project_value)
    
    # Copy entries to the target database
    copy_entries_to_target_database(entries, target_database_id)

if __name__ == "__main__":
    main()
