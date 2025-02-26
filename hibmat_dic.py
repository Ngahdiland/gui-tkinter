
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

class HibmatDictionaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dictionary")
        self.root.geometry("300x500")  # Adjust the size for all terms
        self.root.configure(bg="#04c524")

        # Create title label
        self.title_label = tk.Label(self.root, text="E RECODING SYSTEM", font=("Arial", 
        24, "bold"), bg="#000000", fg="#FFFFFF")

        # --- Term Definitions ---
        self.definitions = {
            "Data Mining": "The process of discovering patterns and insights from large datasets.",
            "Data Governance": "The process of managing and regulating data across an organization.",
        }

        # --- GUI Elements ---
        # Search Frame
        search_frame = ttk.Frame(root, padding=10)
        search_frame.pack( padx=10, pady=10)
        ttk.Label(search_frame, text="Search Term:", font=("Arial", 16), background="purple").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        self.search_entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        search_button = ttk.Button(search_frame, text="Search", command=self.search_term)
        search_button.pack(side=tk.LEFT, padx=5)

         # Add Frame
        add_frame = ttk.Frame(root, padding=10)
        add_frame.pack( padx=10, pady=10)
        ttk.Label(add_frame, text="Add Term:", font=("Arial", 16), background="purple").pack(side=tk.LEFT, padx=5)
        self.add_term_var = tk.StringVar()
        self.add_term_entry = ttk.Entry(add_frame, textvariable=self.add_term_var)
        self.add_term_entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        ttk.Label(add_frame, text="Add Definition:", font=("Arial", 16), background="purple").pack(side=tk.LEFT, padx=5)
        self.add_def_var = tk.StringVar()
        self.add_def_entry = ttk.Entry(add_frame,  textvariable=self.add_def_var)
        self.add_def_entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        add_button = ttk.Button(add_frame, text="Add", command=self.add_term)
        add_button.pack(side=tk.LEFT, padx=5)

        # Definition Display
        ttk.Label(root, text="Definition:", font=("Arial", 16), background="lightGreen").pack(padx=200, pady=10)
        #Increased height to display all definitions
        self.definition_display = scrolledtext.ScrolledText(root, height=15, wrap=tk.WORD) 
        self.definition_display.pack(expand=True, padx=10, pady=0)
        # Make it read-only
        self.definition_display.config(state=tk.DISABLED)  

    def search_term(self):
        term = self.search_var.get().strip()
        if term:
            if term in self.definitions:
               definition = self.definitions[term]
               self.update_definition_display(definition)
            else:
                 self.update_definition_display("Term not found in Dictionary... please add an arrticle if you have one")
        else:
            self.update_definition_display("Please enter term to search... ")

    def add_term(self):
        term = self.add_term_var.get().strip()
        definition = self.add_def_var.get().strip()
        if term and definition:
          self.definitions[term] = definition
          self.update_definition_display(f"Term '{term}' added to the dictionary.")
          self.add_term_var.set("") #Clear Entry box
          self.add_def_var.set("") #Clear Entry box

        else:
             messagebox.showerror("Error","Please fill out both term and definition.")

    def update_definition_display(self, text):
      self.definition_display.config(state=tk.NORMAL)
      self.definition_display.delete("1.0", tk.END)
      self.definition_display.insert(tk.END, text)
      self.definition_display.config(state=tk.DISABLED)



if __name__ == "__main__":
    root = tk.Tk()
    app = HibmatDictionaryApp(root)
    root.mainloop()
