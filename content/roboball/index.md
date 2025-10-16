+++
date = '2025-09-26'
title = 'Graduate Project: RoboBall II'

showReadingtime = false
showWordCount = false
showDate = true
noindex = true
summary = "A high level overview of my work on the RoboBall Robot"

draft = false
+++

{{< icon "triangle-exclamation" >}} _"If I had more time I'd have written a shorter letter"_ - Mark Twain (or Blaise Pascal). Eventually (Very soon!) this page will be a condensed version of my dissertation with more videos. Until then, here is a preprint of the [longer letter](/files/Oevermann_Dissertation_Compressed.pdf)

# Motivation
This article will touch on some key components of my time on the project and direct the reader to the relevant research article or chapter of my dissertation.

# Mechanical Design of RoboBall
RoboBall consists of two main mechanical parts:
1. Inner Mechanical Pendulum
2. Soft Pnuematic Outer Shell

## Design of Inner Pendulum
 - Mechanical Design
 - Instrumentation
 - Inner Pneumatic Circuit -> [paper link](https://ieeexplore.ieee.org/abstract/document/11078128)

## Design of Soft Outer Shell
 - Ring Interface and Hubcap
 - Outer Shell Prototypes -> [paper link](https://arc.aiaa.org/doi/abs/10.2514/6.2024-1961)

### Video: Shell Manufacturing
<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/mold_spray.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Video: Assembly Timelapse

<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/assembly-timelapse.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Electrical Components
- First Gen FRC components
- wiring tricks

# Dynamic Modeling and Control
Basic Dynamic Modeling of the system -> [paperlink](https://ieeexplore.ieee.org/abstract/document/10610555)

# Mobility Studies
What limits the system? [Diss. chapter 4]
- Water 
- Slope Climbing -> [paper link](https://ieeexplore.ieee.org/abstract/document/11068434)

### Video: RoboBall in Water
<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/ball_in_water.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

# Advanced Topics
- Modeling in Drake -> [RA-L Paper Link](https://ieeexplore.ieee.org/abstract/document/11197665)

### Video: Screenrecord of URDF in Drake
<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/urdf_render.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

- Rolling Asteroid Dynamics [ICRA 2026]