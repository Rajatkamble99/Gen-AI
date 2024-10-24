import json

# A utility function to get products and categories
def get_products_and_category():
    return {
        "Computers and Laptops": [
            "TechPro Ultrabook",
            "BlueWave Gaming Laptop",
            "PowerLite Convertible",
            "TechPro Desktop",
            "BlueWave Chromebook"
        ],
        "Smartphones and Accessories": [
            "SmartX ProPhone",
            "MobiTech PowerCase",
            "SmartX MiniPhone",
            "MobiTech Wireless Charger",
            "SmartX EarBuds"
        ],
        "Televisions and Home Theater Systems": [
            "CineView 4K TV",
            "SoundMax Home Theater",
            "CineView 8K TV",
            "SoundMax Soundbar",
            "CineView OLED TV"
        ],
        "Gaming Consoles and Accessories": [
            "GameSphere X",
            "ProGamer Controller",
            "GameSphere Y",
            "ProGamer Racing Wheel",
            "GameSphere VR Headset"
        ],
        "Cameras and Camcorders": [
            "FotoSnap DSLR Camera",
            "ActionCam 4K",
            "FotoSnap Mirrorless Camera",
            "ZoomMaster Camcorder",
            "FotoSnap Instant Camera"
        ]
    }

# A function to parse a customer query and return the products and categories
def get_products_from_query(query):
    products_and_category = get_products_and_category()
    matching_products = []

    for category, products in products_and_category.items():
        for product in products:
            if product.lower() in query.lower():
                matching_products.append({"category": category, "product": product})

    return matching_products

# Converts a string representation of products into a Python list
def read_string_to_list(products_string):
    # Check if the input is already a list
    if isinstance(products_string, list):
        return products_string
    # If it's a string, process it to convert to a list
    try:
        return json.loads(products_string.replace("'", '"'))
    except json.JSONDecodeError:
        return []

# Retrieves information of mentioned products from the list
def get_mentioned_product_info(products_list):
    products_info = get_products_and_category()  # Assuming this retrieves product info
    mentioned_info = []
    
    for item in products_list:
        category = item.get('category')
        product = item.get('product')
        if category and product:
            if product in products_info.get(category, []):
                mentioned_info.append({"category": category, "product": product})
    
    return mentioned_info

# Generates the answer for the user message based on the product information
def answer_user_msg(user_msg, product_info):
    response = []
    for item in product_info:
        category = item.get('category')
        product = item.get('product')
        response.append(f"The {product} belongs to {category} category.")
    
    return " ".join(response)

