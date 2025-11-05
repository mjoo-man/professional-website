---
title: "Meen 612 Sim Project"
date: 2025-03-04T13:39:04-06:00
draft: true
description: ""
summary: "An assignment I designed for students taking MEEN 408/612 Mechanics of Manipulators"
---

# Motivation
MEEN 612: Mechanics of Manipulators is taught in the spring semester. Since I was looking into pydrake for use with RoboBall, Dr. Gray Thomas, the professor for the class, asked me to put together a boilerplate assignmnet for the students to practice some concepts they were learning in class. 

Since learning pydrake and CLI was outside of the scope of the class I setup the urdf, simulation environment and separate blank slate for the students to develop their code. 

Here is a [link to the repository](https://github.com/mjoo-man/ur5e-in-pydrake)

# Environment
Orignally the students downloaded a VM loaded with ubuntu and used a local python virtual environment for packages. This was difficult to set up on all their machines. 

### Future note:
Since drake runs natively Macs and WSL2 support in Windows 11 is excellent, I would recommend the individual students use either of those options instead of the VM.

# Code Structure
The code is structured into two main python files `run_simulator.py` and `my_controller.py`. The rough structure of data within the systems is charted in the figure below. 

![](gallery/drake_ball_sim.png)

The urdf is loaded into a drake specific `MultibodyPlant` which initializes the a rigid body class of the arm. A separate instance of the urdf is then loaded into a drake `LeafSystem` block and wired into the arm. Using another instance of the plant allows for use of the `local_plant.calcMassMatrix()` API to save the students the trouble of computing the lagrangian of the 6-dof arm by hand. The controller urdf can also be swapped for one of a different arm to highlight the difference in modelled versus actual dynamics. 

{{< katex >}}
# The task
The students were given the following controller:

$$ \tau_{control} = 0.1 [1_{1\times n}] \sin(t) - V(q) $$

where
 - $V(q) = $ output of `plant.CalcGravityTorques()`
 - $[1_{1\times n}] = $ a vector of ones the for the number of joints $n$ 

This results in an behavior of an arm that can support itself against gravity, but has additional movement caused by the sinusoidal disturbance in the control law. Since the torques are the same at each joint, the smaller distal joints have a more erratic response. 

The effects of this controller are shown below. 

<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/drake-ur5-sim-trimmed.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

The students were tasked with developing a point tracking computed torque controller based on their class notes. 

<!-- TODO: (mjoo) Since this repo post is public and students are very good at googling, I will not give the correct control law here. However it should look something like this.

<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/point-to-point.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video> -->

**NOTE:**
This is a personal copy of an earlier version of the project before I handed it off to Gray Thomas and Jonas Land to finish setting up the realtime portions for the class. 

The final version of the project is public [here.](https://github.com/tamu-edu/meen-612-ur5e-sim-project)
