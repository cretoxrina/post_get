import tkinter as tk
from tkinter import messagebox
import requests

class OrderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FastAPI Order Management")

        self.create_order_frame = tk.Frame(root)
        self.create_order_frame.pack(pady=10)
        create_order_label = tk.Label(self.create_order_frame, text="Create Order")
        create_order_label.pack()

        products_label = tk.Label(self.create_order_frame, text="Product:")
        products_label.pack()
        self.products_entry = tk.Entry(self.create_order_frame)
        self.products_entry.pack()

        currency_label = tk.Label(self.create_order_frame, text="Currency:")
        currency_label.pack()
        self.currency_entry = tk.Entry(self.create_order_frame)
        self.currency_entry.pack()

        external_id_label = tk.Label(self.create_order_frame, text="External ID:")
        external_id_label.pack()
        self.external_id_entry = tk.Entry(self.create_order_frame)
        self.external_id_entry.pack()

        description_label = tk.Label(self.create_order_frame, text="Description:")
        description_label.pack()
        self.description_entry = tk.Entry(self.create_order_frame)
        self.description_entry.pack()

        create_order_button = tk.Button(self.create_order_frame, text="Create Order", command=self.create_order)
        create_order_button.pack()

    def create_order(self):
        products = self.products_entry.get()
        currency = self.currency_entry.get()
        external_id = self.external_id_entry.get()
        description = self.description_entry.get()

        data = {
            "products": products.split(', '),
            "currency": currency,
            "external_id": external_id,
            "description": description
        }

        response = requests.post("https://api-dev.asadalpay.com/api/orders/create-order", json=data)

        if response.status_code == 303:
            checkout_url = response.headers["location"]
            messagebox.showinfo("Order Created", f"Order created successfully!\nCheckout URL: {checkout_url}")
        else:
            error_message = response.json()["detail"]
            messagebox.showerror("Order Creation Failed", f"Failed to create order. Error: {error_message}")

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderGUI(root)
    root.mainloop()
