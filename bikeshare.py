import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington':  'washington.csv' }
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAYS_OF_WEEK = ['all', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

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
    try:
        my_cities = [key[0] for key in CITY_DATA.items()]
        input_city = input("Enter City from the following options: {} ".format(my_cities))
        if input_city not in my_cities:
            print('city not found, please enter city from options')
            get_filters()

        # TO DO: get user input for month (all, january, february, ... , june)
        my_months = [month for month in MONTHS]
        input_month = input("Enter month from the following options: {} ".format(my_months))
        if input_month not in my_months:
            print('Month not found, please enter month from options')
            get_filters()

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        my_days = [day for day in DAYS_OF_WEEK]
        input_day = input("Enter day from the following options: {} ".format(my_days))
        if input_day not in my_days:
            print('Day not found, please enter day from options')
            get_filters()
    except Exception as e:
        print('Lets try again! Please enter the right input from the options given. {}'.format(e))
        get_filters()

    print('-'*40)
    return input_city, input_month, input_day


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
    input_city = city.lower()
    input_month = month.lower()
    input_day = day
    df = pd.read_csv(CITY_DATA[input_city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if input_month != 'all':
          input_month_number = MONTHS.index(input_month)
          df = df[df['month'] == input_month_number]
    if input_day != 'all':
          df = df[df['day_of_week'] == input_day]
    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print('The most common month is {}'.format(most_common_month))
    
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day is {}'.format(most_common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour of travel is {}'.format(most_common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station of travel is {}'.format(most_common_start_station))
    
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station of travel is {}'.format(most_common_end_station))
    
    # TO DO: display most frequent combination of start station and end station trip
    most_common_station = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    print('The most fequent combination of station is {}'.format(most_common_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total trip duration is {}'.format(total_travel_time))
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean trip duration is {}'.format(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print(user_type_counts)
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    # Since it has NaN, filling NaN with 0
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
        earliest_birth_year = birth_year.min()
        print('The earliest birth year is {}'.format(earliest_birth_year))
    
        most_recent_birth_year = birth_year.max()
        print('The recent birth year is {}'.format(most_recent_birth_year))
    
        most_common_birth_year = birth_year.mode()[0]
        print('The most common birth year is {}'.format(most_common_birth_year))
    
        remove_nan_year = birth_year.fillna(0)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
