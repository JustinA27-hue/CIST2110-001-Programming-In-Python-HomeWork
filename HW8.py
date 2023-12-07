# HW8.py
# Author: Justin Agosto

# This homework will exapnd upon the code for Lab9.py. If you did not complete Lab9.py, you should do so before attempting this homework.

# Copy the code from Lab9.py into this file. I'll add some comments to help you out.

# Import statements (activate venv and install streamlit if you haven't already)


import streamlit as st
import datetime as dt

# Streamlit title, subtitle, date, and button
def title():
    st.title("Date Counter")
    return

def subheader():
    st.subheader("Enter a date and click the button to see how many days until that date.")
    return

def date_input():
    date = st.date_input("Enter a date")
    return date

def button():
    button = st.button("Click me")
    return button



# The calculate_days function from Lab9.py

def calculate_days(date):
    today = dt.date.today()
    days = date - today
    return days.days






# START OF HOMEWORK Questions

# 1. Create a function calculate_days_until_birthday that will calculate how many days from now until the user's birthday. The function should take in the user's birthday as a parameter and return the number of days until their birthday. The function should also display the number of days until their birthday in the Streamlit app. The function should be called in the app function.
def calculate_days_until_birthday(birthday):
    current_date = dt.datetime.now().date()
    birthday = dt.datetime.strptime(birthday, '%Y-%m-%d').date()
    if birthday < current_date:
        birthday = birthday.replace(year=current_date.year + 1)
    days_until_birthday = birthday - current_date
    return days_until_birthday.days


# 2. Create a function days_until_semester_ends that will calculate how many days from now until the end of the semester. The function should take in the current date as a parameter and return the number of days until the end of the semester. The function should also display the number of days until the end of the semester in the Streamlit app. The function should be called in the app function.
# Hint: You can use the date object to create a date for the end of the semester. IE.
# end_of_semester = dt.date(2023, 12, 8)
def days_until_semester_ends(current_date):
    end_of_semester = dt.date(2023, 12, 8)
    days_until_semester_ends = end_of_semester - current_date
    return days_until_semester_ends.days
# 3. Create a function days_until_new_years that will calculate how many days from now until New Year's Day. The function should take in the current date as a parameter and return the number 
# of days until New Year's Day. The function should also display the number of days until New Year's Day in the Streamlit app. The function should be called in the app function. Also include 
# an emoji of a party popper in the Streamlit app.
# Hint: You can use the date object to create a date for New Years. IE. 
# new_years = dt.date(2024, 1, 1)
# Hint: To add an emoji, use the st.write() function. IE. st.write("🎉")
def days_until_new_years(current_date):
    new_years = dt.date(2024, 1, 1)
    days_until_new_years = new_years - current_date
    emoji = st.write("🎉")
    return days_until_new_years.days

# 4. create a button that will display the number of days until New Year's Day when clicked. The button should be labeled "Days until New Year's Day". The button should call the 
# days_until_new_years function when clicked. The button should be placed below the "Calculate" button.Inside the app function call the days_until_new_years function when the button is clicked.
def new_years_button():
    new_years_button = st.button("Days until New Year's Day")
    return new_years_button
# Hint: You can use the st.button() function. IE. button = st.button("Click me")
# Hint2: the days_until_new_years function takes in the current date as a parameter. You can use the dt.datetime.now().date() function to get the current date. 
# IE. current_date = dt.datetime.now().date()
# Hint3: You can use the days_until_new_years function to get the number of days until New Year's Day. IE. days_until_new_years(current_date) This is where you include the emoji  🎉


# app function from Lab9.py
def app():
    title()
    subheader()
    date = date_input()
    button_click = button()
    if button_click:
        try:
            days = calculate_days(date)
            st.write(days)
        except:
            st.write("Please enter a valid date")
    return
if __name__ == '__main__':
    app()