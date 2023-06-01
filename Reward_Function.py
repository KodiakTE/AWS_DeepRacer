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
        timeReward = (60000/steps)*(speed/maxSpeed)
    
    
    #Make Reward function
    totalReward = timeReward + centerReward + progressReward
    return float( totalReward )
