# Jignesh Murugan, CIS 345, 12.00 pm, and Final Project
# My drop down boxes display better when it is in full screen. Please have it on full screen while trying it out and look at the code editor while choosing to display graphs.
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from Jmurugan_class import InstagramUser # We are importing the class from the Jmurugan_class for functionality.

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def decorate_frame(frame):
    frame.config(bg=bg_color)

def show_login():
    clear_frame(main_frame)
    decorate_frame(main_frame)
# We are creating widgets for the login page. Here we have login or create account and both will take us to the next page whatever the input is as of right now.
    username_entry = tk.Entry(main_frame)
    password_entry = tk.Entry(main_frame, show='*')

    def try_login():
        global current_user
        if user_manager.authenticate(username_entry.get(), password_entry.get()):
            current_user = username_entry.get()
            show_second_page()
        else:
            messagebox.showerror("Login Error", "Incorrect username or password")

    tk.Label(main_frame, text="Username", bg=bg_color, fg=fg_color).pack()
    username_entry.pack()
    tk.Label(main_frame, text="Password", bg=bg_color, fg=fg_color).pack()
    password_entry.pack()
    tk.Button(main_frame, text="Login", command=try_login, bg=button_color, fg=fg_color).pack(pady=10)
    tk.Button(main_frame, text="Create Account", command=show_create_account, bg=button_color, fg=fg_color).pack()

def show_create_account():
    clear_frame(main_frame)
    decorate_frame(main_frame)
# We are creating widget creating account.
    new_username_entry = tk.Entry(main_frame)
    new_password_entry = tk.Entry(main_frame, show='*')

    def try_create_account():
        user_manager.add_or_update_user(new_username_entry.get(), new_password_entry.get())
        global current_user
        current_user = new_username_entry.get()
        messagebox.showinfo("Account Created", "Your account has been created/updated successfully.")
        show_second_page()

    tk.Label(main_frame, text="New Username", bg=bg_color, fg=fg_color).pack()
    new_username_entry.pack()
    tk.Label(main_frame, text="New Password", bg=bg_color, fg=fg_color).pack()
    new_password_entry.pack()
    tk.Button(main_frame, text="Create Account", command=try_create_account, bg=button_color, fg=fg_color).pack(pady=10)

def show_second_page(): # Function for the second(main page).
    clear_frame(main_frame)
    decorate_frame(main_frame)
# We are placing 2 images which resembles posts from the instagram users.
    img1 = PhotoImage(file="../../Downloads/Jmurugan_projectfinal/Pic1.png")
    img2 = PhotoImage(file="../../Downloads/Jmurugan_projectfinal/Pic2.png")
    tk.Label(main_frame, image=img1, bg=bg_color).pack(side='left', padx=10)
    tk.Label(main_frame, image=img2, bg=bg_color).pack(side='right', padx=10)

    main_frame.image1 = img1
    main_frame.image2 = img2

# We are creating dropdown actions. We will have a go button to take us to the next page after selecting a dropdown. We will also have a exit button.
    actions = ttk.Combobox(main_frame, values=["Submit Data", "View Summary"], state="readonly")
    actions.pack()
    tk.Button(main_frame, text="Go", command=lambda: take_action(actions.get()), bg=button_color, fg=fg_color).pack(pady=10)
    tk.Button(main_frame, text="Exit", command=root.destroy, bg=button_color, fg=fg_color).pack(pady=10)

def take_action(action): # This is displayed after we select the choose action drop down.
    if action == "Submit Data":
        show_data_entry_page() # If the user selects the submit data button we will call this function.
    elif action == "View Summary":
        show_summary_page() # If they choose the view summary button then we will call this function.
    else:
        messagebox.showinfo("Try again", "You selected an invalid option") # If no action is selected then we display an error.

def show_data_entry_page(): # This will have 3 entry points for number of posts, followers, and likes.
    clear_frame(main_frame)
    decorate_frame(main_frame)
    posts_entry = tk.Entry(main_frame)
    followers_entry = tk.Entry(main_frame)
    likes_entry = tk.Entry(main_frame)

    def submit_data():
        user_manager.add_data(current_user, posts_entry.get(), followers_entry.get(), likes_entry.get())
        messagebox.showinfo("Data Submitted", "Your data has been submitted successfully.")
        show_second_page()

    tk.Label(main_frame, text="Number of Posts", bg=bg_color, fg=fg_color).pack()
    posts_entry.pack()
    tk.Label(main_frame, text="Number of Followers", bg=bg_color, fg=fg_color).pack()
    followers_entry.pack()
    tk.Label(main_frame, text="Number of Likes", bg=bg_color, fg=fg_color).pack()
    likes_entry.pack()
    tk.Button(main_frame, text="Submit", command=submit_data, bg=button_color, fg=fg_color).pack(pady=10)
    tk.Button(main_frame, text="Back", command=show_second_page, bg=button_color, fg=fg_color).pack(pady=10)

def show_summary_page():  # This page will have drop down box with 4 options.
    clear_frame(main_frame)
    decorate_frame(main_frame)
    summary_options = ttk.Combobox(main_frame, values=["Average time spent per day", "Time spent each day", "Money earned", "Average likes per post"], state="readonly")
    summary_options.pack()

    def show_selected_summary(): # After selecting the show button, this function is called.
        selection = summary_options.get()
        result = user_manager.summarize_data(current_user, selection)
        if isinstance(result, str):
            messagebox.showinfo("Summary", result)
        show_second_page()

    tk.Button(main_frame, text="Show", command=show_selected_summary, bg=button_color, fg=fg_color).pack(pady=10)
    tk.Button(main_frame, text="Back", command=show_second_page, bg=button_color, fg=fg_color).pack(pady=10)

root = tk.Tk()
root.title("Instagram User Dashboard")
root.geometry("800x500") # We set the size of the window as 800 * 500.

bg_color = "DarkOrchid3" # This is our overall background color.
fg_color = "snow" # white background.
entry_bg = "gray33" # This is our entry background.
button_color = "SlateBlue1" # This is our button color.
font_style = ("Helvetica", 12, "bold")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)
decorate_frame(main_frame)

user_manager = InstagramUser()
current_user = ""

show_login()

root.mainloop()