def rent_movie(inventory, movie_name):
    if movie_name not in inventory:
        return f"Error: {movie_name} not available in our inventory"
    
    if inventory[movie_name]["quantity"] > 0:
        inventory[movie_name]["quantity"] -= 1
        inventory[movie_name]["times_rented"] += 1
        return f"Rented: {movie_name} (${inventory[movie_name]['rental_price']})"
    else:
        return f"Sorry, {movie_name} is out of stock"

def return_movie(inventory, movie_name):
    if movie_name in inventory:
        inventory[movie_name]["quantity"] += 1
        return f"Returned: {movie_name}"
    else:
        return f"Error: {movie_name} not in our system"

def show_movie_details(inventory):
    print("\n=== MOVIE RENTAL INVENTORY ===")
    for movie, details in inventory.items():
        print(f"\nMovie: {movie}")
        print(f"Rental Price: ${details['rental_price']}")
        print(f"Available Copies: {details['quantity']}")
        print(f"Rating: {details['rating']}")
        print(f"Times Rented: {details['times_rented']}")

def add_movie(inventory, movie_name, rental_price, quantity, rating):
    inventory[movie_name] = {
        "rental_price": rental_price,
        "quantity": quantity,
        "rating": rating,
        "times_rented": 0  # New feature to track popularity
    }

def most_popular_movies(inventory):
    print("\n=== MOST POPULAR RENTALS ===")
    sorted_movies = sorted(inventory.items(), 
                         key=lambda x: x[1]['times_rented'], 
                         reverse=True)
    top_three = sorted_movies[:3]  # Gets top 3
    
    for movie, details in top_three:
        print(f"\nMovie: {movie}")
        print(f"Times Rented: {details['times_rented']}")
    
    return top_three  # Still returns the data if needed

# Your full code would now be:
inventory = {}

# Add movies
add_movie(inventory, "Die Hard", 7, 5, "R")
add_movie(inventory, "Miller's Crossing", 7, 5, "R")
add_movie(inventory, "Inside Out", 5, 8, "G")
add_movie(inventory, "Cars", 8, 3, "PG")

# Rent movies
print("\n=== RENTAL TRANSACTIONS ===")
print(rent_movie(inventory, "Cars"))
print(rent_movie(inventory, "Cars"))  # Note: This will fail because Python is case-sensitive
print(rent_movie(inventory, "Miller's Crossing"))
print(rent_movie(inventory, "Miller's Crossing"))
print(rent_movie(inventory, "Miller's Crossing"))

# Return movies
print("\n=== RETURN TRANSACTIONS ===")
print(return_movie(inventory, "Cars"))
print(return_movie(inventory, "Miller's Crossing"))

# Show current inventory
show_movie_details(inventory)

# Show most popular movies
most_popular_movies(inventory)