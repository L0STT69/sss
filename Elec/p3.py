import tkinter as tk

def open_homepage():
    app.destroy()  # Close the User Profile Page
    # Add code to open the Homepage (create a new instance of the homepage)

app = tk.Tk()
app.title("SHOWTIME - User Profile")

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

# User profile information (replace with actual user data)
user_name = tk.Label(content, text="User's Name")
user_name.pack()
user_email = tk.Label(content, text="user@example.com")
user_email.pack()
user_watchlist = tk.Label(content, text="Watchlist")
user_watchlist.pack()
user_history = tk.Label(content, text="Recently Watched Items")
user_history.pack()
user_settings = tk.Label(content, text="Account Settings")
user_settings.pack()

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
