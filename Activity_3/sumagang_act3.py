# Product Inventory Program

products = []
prices = []

# --- INPUT INITIAL PRODUCTS ---
num = int(input("Enter number of products: "))

for i in range(num):
    name = input(f"Enter product {i+1} name: ")
    
    # Validate price
    while True:
        try:
            price = float(input(f"Enter price of {name}: "))
            break
        except ValueError:
            print("Invalid price! Please enter a number.")
    
    products.append(name)
    prices.append(price)

print("----------------------------------------")
print("Product List:")
print(products)
print("Price List:")
print(prices)
print("----------------------------------------")

# --- MAIN LOOP ---
while True:
    print("Choose an action:")
    print("1 - Add a new product")
    print("2 - Remove a product")
    print("3 - Sort products by price")
    print("4 - Search for a product")

    choice = input("Enter your choice: ")

    # ADD PRODUCT
    if choice == "1":
        new_name = input("\nEnter new product name: ")
        
        while True:
            try:
                new_price = float(input(f"Enter price of {new_name}: "))
                break
            except ValueError:
                print("Invalid price! Please enter a number.")

        products.append(new_name)
        prices.append(new_price)
        print(f"{new_name} added successfully!")

    # REMOVE PRODUCT
    elif choice == "2":
        remove_name = input("Enter the product name to remove: ")

        if remove_name in products:
            index = products.index(remove_name)
            products.pop(index)
            prices.pop(index)
            print(f"{remove_name} removed successfully!")
        else:
            print("Product not found!")

    # SORT PRODUCTS
    elif choice == "3":
        print("Sort by price:")
        print("1 - Ascending")
        print("2 - Descending")
        sort_choice = input("Enter your choice: ")

        # Combine and sort
        combined = list(zip(products, prices))

        if sort_choice == "1":
            combined.sort(key=lambda x: x[1])
            print("Products sorted in ascending order by price!")
        elif sort_choice == "2":
            combined.sort(key=lambda x: x[1], reverse=True)
            print("Products sorted in descending order by price!")
        else:
            print("Invalid sort choice!")

        # Unzip back to lists
        products, prices = zip(*combined)
        products = list(products)
        prices = list(prices)

    # SEARCH PRODUCT
    elif choice == "4":
        search_name = input("Enter product name to search: ")
        
        if search_name in products:
            index = products.index(search_name)
            print("Product Found!")
            print(f"{search_name} - Price: {prices[index]}")
        else:
            print("Product not found!")

    else:
        print("Invalid choice!")

    # Display updated lists
    print("----------------------------------------")
    print("Updated Product List:")
    print(products)
    print("Price List:")
    print(prices)
    print("----------------------------------------")

    # Continue?
    again = input("Do you want to continue? (yes/no): ").lower()
    if again != "yes":
        break

print("Program terminated.")
print("Thank you for using the Product List Manager!")
