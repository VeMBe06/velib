# Personnal Project: Analysis of traffic on Paris's Rental bike system

Hey there!

If you're reading this, this is a personal project I'm currently working on. I am a frequent user of Paris's rental bike system, called "Velib", and it always seems like the bikes are never there when I need them, which brought me to the question: Where are the f*cking bikes gone??

From that came the idea of finding out by myself the answer ot that question by analyzing the patterns of the bikes' localization over an entire week.


# Dev log
## Currently working on:

- Exploring dataviz libraries to find which one will be best for my use case (currently
hesitating between Folium and Plotly)
- Testing whether I can reproduce the information there is on the Velib map, with station information etc

## Past Logs:

- Performed Data Cleaning, trying to minimize data loss in the process. A big part of it was to understand how the Velib API worked
in order to decide exactly what was "dirty". In the end I got a pretty good idea of how the API worked and was able to remove the
data that was unusable (at least for the use I have of it)
- Added a new folder for interesting visuals that might pop up during the preparation of the project
- Planned what type of insight I want to extract from the data: I'm focusing on impactful visuals
- Exploratory Data Analysis of the Velib dataset I created
- Turns out the first dataset I created has a major flaw: some of the timestamps didn't update from one API call to the next, which is problematic. This happened to about more than 60% of the
API calls, which is huge. I suspect that the API provided by Velib doesn't actually update the station status timestamps every minute if no bikes were taken in/out of the station.
I modified my dataset making script and relaunched my VM for a new week of data collection to get a fresh dataset
- Downloaded the final csv file from my VM and shut everything down to optimize cost
- The virtual machine is done collecting data, after 700+ API calls I have a (supposedly) working dataset
- Set up a virtual machine on Google Cloud Platform to collect velib data 24/7 for a week
- Found a way to trigger the data collection process at regular time intervals
- Set up a script to create a dataset out of Smovengo's public API
