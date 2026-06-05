import customtkinter as ctk
import os
from PIL import Image

class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("YouTube")
        self.geometry("400x700")
        self.resizable(False, False)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=10, pady=10)

        img_path = os.path.join("Assests", "ytpre.png")
        self.logo = ctk.CTkImage(light_image=Image.open(img_path),dark_image=Image.open(img_path), size=(40, 40))

        logo_img = ctk.CTkLabel(header,text="",image=self.logo)
        logo_img.pack(side="left", padx=5)

        logo_text = ctk.CTkLabel(header,text="YouTube",font=("Arial", 22, "bold"))
        logo_text.pack(side="left")

        img_path = os.path.join("Assests", "man.png")
        self.profile = ctk.CTkImage(light_image=Image.open(img_path),dark_image=Image.open(img_path), size=(50, 50))

        profile_img = ctk.CTkLabel(header,text="",image=self.profile)
        profile_img.pack(side="right", padx=5)

        self.search_entry = ctk.CTkEntry(self,width=300,placeholder_text="Search videos...")
        self.search_entry.pack(pady=10)

        search_butn = ctk.CTkButton(self,text="Search",command=self.search)
        search_butn.pack(pady=10)

        category_frame = ctk.CTkFrame(self, fg_color="transparent")
        category_frame.pack(pady=10)

        cat_all=ctk.CTkButton(category_frame, text="All", width=70)
        cat_all.pack(side="left", padx=5)

        cat_music=ctk.CTkButton(category_frame, text="Music", width=70)
        cat_music.pack(side="left", padx=5)
        
        cat_gaming=ctk.CTkButton(category_frame, text="Gaming", width=70)
        cat_gaming.pack(side="left", padx=5)

        video_frame = ctk.CTkFrame(self)
        video_frame.pack(fill="x", padx=10, pady=10)

        video = ctk.CTkLabel(video_frame,text="Python Tutorial",font=("Arial", 16, "bold"))
        video.pack(anchor="w", padx=10, pady=5)

        video_desc = ctk.CTkLabel(video_frame,text="Code Channel • 100K views")
        video_desc.pack(anchor="w", padx=5, pady=5)

        video_frame2 = ctk.CTkFrame(self)
        video_frame2.pack(fill="x", padx=10, pady=10)

        video = ctk.CTkLabel(video_frame2,text="Java Tutorial",font=("Arial", 16, "bold"))
        video.pack(anchor="w", padx=10, pady=5)

        video_desc = ctk.CTkLabel(video_frame2,text="Programming Channel • 700K views")
        video_desc.pack(anchor="w", padx=5, pady=5)

        video_frame3 = ctk.CTkFrame(self)
        video_frame3.pack(fill="x", padx=10, pady=10)

        video = ctk.CTkLabel(video_frame3,text="React Tutorial",font=("Arial", 16, "bold"))
        video.pack(anchor="w", padx=10, pady=5)

        video_desc = ctk.CTkLabel(video_frame3,text="WebDev Channel • 798K views")
        video_desc.pack(anchor="w", padx=5, pady=5)

    def search(self):
        query = self.search_entry.get()
        print("Searching for:", query)

if __name__ == "__main__":
    app = GUI()
    app.mainloop()