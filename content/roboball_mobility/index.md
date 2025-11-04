---
title: "Roboball Mobility Studies"
date: 2024-05-04T09:49:01-06:00
draft: true
description: ""
summary: "Case Studies of RoboBall on Water and Slopes"
---


# Mobility Studies
While RoboBall was originally designed to head into craters, its unique form factor lends it to mobility in other situations. 

### RoboBall on Slopes
RoboBall has a limited ability to climb slopes. By designing the center of mass of the system to be as close to the edge of the robot as possible the maximum slope climbing angle can be increased. So we swapped out the bottom ballast plate for a heaver version made of copper to improve our climbing ability.
![](gallery/ballast%20cmparison.png)

<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/ramp_test_drive_stand_converted.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

My labmate Rishi took these test results to showcase the improved slope climbing ability of the 6ft diameter RoboBall: [paper link](https://ieeexplore.ieee.org/abstract/document/11068434)

### RoboBall in Water
Since the robot is inflatable it can navigate from ground to water without any additional modifications. 

<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/ball_in_water.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

However at certain speeds it produces a "rooster tail" effect that negatively impacts its forward thrust in water. We tested this by comparing drive motor encoder data with forward speeds measured from videos. The figure below shows snapshots from various tests at increasing speeds and rooster tails. Notice that the fastest speed with the greatest rooster tail has a reduction in forward velocity. Primarily due to a *rocket equation* effect where we are throwing mass in the wrong direction.  

![](gallery/rooster_tail_diagram.png)
