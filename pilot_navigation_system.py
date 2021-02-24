#- you are a pilot
#- you are in the air
#- You are approaching an Airport
#-So there you need to land a plane
#- so there is a need of navigation system,
#- which can help the pilot understand, should I land the plane of make a GO Around

#- The casse with the pilot are
  #- if your altitude is more than 10k feet, just go around and then land

  #- if your altitude is 5k feet, drop the landing gears

  # - if your altitude is less than 3k, try landing plane with brakes

# - Pilot will input the Altitude in the system
 
# We need conditional statement,
# It is going to have 3 conditions.
# things we used in the program 
# 1.  IF ELIF ELSE
# 2. INPUT()


altitude = int(input("Hey Pilot, input your current altitude - "))
int(altitude)

if altitude >= 10000:
    print("Go around and land the plane after reducing the alt to 5k")
elif altitude >= 5000 and altitude <= 9999:
        print("Drop the Landing Gears")
elif altitude >= 3000 and altitude <5000:
         print("land using the brakes") 
else:
        print("n/a")
             
