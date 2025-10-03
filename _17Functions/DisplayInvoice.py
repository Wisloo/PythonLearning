def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f}")
    print(f"is due on {due_date}")

display_invoice("Wisloo", 15000, "04/10/2025")