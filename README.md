# ISS Overhead Notifier

Python script that emails you when the ISS is overhead at night.

## How it works
- Tracks ISS position using Open Notify API
- Checks sunrise/sunset via Sunrise-Sunset API
- Sends Gmail alert if ISS is overhead during nighttime

## Usage
1. Install requirements: `pip install requests`
2. Update your latitude, longitude, email, and password in the script
3. Run: `python main.py`
