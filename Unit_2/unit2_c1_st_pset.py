'''
Given two lists of strings, artists and set_times, both of length n,
write a function lineup() that maps each artist to their set time.

An artist artists[i] has set time set_times[i].
Assume 0 <= i < n and len(artists) == len(set_times).

Input: Two lists of strings, artists and set_times
Output: Combined output that matches artists to set_times
Strat: Use a dictionary for the result and employ zip function
'''
def lineup(artists, set_times):
    result = {}
    if not artists or not set_times :
        return result
    
    for artist, time in zip(artists, set_times):
        result[artist] = time

    return result # Works

'''
Problem 2: Planning App
You are designing an app for your festival to help attendees have the best experience possible!
As part of the application, users will be able to easily search their favorite artist and find out the day,
time, and stage the artist is playing at.
Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping
artist's names to dictionaries containing the day, time, and stage they are playing on.
Return the dictionary containing the information about the given artist.

If the artist searched for does not exist in festival_schedule,
return the dictionary {"message": "Artist not found"}.

Input: an artist and a dictionary of artists with artist, schedule pair
Output: the schedule of the passed artist/key
Strat: search for the artist using the key, if not found, return a msg
'''

def get_artist_info(artist, festival_schedule):
    not_found_dict = {"message": "Artist not found"}
    return festival_schedule.get(artist, not_found_dict) # Works

'''
Problem 3: Ticket Sales
A dictionary ticket_sales is used to map ticket type to number of tickets sold. 
Return the total number of tickets of all types sold.
'''

def total_sales(ticket_sales):
    total = 0
    return sum(ticket_sales.values()) # Works

'''
Problem 4: Scheduling Conflict

Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues.
Some artists will perform both venues, while others will perform at just one.
To ensure that there are no scheduling conflicts, implement a function identify_conflicts()
that accepts two dictionaries venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times.
Return a dictionary containing the key-value pairs that are the same in each schedule.

Input: Two dictionaries with key, value pairs
Output: Intersection of these two dictionaries
Strat: Use & to create tuples and return the dictionary of it
'''

def identify_conflicts(venue1_schedule, venue2_schedule):
    result = venue1_schedule.items() & venue2_schedule.items()
    return dict(result) # Works

'''
Problem 5: Best Set

As part of the festival, attendees cast votes for their favorite set.
Given a dictionary votes that maps attendees id numbers to the artist they voted for,
return the artist that had the most number of votes.
If there is a tie, return any artist with the top number of votes.
'''

def best_set(votes):
    pass