# Volcano Rover Dashboard
A dashboard to show the volcano rover's position and enter waypoints.

## Documentation
This document details how to connect a computer to the rover and how to run certain applications related to the rover. It assumes you already have access to the python webapp, have already installed mission planner/ardupilot, changed your ethernet ip to 192.168.1.18 and that you have the MikroTik antenna already. Credit to Will, a previous intern for this project, for setting up the ROS and providing the information on how to connect the computer and mission planner to the rover

### Connecting to the rover over terminal1.

1. Start by opening up your terminal of choice and ‘ssh’ing into the rover by typing 
    ```
    ssh pi@192.168.1.21
    ```
    to connect through the MikroTik or
    ```
    ssh pi@navioto
    ```
    connect through the wifi (assuming the wifi is set on both sides
    
2. Type the password set
3. Then to connect to ROS, simply type 
    ```
    roscore
    ```
    into the terminal. `Note`: you may want to have multiple instances of the rovers terminal open, tmux is recommended for this, click [here](https://tmuxcheatsheet.com/) for a cheat sheet
4. You can now access ros and the rest of the rover libraries 

Connecting the rover to the python webapp or mission planner

1. It is assumed that you have already connected to the rover from the terminal, if not please go over those steps first in a separate instance of the rovers terminal
2. Start ardupilot inside the rover by typing 
    ```
    sudo systemctl start ardupilot
    ```
3. Then start mavros and the udp connection to mission planner by typing
    ```
    rosrun mavros mavros_node _fcu_url:=udp://:14650@_gcs_url:=udp://:14551@192.168.1.19:14550
    ```
4. Mission Planner/Ardupilot:
    * Open mission planner/ardupilot on your computer and connect via udp. `Note`: that if this doesn’t work you may need to rerun step 3
    
    Python Webapp:
    * Run the python webapp (Feel free to change the script to your needs)
5. You should now have access to the python web app or mission planner. `Note`: you can connect both the webapp and mission planner at the same time 

Switching to manual/guided modeManual mode:
1. To manually control the rover you must have connected the rover to mission planner first, if you haven’t follow the steps above
2. Go into a separate instance of the rover terminal and type
3. Then connect your controller to mission planner by clicking joystick, you can also change the controls at the same time
4. Then click arm and move the rover

Guided mode:
1. To move rover to a set location starting ardupilot and mavros
    ```
    sudo systemctl start ardupilot
    rosrun mavros mavros_node _fcu_url:=udp://:14650@_gcs_url:=udp://:14551@192.168.1.19:14550
    ```
2. Then set the rover to guided mode by typing
    ```
    rosservice call /mavros/set_mode "custom_mode: 'GUIDED'"
    ```
3. Move the rover to the set coordinates

Finally you can check what mode the rover is in by typing 
```
rostopic echo /mavros/state
```
Learn more about the swapping mode by heading to
https://masoudir.github.io/mavros_tutorial/Chapter1_ArduRover_with_CLI/Step1_How_to_change
_mode/

Final comments: There were plans to have the python webapp to control the rover using the python library paramiko however this did not end up being finished and so remnants of these plans may be
in the python script.