#Get the city the user will be flying to
city_flight = input('Please enter the city you will be flying to: ')
#Get the number of nights they will be staying
num_nights = int(input('Please enter the number of nights you will be staying at a hotel: '))
#Get the number of days which they will be hiring a car
rental_days = int(input('Please enter the number of days you will be renting a car: '))

#Create a function that takes the number of nights as arguments and return total cost of stay
def hotel_cost(num_nights, cost_of_stay = 100):
    cost = num_nights * cost_of_stay
    return cost
    
#Call the function to get hotel cost
hotel_cost_result = hotel_cost(num_nights)   
    
#Create a function that takes the city they are flying to and return cost of the flight
def plane_cost(city_flight):
    if city_flight == "Paris":
        cost_of_flight = 150
    elif city_flight == "Sevilla":
        cost_of_flight = 250
    elif city_flight == "Rome":
        cost_of_flight = 135
    else:
        cost_of_flight = 125
        
    return cost_of_flight
    
    
#Call the function to get plane cost
plane_cost_result = plane_cost(city_flight)
    
    
#Create a function that take rental days as an argument and return the cost of the car rental
def car_rental(rental_days, cost_of_rental = 150):
    cost = rental_days * cost_of_rental
    return cost
    
#Call the function to get car rental cost   
car_rental_result = car_rental(rental_days)

#Create a function that takes the three previous functions and combine with a total cost for the holiday.
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost = hotel_cost + plane_cost + car_rental
    return total_cost

#Call the function to get total holiday cost    
final_cost = holiday_cost(hotel_cost_result, plane_cost_result, car_rental_result)

#Print the individuals and final holiday cost
print(f'The cost of spending {num_nights} nights at the hotel is {hotel_cost_result}')
print(f'The cost of flying to {city_flight} is {plane_cost_result}')
print(f'The cost of renting a car for {rental_days} days is {car_rental_result}')
print(f'The total cost of the holiday is {final_cost}')