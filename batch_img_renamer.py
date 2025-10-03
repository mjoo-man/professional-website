import os
from tkinter import Tk, Label, Entry, Button, filedialog
from PIL import Image, ImageTk, ExifTags


class ImageRenamer:
    def __init__(self, master, image_folder, valid_exts):
        self.master = master
        self.image_folder = image_folder
        
        self.file_list = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(valid_exts)])
        self.index = 0

        self.label = Label(master)
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.button = Button(master, text="Rename and Next", command=self.rename_next)
        self.button.pack()

        self.show_image()

    def show_image(self):
        if self.index >= len(self.file_list):
            self.label.config(text="All done!")
            self.entry.destroy()
            self.button.destroy()
            return

        self.filename = self.file_list[self.index]
        path = os.path.join(self.image_folder, self.filename)
        img = Image.open(path)
        img.thumbnail((800, 600))
        self.tkimg = ImageTk.PhotoImage(img)
        self.label.config(image=self.tkimg)

    def rename_next(self):
        new_name = self.entry.get().strip()
        if new_name:
            ext = os.path.splitext(self.filename)[1]
            os.rename(
                os.path.join(self.image_folder, self.filename),
                os.path.join(self.image_folder, new_name + ext)
            )
        self.entry.delete(0, 'end')
        self.index += 1
        self.show_image()

def fix_img_rotations(folder):

    for filename in os.listdir(folder):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            path = os.path.join(folder, filename)
            image = Image.open(path)

            try:
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == 'Orientation':
                        break

                exif = image._getexif()
                if exif and orientation in exif:
                    orient = exif[orientation]

                    if orient == 3:
                        image = image.rotate(180, expand=True)
                    elif orient == 6:
                        image = image.rotate(270, expand=True)
                    elif orient == 8:
                        image = image.rotate(90, expand=True)

                    # Save without EXIF
                    image.save(path, exif=b"")
                    print(f"Fixed orientation: {filename}")
            except Exception as e:
                print(f"Skipped {filename}: {e}")


if __name__ == "__main__":

    image_folder = "content/projects/bakerrisk/gallery/Photos-1-001"
    valid_exts = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".JPG")

    fix_img_rotations(image_folder)
    
    root = Tk()
    app = ImageRenamer(root, image_folder, valid_exts)
    root.mainloop()

