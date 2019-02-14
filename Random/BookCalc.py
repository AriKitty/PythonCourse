book1 = "Design Patterns: Elements of Reusable Object-Oriented Software by Gamma, Helm, Johnson and Vlissides"
book2 = "Effective Java by Bloch"
book3 = "Java Puzzlers: Traps, Pitfalls and Corner Cases by Bloch and Gafter"
book1_price = 32.46
book2_price = 35.48
book3_price = 27.86

copies_book1 = int(input(f"How many copies of {book1} do you want? Price is ${book1_price}. "))
copies_book2 = int(input(f"How many copies of {book2} do you want? Price is ${book2_price}. "))
copies_book3 = int(input(f"How many copies of {book3} do you want? Price is ${book3_price}. "))

subtotal = copies_book1 * book1_price + copies_book2 * book2_price + copies_book3 * book3_price
print(f"Subtotal is ${subtotal:.2f}.")

tax_rate = .065
tax = subtotal * tax_rate
print(f"Tax is ${tax:.2f}.")
print(f"Total price is ${subtotal + tax:.2f}.")
