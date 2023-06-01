AWS DeepRacer – reward_function()
-------------

The code presented here is a **reward function()** for the [AWS DeepRacer](https://aws.amazon.com/deepracer/) vehicle training tasks (Reinforcement Machine Learning). This is an outcome of participating in a one-day AI competition.
 
I've seen a lot of trained models intentionally go outside the race track in order to get faster times since the penalty for getting outside of the race track is minimal. I wanted to do something different by  creating a model that doesn't fall off the track while trying to go as fast as possible. This involves splitting the reward into 3 portions: Distance from Center, Progress, and Time.

### Distance from center
This is code given from an example from AWS. This code works by giving the vehicle a reward for staying closer to the center of the track. If the vehicle falls off at any point, then a very small reward will be given to the car. I've just modified the variable names just so it aligns with my goals to split the reward into 3 portions.
```python

 # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        centerReward = 100
    elif distance_from_center <= marker_2:
        centerReward = 50
    elif distance_from_center <= marker_3:
        centerReward = 10
    else:
        centerReward = MinPartialReward  # likely crashed/ close to off track
```
### Progress
I wanted there to be a reward for the vehicle to complete the track. If the vehicle does complete the track, then a 100 point reward is given. 
```python
    completedTrack = False
    if progress >= 99:
        completedTrack = True
    progressReward = progress
```
When the vehicle completes the track, the vehicle has access to gain more rewards for completing the track faster shown below.

### Time
In the function, I wanted the vehicle to be rewarded for going faster. This is done here:
```python
    timeReward = 0
    if completedTrack == True:
        timeReward = 1000*(speed/maxSpeed)
```
`completedTrack == True` ensures that the vehicle will only get this big boost in reward when it completes the track is completed.

`1000*(speed/maxSpeed)` basically means that the closer the car is to the max speed, the more reward it will get. The max reward being 1000.

### Adding it all up
Now that all the portions have been completed, all you need to do is add up the rewards.
```python
    totalReward = timeReward + centerReward + progressReward
    return float( totalReward )
```


## My Full Reward Function:
```python
def reward_function(params):    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    steps = params['steps']
    speed = params['speed']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    #initilize variables
    MaxPartialReward = 1e5
    MinPartialReward = 1e-5
    totalReward = 0
    maxSpeed = 1
     
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        centerReward = 100
    elif distance_from_center <= marker_2:
        centerReward = 50
    elif distance_from_center <= marker_3:
        centerReward = 10
    else:
        centerReward = MinPartialReward  # likely crashed/ close to off track

    #Reward for making progress
    completedTrack = False
    if progress >= 99:
        completedTrack = True
    progressReward = progress
    
    
    #reward for fast time
    timeReward = 0
    if completedTrack == True:
        timeReward = 1000*(speed/maxSpeed)
    
    
    #Make Reward function
    totalReward = timeReward + centerReward + progressReward
    return float( totalReward )

```
