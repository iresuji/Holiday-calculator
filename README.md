# Travel Cost Calculator

This is a simple Python script that helps users estimate the cost of their holiday based on various factors such as hotel stay, flight, and car rental. Users are prompted to input the destination city, the number of nights they plan to stay at a hotel, and the number of days for which they will be renting a car.

## Usage

1. Run the script.
2. Enter the destination city for your flight.
3. Provide the number of nights you will be staying at a hotel.
4. Input the number of days for which you will be renting a car.

The script will then calculate the individual costs for hotel stay, flight, and car rental, as well as the total cost of the holiday.

## Functions

1. **hotel_cost(num_nights, cost_of_stay):**
   - Calculates the cost of hotel stay based on the number of nights and a default cost of stay (default is $100 per night).

2. **plane_cost(city_flight):**
   - Determines the cost of the flight based on the destination city.

3. **car_rental(rental_days, cost_of_rental):**
   - Calculates the cost of car rental based on the number of days and a default cost of rental (default is $150 per day).

4. **holiday_cost(hotel_cost, plane_cost, car_rental):**
   - Combines the costs of hotel stay, flight, and car rental to calculate the total cost of the holiday.

## Example

```bash
python travel_cost_calculator.py

## Instructions

Follow the on-screen instructions to input the required information and view the estimated costs.

**Note:**
- Modify the default costs in the functions to customize the calculations according to your preferences.
- Feel free to use and modify this script to suit your needs for estimating travel costs!





