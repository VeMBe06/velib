# Notes on the visuals:

So far there are only weird plots that I think are interesting as a concept, but not necessarily for
what I want to output for my project.


### map.html
Just a test run, I don't have what I want yet. But it's still an encouraging result
### scatterplot_time_delta.png
This plot was very interesting to me (hence why I saved it) because it shows how the Vélib API might work:
- according to the documentation, the API "updates" its data every minute, however it actually has to wait for velib
stations to send data
- as long as there is no movement in the station, a velib station will not send any update to the API
- therefore, if a station is not used for a long time, the API keeps the old information until an update is sent to it
- The 'trails' graph show the velib stations that had no bike returned or rented with their information "getting old"
live as time passes
