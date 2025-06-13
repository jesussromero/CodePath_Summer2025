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

