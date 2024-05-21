# Jignesh Murugan, CIS 345, 12.00 pm, and Final Project
import csv
import random # We are going to generate random hours for the avg time spent each day graph.
import matplotlib.pyplot as plt # We are importing matplotlib to generate the graphs.

class InstagramUser:
    def __init__(self, filename='users.csv'): # We are creating a csv fle to hold username and password.
        self.filename = filename
        self.load_users()

    def load_users(self):
        self.users = {}
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        username, password = row
                        self.users[username] = password
        except FileNotFoundError:
            with open(self.filename, mode='w', newline='') as file:
                pass  # Create the file if it does not exist

    def authenticate(self, username, password): # We make sure that the username and the password matches or not.
        return self.users.get(username) == password

    def add_or_update_user(self, username, password):
        self.users[username] = password # We can add new username and password, or update the password of an already existing username.
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user, passw in self.users.items():
                writer.writerow([user, passw])

    def add_data(self, username, posts, followers, likes): # We are going to add a list for each user which consists of the number of posts, followers, and likes which the user inputs.
        data_filename = f'{username}_data.csv'
        with open(data_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([posts, followers, likes]) # We will keep track of it in a csv file for the user.

    def summarize_data(self, username, summary_type):
        data_filename = f'{username}_data.csv' # We are accessing the csv file of that particular user which consists of their data such as number of likes, followers, and posts.
        try:
            with open(data_filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # We skip the header.
                data = [row for row in reader]
                if summary_type == 'Average time spent per day':
                    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] # The days would be our column.
                    hours = [random.randint(1, 5) for _ in days] # We are creating a random number of hours for each day and the hours would be between 1 to 5.
                    plt.figure(figsize=(10, 5))
                    plt.bar(days, hours, color='blue')
                    plt.xlabel('Days of the Week') # This is our label for the column.
                    plt.ylabel('Hours Spent') # This is our label for the row.
                    plt.title('Average Time Spent per Day') # This is our title.
                    plt.show()
                elif summary_type == 'Time spent each day': # We are doing the same thing here as the Average time spent each day but instead of 1 to 5, it will be 1 to 10.
                    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                    hours = [random.randint(1, 10) for _ in days]
                    plt.figure(figsize=(10, 5))
                    plt.bar(days, hours, color='green')
                    plt.xlabel('Days of the Week')
                    plt.ylabel('Hours Spent')
                    plt.title('Time Spent Each Day')
                    plt.show()
                elif summary_type == 'Money earned': # We are calculating the money the user earned by posting.
                    total = sum(int(row[1]) + int(row[2]) + int(row[0]) for row in data) * 10 # The money earned will be 10 times the sum of number of posts, followers, and likes.
                    return f'Total money earned: ${total}'
                elif summary_type == 'Average likes per post':
                    total_posts = sum(int(row[0]) for row in data) # We are calculating the total posts.
                    total_likes = sum(int(row[2]) for row in data) # We are calculating the total likes.
                    if total_posts > 0: # We are seeing if there are any posts.
                        average_likes = total_likes / total_posts # Average likes will be the total likes divided by total posts.
                        return f'Average likes per post: {average_likes:.2f}'
                    else:
                        return 'No posts to calculate average likes.'
        except FileNotFoundError: # If the user did not input any data, then they will not have a file filled with their data, so we will return an error.
            return 'No data available.'
