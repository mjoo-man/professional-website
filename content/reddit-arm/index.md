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
In my last semester of undergrad, I enrolled in **MEEN 408/612: Robotic Manipulators** with Dr. Dharba. It was a challenging but fascinating course, and a big reason why I decided to pursue robotics as a career.  

Part of the class focused on different control strategies for manipulator arms. Since there were no lab sessions, I wanted to take what I learned and apply it to real hardware.

## Open Source Robot Arm
The most cost-effective way to get an arm was to build one myself. I found a small group called [Annin Robotics](https://www.anninrobotics.com/) that sold pre-designed kits. These kits included machined parts and a bill of materials for sourcing the rest from Amazon or McMaster-Carr.

# Design Lessons
The parts arrived, and I started assembly around the same time we were designing the **RoboBall** pendulum. As you can imagine, working with Dr. Ambrose on a custom robot is *wildly* different from assembling a cheap kit. Here are a few lessons I learned while building this arm alongside RoboBall:  

- **Standardize your fasteners** – This kit used multiple bolt heads, set screws, and thread types. Keeping track of them was a pain compared to RoboBall, which only used 4-40s and 10-32s.  
- **Use standard components wherever possible** – For some reason, all the screws were metric, which made it harder to find spares locally.  
- **Working in an apartment is very limiting** – Building an arm requires a surprising amount of space and tools. My bedroom couldn’t function as both a workshop and a place to sleep.  
- **Design with maintenance in mind** – The kit called for many components to be soldered directly together. Adding connectors might have increased bulk but would’ve saved a lot of headaches during repairs.  
- **Keep software modular and familiar** – The included control software used a custom serial protocol, with all the low-level logic lumped into one massive `for` loop. It was nearly impossible to read or debug.  

![Low Budget Apartment Build](gallery/arm_cableing2.jpg "Cramped workspace in my apartment")

# Calibration Video
I eventually finished assembling the arm according to the kit instructions, but didn’t have time to go further as the RoboBall project was ramping up.  

<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/arm-calibration.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

# Update — October 2025
I’ve since finished grad school and learned a lot more about robot programming. Once I’m settled into a new job, I plan to rewrite the control software in **ROS 2** and possibly implement some controllers using the **pydrake** library.
