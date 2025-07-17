from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/litterbox_data', methods=['GET'])
def get_litterbox_data():
    # Simulated data for the litterbox
    data = [
        {
            "enter_time": "2025-07-10T07:12:03",
            "exit_time": "2025-07-10T07:14:23",
            "weight_enter": 10.55,
            "weight_exit": 10.62
        },
        {
            "enter_time": "2025-07-10T12:43:10",
            "exit_time": "2025-07-10T12:45:15",
            "weight_enter": 10.57,
            "weight_exit": 10.66
        },
        {
            "enter_time": "2025-07-11T08:01:55",
            "exit_time": "2025-07-11T08:03:30",
            "weight_enter": 10.63,
            "weight_exit": 10.70
        },
        {
            "enter_time": "2025-07-11T19:15:21",
            "exit_time": "2025-07-11T19:17:05",
            "weight_enter": 10.65,
            "weight_exit": 10.72
        },
        {
            "enter_time": "2025-07-12T06:45:32",
            "exit_time": "2025-07-12T06:47:10",
            "weight_enter": 10.62,
            "weight_exit": 10.68
        },
        {
            "enter_time": "2025-07-13T13:30:40",
            "exit_time": "2025-07-13T13:33:20",
            "weight_enter": 10.66,
            "weight_exit": 10.73
        },
        {
            "enter_time": "2025-07-14T09:22:15",
            "exit_time": "2025-07-14T09:24:05",
            "weight_enter": 10.69,
            "weight_exit": 10.76
        },
        {
            "enter_time": "2025-07-15T17:50:11",
            "exit_time": "2025-07-15T17:51:59",
            "weight_enter": 10.72,
            "weight_exit": 10.79
        },
        {
            "enter_time": "2025-07-16T10:18:09",
            "exit_time": "2025-07-16T10:20:40",
            "weight_enter": 10.75,
            "weight_exit": 10.81
        },
        {
            "enter_time": "2025-07-17T07:05:03",
            "exit_time": "2025-07-17T07:07:45",
            "weight_enter": 10.77,
            "weight_exit": 10.84
        }
    ]
    return jsonify(data)
    
    