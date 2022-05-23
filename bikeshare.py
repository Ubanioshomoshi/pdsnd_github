import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#lists for month and day to check user input validity
month_list=['january', 'february', 'march', 'april', 'may', 'june','all']
weekday_list=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']

#function to validate user input
def check_user_input(user_input,input_type):
    while True:
            input_user_entered=input(user_input).lower()
            try:
                if input_user_entered in ['chicago','new york city','washington'] and input_type == 'c':
                    break
                elif input_user_entered in month_list and input_type == 'm':
                    break
                elif input_user_entered in weekday_list and input_type == 'd':
                    break
                else:
                    if input_type == 'c':
                        print("Invalid Input!, input must be: chicago, new york city, or washington")
                    if input_type == 'm':
                        print("Invalid Input!, input must be: january, february, march, april, may, june or all")
                    if input_type == 'd':
                        print("Invalid Input!, input must be: sunday, ... friday, saturday or all")
            except ValueError:
                print("Sorry, your input is wrong")
    return input_user_entered

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = check_user_input("Would you like to see the data for chicago, new york city or washington?\n",'c')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = check_user_input("For filtering data by specific mounth please enter month name from (january, february, march, april, may, june) otherwise enter 'all'\n", 'm')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_user_input("For filtering data by specific day please enter day name from (sunday, monday, tuesday, wednesday, thursday, friday, saturday) otherwise enter 'all'\n", 'd')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and Hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month is: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Day Of the Week is: ', most_common_day)


    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour Of the Day is: ', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The Most Commonly used Start Station is: ', most_common_start_station)


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The Most Commonly used End Station is: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination=df.groupby(['Start Station','End Station'])
    most_frequent_station_combination = combination.size().sort_values(ascending=False).head(1)
    print('The Most frequent combination of Start Station and End Station trip is: ', most_frequent_station_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The Total Travel Time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The Mean Travel Time is: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of Each User Types: ',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
      gender_counts = df['Gender'].value_counts()
      print('\nGender Counts:\n', gender_counts)
    except KeyError:
      print("\nGender Counts:\nNo available data.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year_of_Birth = df['Birth Year'].min()
      print('\nEarliest Year of Birth:', Earliest_Year_of_Birth)
    except KeyError:
      print("\nEarliest Year of Birth:\n No available data.")

    try:
      Most_Recent_Year_of_Birth = df['Birth Year'].max()
      print('\nMost Recent Year of Birth:', Most_Recent_Year_of_Birth)
    except KeyError:
      print("\nMost Recent Year of Birth:\n No available data.")

    try:
      Most_Common_Year_of_Birth = df['Birth Year'].mode()[0]
      print('\nMost Common Year of Birth:', Most_Common_Year_of_Birth)
    except KeyError:
      print("\nMost Common Year of Birth:\n No available data.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#view raw data to user
def view_raw_data(df):
    row=0
    while True:
        rawData = input("Would you like to see the raw data?  Enter yes or no.\n").lower()

        if rawData == "yes":
            print(df.iloc[row : row + 6])
            row += 6
        elif rawData == "no":
            break
        else: #validate user input
            print("Sorry! You entered Wrong Input, Kindly try Again!")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
