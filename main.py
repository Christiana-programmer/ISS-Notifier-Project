import requests
from datetime import datetime
import smtplib
import time
MY_LAT=9.081999
MY_LONG=8.675277
MY_EMAIL = "ifepythonmail4@gmail.com"
MY_PASSWORD= "cgpxlmmiufhvxnbe"
def is_iss_overhead():
    response=requests.get(url= "http://api.open-notify.org/iss-now.json")
    # print(response.status_code)
    response.raise_for_status()
    data = response.json()
    longitude= float(data["iss_position"]["longitude"])
    latitude= float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG +5:
        return True

def is_night():
    parameters ={
        "lat": MY_LAT,
         "lng":MY_LONG,
        "formatted": 0,
    }
    response= requests.get("https://api.sunrise-sunset.org/json",parameters)
    response.raise_for_status()
    data =response.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_position =(sunrise,sunset)
    # print(sunrise)
    # print(sunrise.split("T"))

    time_now =datetime.now().hour

    if time_now >= sunset or time_now<= sunrise:
        return True
    # print(time_now)
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # make our email secure
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="ifepythonmail4@yahoo.com",
                                msg=f"Subject: Look Up\n\n  The ISS is above you in the sky.")



