from pyscript import display

store_name = "BOOK NOOK"
owner = "by Gianna Entrada"
year_founded = 2023
popular_item_price = 540.20

has_books = True

product_names = ["Better than the Movies", "The Song of Achilles", "Six of Crows"]

business_hours = {"open": "10:00 AM", "close": "8:00 PM"}

menu_prices = {
    "Better than the Movies": 540.20,
    "The Song of Achilles": 500.20,
    "Six of Crows": 400.70,
    "Frankenstein and Cleopatra": 599.00,
    "Book Nook": 250.00
}

common_allergens = ["book", "booknook", "pages"]

tax_rate = 0.08

# Display store info
display(store_name, target="storename")
display(owner, target="ownerName")
display(year_founded, target="yearFounded")