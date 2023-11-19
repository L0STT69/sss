import tkinter as tk

def open_homepage():
    # Add code to open the Homepage
    pass

app = tk.Tk()
app.title("SHOWTIME - Movie Details")

# Header
header = tk.Frame(app, height=50, bg="blue")
header.pack(fill=tk.X)

logo = tk.Label(header, text="SHOWTIME", font=("Helvetica", 20), fg="white", bg="blue")
logo.pack(side=tk.LEFT, padx=20, pady=5)

search_bar = tk.Entry(header, width=30)
search_bar.pack(side=tk.LEFT, padx=10, pady=5)

profile_button = tk.Button(header, text="User Profile", fg="white", bg="blue", command=open_homepage)
profile_button.pack(side=tk.RIGHT, padx=20, pady=5)

# Content
content = tk.Frame(app, bg="white")
content.pack(pady=20)

# Movie details (replace with actual data)
movie_poster = tk.Label(content, text="Movie Poster")
movie_poster.pack()
movie_title = tk.Label(content, text="Movie Title")
movie_title.pack()
movie_details = tk.Label(content, text="Year: 2023 | Genre: Action | Rating: 7.5")
movie_details.pack()
movie_description = tk.Label(content, text="Movie description and plot summary.")
movie_description.pack()

# Related movies (replace with actual movie posters)
related_movies = tk.Label(content, text="Related Movies")
related_movies.pack()

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
