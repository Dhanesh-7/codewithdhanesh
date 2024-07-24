import tkinter as tk
import requests
from PIL import Image, ImageTk
import webbrowser

# Function to get top 5 recipes
def get_top_5_recipes():
    recipe_name = entry_recipe_name.get()
    if recipe_name:
        api_url = "https://api.edamam.com/search"
        app_id = "your_app_id"
        app_key = "your_app_key"

        params = {
            "q": recipe_name,
            "app_id": app_id,
            "app_key": app_key,
            "from": 0,
            "to": 5,
        }

        response = requests.get(api_url, params=params)
        data = response.json()

        clear_recipe_list()

        if "hits" in data and data["hits"]:
            for i, hit in enumerate(data["hits"]):
                recipe_title = hit["recipe"]["label"]
                image_url = hit["recipe"]["image"]
                recipe_url = hit["recipe"]["url"]

                recipe_list.append(recipe_title)
                recipe_labels.append(tk.Label(canvas_frame, text=recipe_title, wraplength=200))
                recipe_labels[-1].pack()

                response = requests.get(image_url, stream=True)
                image = Image.open(response.raw)
                image = image.resize((200, 200), Image.LANCZOS)
                photo_image = ImageTk.PhotoImage(image)
                recipe_images.append(tk.Label(canvas_frame, image=photo_image))
                recipe_images[-1].image = photo_image
                recipe_images[-1].pack()

                recipe_links.append(tk.Button(canvas_frame, text="View Recipe", command=lambda url=recipe_url: open_link(url)))
                recipe_links[-1].pack()

# Function to clear recipe list
def clear_recipe_list():
    for label in recipe_labels:
        label.pack_forget()
    for image_label in recipe_images:
        image_label.pack_forget()
    for link_label in recipe_links:
        link_label.pack_forget()
    recipe_labels.clear()
    recipe_images.clear()
    recipe_links.clear()

# Function to open link
def open_link(link):
    webbrowser.open(link)

# Initialize Tkinter root window
root = tk.Tk()
root.title("Recipe Finder")
root.geometry("600x600")
root.configure(bg="#F1F1F1")

# Create a frame
frame = tk.Frame(root, bg="#F1F1F1")
frame.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=20)

# Create a label, entry, and search button
label_recipe_name = tk.Label(frame, text="Enter Recipe Name:", font=("Helvetica", 14, "bold"), bg="#F1F1F1")
label_recipe_name.pack()
entry_recipe_name = tk.Entry(frame, font=("Helvetica", 12))
entry_recipe_name.pack(pady=5)
search_button = tk.Button(frame, text="Search Recipes", font=("Helvetica", 12, "bold"), command=get_top_5_recipes)
search_button.pack(pady=10)

# Create a canvas for recipe display
canvas = tk.Canvas(frame, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

# Create a scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a frame inside the canvas
canvas_frame = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=canvas_frame, anchor=tk.NW)

# Bind canvas to scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Bind canvas to frame
canvas_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

# Initialize recipe lists
recipe_list = []
recipe_labels = []
recipe_images = []
recipe_links = []

# Start Tkinter event loop
root.mainloop()
