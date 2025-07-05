import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

# Create destination folder
UPLOAD_FOLDER = "uploaded_images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def upload_image():
    # Open file dialog to select image
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )
    
    if file_path:
        # Get the filename
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(UPLOAD_FOLDER, file_name)
        
        # Copy the selected file to the upload folder
        shutil.copy(file_path, dest_path)
        messagebox.showinfo("Success", f"Image uploaded to {dest_path}")
    else:
        messagebox.showwarning("Cancelled", "No image selected.")

# Create GUI window
window = tk.Tk()
window.title("Image Upload")
window.geometry("300x150")

upload_btn = tk.Button(window, text="Upload Image", command=upload_image)
upload_btn.pack(pady=50)

window.mainloop()
