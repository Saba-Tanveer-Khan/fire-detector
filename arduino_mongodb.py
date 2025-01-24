from flask import Flask, request
from datetime import datetime  # Import datetime for timestamps
from pymongo import MongoClient  # Import MongoDB client

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('######')  # Replace with your MongoDB connection string
db = client['fire-db']  # Replace with your database name
fire_events_collection = db['fire_events']  # Collection to store fire events

# List to store fire detection events with timestamps
fire_events = []

@app.route('/fire-detected', methods=['GET'])
def fire_detected():
    # Get the current time when fire is detected
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create fire detection event with timestamp
    event = {"message": "Fire detected", "timestamp": current_time}
    
    # Add the event to the in-memory list
    fire_events.append(f"Fire detected at {current_time}")
    
    # Insert the event into MongoDB
    fire_events_collection.insert_one(event)  # Insert the event into the collection
    
    # Log event to the console
    print(f"Fire detected at {current_time}")
    
    return "Fire detection received and stored in MongoDB", 200

@app.route('/')
def index():
    # Fetch all events from MongoDB and store in a list
    events_from_db = list(fire_events_collection.find({}, {'_id': 0}))  # Fetch all records excluding the '_id' field
    
    # Initialize an empty list to store HTML formatted events
    event_list = []
    
    # Loop through the fetched events and format them as HTML list items
    for event in events_from_db:
        event_list.append(f"<li>{event['message']} at {event['timestamp']}</li>")
    
    # Create the HTML content
    if event_list:
        html_content = f"<h1>Fire Events:</h1> <ul>{''.join(event_list)}</ul>"
    else:
        html_content = "<h1>No fire events detected yet.</h1>"
    
    return html_content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
