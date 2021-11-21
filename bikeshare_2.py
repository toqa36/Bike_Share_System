import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago','new york city','washington']
months = ['all','january', 'february', 'march', 'april', 'may', 'june']
days = ['all','saturday', 'sunday', 'monday', 'tuesday', 'widnesday', 'thursday', 'friday']


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
    while True :
        print('Which City Do You Want \n 1- Chicago \n 2- New york city \n 3- Washington \n')
        city = input().lower()
        if city in cities:
            break
            
        else:
            print("Not Valid Input ")
            
            
       
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        print('which month do you want [all, january, february, march, april, may, june]')
        month = input().lower()
        if month in months:
            break
        else:
            print("Not Valid Input ")
    
   


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        print('which day do you want [all, saturday, sunday, monday, tuesday, widnesday, thursday, friday] ')
        day = input().lower()
        if day in days:
            break
            
        else:
            print("Not Valid Input ")
   


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
 
    df = pd.read_csv(CITY_DATA[city])


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
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
    common_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('Common month is --> ' ,months[common_month-1])


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Common day is --> ', common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Common start hour is --> ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Common start station is --> ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Common end station is --> ', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = df[['Start Station','End Station']].mode().loc[0]
    print('Common start to end station is --> ', common_start_end[0],' To ',common_start_end[1])
    print()
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('Total Travel Time --> ',total)


    # TO DO: display mean travel time
    avrage = df['Trip Duration'].mean()
    print('Avrage Travel Time --> ',avrage)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Type of Users\n',user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts() 
        print('Gender\n',gender)
    else:
        print('There IS No Gender Column In Washington DataSet')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest Birth Year --> ',earliest_birth_year)
        
        recent_birth_year = df['Birth Year'].max()
        print('Recent Birth Year --> ',recent_birth_year)
        
        common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year --> ',common_birth_year)
    else:
        print('There Is No Birth Year Column In Washington DataSet')
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    answers = ['yes','no']
    counter=1
    rows=0
    while True :
        print('Do You want to see 5 rows of data ( yes/no )')
        answer = input().lower()
        if answer in answers:
            if answer == 'yes':
                print(df.iloc[rows:rows+5])
                rows+=5
            else:
                break  
            
        else:
            print("Not Valid Input ")
            
  
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
