
import tkinter as tk
from tkinter import ttk, messagebox

class ReceiptGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("E RECORD SYSTEM")
        self.root.configure(bg="#04c524")
        self.items = []
        self.item_options = ["Boster", "33 Export", "Ice", "Muzic", "Kadji", "Chill", "Malta", "smooth"]
        self.item_prices = {
            "Boster": 800,
            "33 Export": 800,
            "Ice": 700,
            "Muzic": 750,
            "Kadji": 500,
            "Chill": 700,
            "Malta": 500,
            "smooth": 800,

        }

        # Create title frame
        self.title_frame = tk.Frame(self.root,
        bg="#000000")
        self.title_frame.grid(row=0, column=0,
        columnspan=2, padx=20, pady=20)


        # Create title label
        self.title_label = tk.Label(self.title_frame, 
        text="E RECODING SYSTEM", font=("Arial", 
        24, "bold"), bg="#000000", fg="#FFFFFF")
        self.title_label.pack(fill="x", padx=20, pady=20)

        # Create item name frame
        self.item_name_frame = tk.Frame(self.root, 
        bg="#04c524")
        self.item_name_frame.grid(row=1, column=0, 
        padx=20, pady=10)
        # Create item name label
        self.item_name_label = tk.Label(self.
        item_name_frame, text="Item Name:", font=
        ("Arial", 16), bg="#FFFFFF")
        self.item_name_label.pack(side="left", padx=10)

        # Create item name dropdown

        self.item_name_var = tk.StringVar()
        self.item_name_dropdown = ttk.Combobox(self.
        item_name_frame, textvariable=self.item_name_var)
        self.item_name_dropdown['values'] = self.item_options
        self.item_name_dropdown.pack(side="left", padx=10)
        self.item_name_dropdown.bind("<<ComboboxSelected>>", self.auto_fill_price)

        # Create item price frame
        self.item_price_frame = tk.Frame(self.root, 
        bg="#04c524")
        self.item_price_frame.grid(row=2, column=0, 
        padx=20, pady=10)

        # Create item price label
        self.item_price_label = tk.Label(self.
        item_price_frame, text="Item Price(FCFA):", 
        font=("Arial", 16), bg="#FFFFFF")
        self.item_price_label.pack(side="left", 
        padx=10)

        # Create item price entry

        self.item_price_entry = tk.Entry(self.item_price_frame, font=("Arial", 16))
        self.item_price_entry.pack(side="left", padx=10)

        # Create quantity frame

        self.quantity_frame = tk.Frame(self.root, 
        bg="#04c524")
        self.quantity_frame.grid(row=3, column=0, 
        padx=20, pady=10)


        # Create quantity label

        self.quantity_label = tk.Label(self.
        quantity_frame, text="Quantity:", font=
        ("Arial", 16), bg="#FFFFFF")
        self.quantity_label.pack(side="left", 
        padx=10)
        
        
        # Create quantity entry

        self.quantity_entry = tk.Entry(self.
        quantity_frame, font=("Arial", 16))
        self.quantity_entry.pack(side="left", 
        padx=10)

         # Create button frame
        self.button_frame = tk.Frame(self.root, 
        bg="#04c524")
        self.button_frame.grid(row=4, column=0, 
        padx=20, pady=20)
         
        # Create add item button

        self.add_item_button = tk.Button(self.
        button_frame, text="Add Item", 
        command=self.add_item, font=("Arial", 
        16), bg="#000000", fg="#FFFFFF")
        self.add_item_button.pack(side="left", 
        padx=10)

        # Create label to display total
        self.total_label = tk.Label(root, text="Total: (FCFA): 0.00", font=("Arial", 24, "bold"), bg="#000000", fg="#FFFFFF")
        self.total_label.grid(row=24, column=0)

        # Create button to generate receipt
        self.generate_receipt_button = tk.Button(self.button_frame, text="Generate Receipt", command=self.generate_receipt, 
        font=("Arial", 16), bg="#000000", 
        fg="#FFFFFF")
        self.generate_receipt_button.pack(side="left", padx=10)
        self.item_info_frame = tk.Frame(self.
        root, bg="#FFFFFF")
        self.item_info_frame.grid(row=5, 
        column=0, padx=20, pady=20)

        # Create item info Frame
        self.item_info_frame = tk.Frame(self.root, bg="#FFFFFF")
        self.item_info_frame.grid(row=1, column=1, rowspan=4, padx=20, pady=20, sticky="n")

        # Create item info label
        self.item_info_label = tk.Label(self.
        item_info_frame, text="Item Information:", font=("Arial", 16), 
        bg="#04c524")
        self.item_info_label.pack(side="top", 
        padx=10, pady=10)
        # Create item info text
        self.item_info_text = tk.Text(self.
        item_info_frame, width=40, height=10, 
        font=("Arial", 16))
        self.item_info_text.pack(side="top", 
        padx=10, pady=10)
        # Create total frame
        self.total_frame = tk

    def auto_fill_price(self, event):
        selected_item = self.item_name_var.get()

        price = self.item_prices[selected_item]
        self.item_price_entry.delete(0, tk.END)
        self.item_price_entry.insert(0, price)

    def add_item(self):
        item_name = self.item_name_var.get()
        item_price = float(self.item_price_entry.get())
        quantity = int(self.quantity_entry.get())
        total_price = item_price * quantity

        self.items.append({
            "item_name": item_name,
            "item_price": item_price,
            "quantity": quantity,
            "total_price": total_price
        })

        self.item_name_var.set("")
        self.item_price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

        self.display_item_info()
        self.update_total()

    def display_item_info(self):
        self.item_info_text.delete(1.0, tk.END)
        for i, item in enumerate(self.items, start=1):
            self.item_info_text.insert(tk.END, f"{i}. {item['item_name']} = {item['item_price']} x {item['quantity']} = {item['total_price']:.2f}\n")

    def update_total(self):
        total = sum(item["total_price"] for item in self.items)
        self.total_label['text'] = f"Total(FCFA): {total:.2f}"

    def generate_receipt(self):

        grand_total = sum(item["total_price"] for item in self.items)

        with open("receipt.txt", "w") as file:
            file.write("Receipt\n")
            file.write("--------\n")
            for i, item in enumerate(self.items, start=1):
                file.write(f"{i}. {item['item_name']} = {item['item_price']} x {item['quantity']} = {item['total_price']:.2f}\n")
            file.write(f"Grand Total(FCFA): {grand_total:.2f}\n")

        messagebox.showinfo("Receipt Generated", "Receipt saved to receipt.txt")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReceiptGenerator(root)
    root.mainloop()
