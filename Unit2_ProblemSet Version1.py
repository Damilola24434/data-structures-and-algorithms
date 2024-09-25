#### Unit two section one question 1
'''
Given two lists of strings artists and set_times of length n, 
write a function lineup() that maps each artist to their set time.
An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and 
len(artists) == len(set_times).

def lineup(artists, set_times):
'''
'''
def lineup(artists, set_times):
    return dict(zip(artists,set_times))
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
'''
#### Unit two section one question 2...
'''
You are designing an app for your festival to help attendees 
have the best experience possible! As part of the application,
users will be able to easily search their favorite artist and 
find out the day, time, and stage the artist is playing at. 
Write a function get_artist_info() that accepts a string artist
and a dictionary festival_schedule mapping artist's names to 
dictionaries containing the day, time, and stage they are playing
on. Return the dictionary containing the information about the 
given artist.If the artist searched for does not exist in
 festival_schedule, return the dictionary {"message": "Artist not found"}.
'''
'''
def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        c
    else:
        return {"message": "Artist not found"}
festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule)) 
'''
#### Unit two section one question 3
'''

def total_sales(ticket_sales):
    return sum(ticket_sales.values())
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))
'''
#### Unit two section one question 4
'''
def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = {}
    
    for artist, time in venue1_schedule.items():
        if artist in venue2_schedule:
            if time == venue2_schedule[artist]:
                conflicts[artist] = time
    
    return conflicts

# Example usage:
venue1_schedule = {
    "Blood Orange": "9:00 PM",
    "Metallica": "8:00 PM",
    "Kali Uchis": "7:00 PM"
}

venue2_schedule = {
    "Metallica": "8:00 PM",
    "Kali Uchis": "6:00 PM",
    "Lawrence": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
'''
#### Unit two section one question 5
'''
def max_audience_performances(audiences):
    # Step 1: Find the maximum audience size
    max_audience = max(audiences)
    
    # Step 2: Sum the audience sizes of performances with the maximum size
    total_max_audience = sum(audience for audience in audiences if audience == max_audience)
    
    return total_max_audience

# Example Usage
audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))  # Output: 250
print(max_audience_performances(audiences2))  # Output: 440
'''