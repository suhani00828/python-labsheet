# Perform basic CRUD operations on an in-memory product dictionary.
products = {"P101": {"name": "Notebook", "price": 50.0, "stock": 20}}
while True:
    print("\n1 Add  2 View  3 Update  4 Delete  5 Exit")
    choice = input("Choose: ").strip()
    try:
        if choice == "1":
            product_id = input("Product ID: ").strip()
            if product_id in products:
                print("Product ID already exists.")
            else:
                products[product_id] = {"name": input("Name: ").strip(), "price": float(input("Price: ")), "stock": int(input("Stock: "))}
                print("Product added.")
        elif choice == "2":
            print(*[f"{key}: {value}" for key, value in products.items()], sep="\n") if products else print("No products.")
        elif choice == "3":
            product_id = input("Product ID: ").strip()
            if product_id in products:
                products[product_id] = {"name": input("New name: ").strip(), "price": float(input("New price: ")), "stock": int(input("New stock: "))}
                print("Product updated.")
            else:
                print("Product not found.")
        elif choice == "4":
            print("Product deleted." if products.pop(input("Product ID: ").strip(), None) else "Product not found.")
        elif choice == "5":
            break
        else:
            print("Choose an option from 1 to 5.")
    except ValueError:
        print("Price and stock must be numeric.")
