import time
import pandas as pd

import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
day_data = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

month_data = ['january', 'february', 'march', 'april', 'may','june', 'all']





def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input('Enter the cityname, Please Choose between Chicago, New York City, or Washington: ').lower()
    while city not in CITY_DATA.keys():
        print('Oops! it appears that you have entered a wrong city. Please Choose between Chicago, New York City, or Washington')
        city = input('Enter the name of the city: ').lower()

    # get user input for month (all, january, february, ... , june)

    month = input('Enter the month name or all if no filter ').lower()
    while month not in month_data:
        print('Oops! it appears that you have entered a wrong month')
        month = input('Enter the name of the month (type \'all\' for no filter): ').lower()


    # get user input for day  (all, monday, tuesday, ... sunday)

    day = input('Are you looking for a specific day? \n  please enter the following days: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday, or put all if you have no preference.\n  ').lower()
    while day not in day_data:
        print('Oops! it appears that you have entered a wrong day, please choose again')
        day = input('Are you looking for a specific day? \n if yes enter the following days: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday, or put all if you have no preference.\n ').lower()

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

    #Get the data frame file

    df = pd.read_csv(CITY_DATA[city])

    #Start and End Times convert to datatime.
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #get month /  day / hour from Start Time
    df['hour'] = df['Start Time'].dt.hour
    df['day'] = df['Start Time'].dt.day
    df['month'] = df['Start Time'].dt.month
    
    

    # use filter month, where relevant
    if month != 'all':
        
        # Use the month list index to obtain the appropriate value
        
        month = month_data.index(month) + 1

        # Filter by month to get new dataframe
        df = df[df['month'] == month]

    # use filter by  day, where relevant
    if day != 'all':
        # Use the day list index to obtain the appropriate value
        day = day_data.index(day)
        # Filter by day to get new dataframe
        df = df[df['day'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculate  Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month is: {}'.format(popular_month))
    # display the most common day of week
    popular_day = df['day'].mode()[0]
    print('Most Popular Start Day is: {}'.format(popular_day))

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour is: {}'.format(popular_hour))




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculate Most Popular Stations and Trip...\n')
    start_time = time.time()
 
    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station is: {}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station is:'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    freq_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent combination is: {} AND {}'.format(freq_combination[0], freq_combination[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculate Trip Duration...\n')
    start_time = time.time()
 
    # display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('Total trip duration is: ', total_trip_duration)
    # display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print('Average trip duration is: ', mean_trip_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculate Users statistics...\n')
    start_time = time.time()


    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(' number of user types   : {}'.format(user_types))
    
# Display counts of gender
    if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('\nNumber of male users are {}\n'.format(int(male_count)))
        print('\nNumber of female users are {}\n'.format(int(female_count)))


    
 # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_YOB = df['Birth Year'].min()
        print('The earliest year of birth is: {}'.format(earliest_YOB))
        recent_YOB = df['Birth Year'].max()
        print('The most recent year of birth is: {}'.format(recent_YOB))
        common_YOB = df['Birth Year'].mode()[0]
        print('The most common year of birth is: {}'.format(common_YOB))
    



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    view_data = input('\nWould you like to vıew the fıve rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data) == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Would you like to continue with the next 5 rows ? Enter yes or no\n'").lower()
        continue 
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')

 
 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)         

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
