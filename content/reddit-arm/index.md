+++
date = '2022-01-02'
title = 'Personal Project: Six DOF Stepper Arm'

showReadingtime = false
showWordCount = false
showDate = true
noindex = true
summary = "Built a 6 degree-of-freedom stepper driven arm, honestly not a great design"

draft = true
+++


# Motivation
In my last semester of undergrad I enrolled in MEEN 408/612: Robotic Manipulators with Dr. Dharba. It was a challenging but really cool class that is a large reason why I wanted to go into robotics as a career. 

Part of the class focuses on different control strategies for manipulator arms, and since there were no labs in the class I wanted to try and implement what I learned in class on hardware. 

## Open Source Robot Arm
I figured the most cost effective way to get a arm would be to build one myself. I found a small group called [Annin Robotics](https://www.anninrobotics.com/) that sold predesigned kits. These kits consisted of machined parts and a Bill of Materials to procure the rest of the parts from Amazon or McMaster. 

# Design Lessons
The parts came in and I started assembly around the same time we were designing the RoboBall pendulum. As you can imagine, working with Dr. Ambrose to design a robot is wildy different from a cheap kit. I'll summarize some of the big lessons I learn from building this arm alongside RoboBall below. 

- **Make a choice to only use a few bolt types** - This robot had multiple types of bolt heads,set screws, and trhead types. These were a pain to keep up with compared to RoboBall (which only used 4-40s and 10-32s)  
- **Use standard components wherever possible** - For some reason all the  screws were metric, so sourcing spares was harder than simply going to Ace hardware.
- **Working in an apartment room is very restrictive** - Arms take alot of supporting tools, my bedroom cannot serve as both a workshop and a place of rest
- **Design with maintenance in mind** - the kit called for alot of components to be soldered directly together. Adding electrical connectors would increase bulk but lower headaces when something broke
- **Software should be modular and include as little new material as possible** - The software suite this arm shipped with relied on a bespoke serial protocall. All low level logic was in one massive for loop, so it was impossible to understand or even debug. 

![Low Budget Apartment Build](gallery/arm_cableing2.jpg "Cramped workspace in my apartment")

# Calibration Video
I eventually finished the arm accroding to the kit instructions, but did not have the time to go further as the RoboBall project was picking up. 


<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/arm-calibration.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

# Update on October 2025
I've finished grad school and learned alot more about how to program a robot. Once I get resettled in a new job I'll try to rewrite the code for ROS2 and potential to implement some of the controllers in the pydrake library. 