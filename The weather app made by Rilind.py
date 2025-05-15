import requests

while True:
    try:
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))
    except ValueError:
        print("Please enter valid numbers for latitude and longitude.")
        continue

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)

    if response.status_code != 200:
        print("Bad connection or invalid coordinates.")
        continue

    data = response.json()

    if "current_weather" not in data:
        print("Weather data not available for this location.")
        continue

    weather = data["current_weather"]
    temp = weather["temperature"]
    wind = weather["windspeed"]
    direction = weather["winddirection"]
    is_day = weather["is_day"]

    print("It's daytime." if is_day == 1 else "It's nighttime.")
    print(f"The temperature is {temp}°C with winds at {wind}km/h at {direction}°.")

    # Log to file (optional in Mimo)
    try:
        with open("weather_log.txt", "a") as file:
            file.write(f"{lat}, {lon}: {temp}°C, {wind} km/h wind, {direction}°\n")
    except:
        print("(Couldn't write to file — maybe not supported in this environment.)")

    again = input("Check another location? (y/n): ").strip().lower()
    if again != "y":
        break
