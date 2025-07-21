from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import random
import uuid

app = Flask(__name__)

# Single cat and litterbox data
CAT = {"id": 1, "name": "Atticus", "weight": 9, "breed": "Domestic Longhair"}
LITTER_BOX = {"id": "box_001", "location": "living_room", "type": "manual"}

def generate_fake_litterbox_usage_data(days=7):
    """Generate fake litterbox usage data for the specified number of days."""
    data = []

    # Start from 7 days ago
    start_date = datetime.now() - timedelta(days=days)
    
    for day in range(days):
        current_date = start_date + timedelta(days=day)

        # cat uses litterbox 2-4 times a day
        daily_uses = random.randint(2, 4)

        for use in range(daily_uses):
            # Random time during the day
            hour = random.randint(6, 23)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)

            enter_time = current_date.replace(hour=hour, minute=minute, second=second)
    
            # Duration between 30 seconds to 5 minutes
            duration_seconds = random.randint(30, 300)
            exit_time = enter_time + timedelta(seconds=duration_seconds)

            # weight calculation
            base_weight = CAT['weight']
            weight_enter = round(base_weight + random.uniform(-0.1, 0.1), 2)
            
            # Weight loss between 0.05 and 1 lb
            waste_weight = round(random.uniform(0.05, 1.0), 2)
            weight_exit = round(weight_enter - waste_weight, 2)

            entry = {
                "id": str(uuid.uuid4()),
                "cat_id": CAT['id'],
                "litterbox_id": LITTER_BOX['id'],
                "enter_time": enter_time.isoformat(),
                "exit_time": exit_time.isoformat(),
                "weight_enter": weight_enter,
                "weight_exit": weight_exit,
                "timestamp": datetime.now().isoformat()
            }

            data.append(entry)

        # sort by enter_time
        data.sort(key=lambda x: x['enter_time'])
    return data

# Generate the fake data once when the server starts
FAKE_LITTERBOX_USAGE_DATA = generate_fake_litterbox_usage_data(7)

@app.route('/')
def home():
    """API information endpoint."""
    return jsonify({
        "message": "Welcome to the Cat Litterbox API",
        "endpoints": {
            "/cat": "Get cat information",
            "/litterbox_usage_data": "Get simulated litterbox usage data"
        }
    })

@app.route('/litterbox_usage_data', methods=['GET'])
def get_litterbox_usage_data():
    """Get all litterbox usage with optional filtering."""

    # Query parameters for filtering
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # filter data based on query parameters
    filtered_data = FAKE_LITTERBOX_USAGE_DATA.copy()

    if start_date:
        try:
            start_date = datetime.fromisoformat(start_date)
            filtered_data = [entry for entry in filtered_data if datetime.fromisoformat(entry['enter_time']) >= start_date]
        except ValueError:
            return jsonify({"error": "Invalid start_date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)"}), 400

    if end_date:
        try:
            end_date = datetime.fromisoformat(end_date)
            filtered_data = [entry for entry in filtered_data if datetime.fromisoformat(entry['exit_time']) <= end_date]
        except ValueError:
            return jsonify({"error": "Invalid end_date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)"}), 400

    return jsonify(filtered_data)


@app.route('/cat', methods=['GET'])
def get_cat_info():
    """Get information about the cat."""
    return jsonify(CAT)


    
    