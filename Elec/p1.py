import tkinter as tk

def open_movie_details_page():
    # Add code to open the Movie Details Page
    pass

def open_user_profile_page():
    # Add code to open the User Profile Page
    pass

app = tk.Tk()
app.title("SHOWTIME - Home")

# Header
header = tk.Frame(app, height=50, bg="blue")
header.pack(fill=tk.X)

logo = tk.Label(header, text="SHOWTIME", font=("Helvetica", 20), fg="white", bg="blue")
logo.pack(side=tk.LEFT, padx=20, pady=5)

search_bar = tk.Entry(header, width=30)
search_bar.pack(side=tk.LEFT, padx=10, pady=5)

profile_button = tk.Button(header, text="User Profile", fg="white", bg="blue", command=open_user_profile_page)
profile_button.pack(side=tk.RIGHT, padx=20, pady=5)

# Content
content = tk.Frame(app, bg="white")
content.pack(pady=20)

title = tk.Label(content, text="Featured Movies", font=("Helvetica", 16))
title.pack()

# Featured movies (replace with actual movie posters and data)
movie1 = tk.Label(content, text="Movie 1 Poster")
movie1.pack(pady=10)
movie2 = tk.Label(content, text="Movie 2 Poster")
movie2.pack(pady=10)
movie3 = tk.Label(content, text="Movie 3 Poster")
movie3.pack(pady=10)

# Footer
footer = tk.Frame(app, height=50, bg="blue")
footer.pack(side=tk.BOTTOM, fill=tk.X)

about_link = tk.Label(footer, text="About Us", fg="white", bg="blue")
about_link.pack(side=tk.LEFT, padx=20)
help_link = tk.Label(footer, text="Help Center", fg="white", bg="blue")
help_link.pack(side=tk.LEFT, padx=20)
terms_link = tk.Label(footer, text="Terms of Service", fg="white", bg="blue")
terms_link.pack(side=tk.LEFT, padx=20)
privacy_link = tk.Label(footer, text="Privacy Policy", fg="white", bg="blue")
privacy_link.pack(side=tk.LEFT, padx=20)
contact_link = tk.Label(footer, text="Contact Us", fg="white", bg="blue")
contact_link.pack(side=tk.LEFT, padx=20)

app.mainloop()
