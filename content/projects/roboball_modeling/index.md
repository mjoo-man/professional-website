---
title: "Roboball Modeling"
date: 2025-06-04T09:57:14-06:00
draft: false
description: ""
summary: "A description on how to model RoboBall in pyDrake"

weight: 5
tags: ["RoboBall", "pyDrake", "Dynamics", "Control"]
---


{{< katex >}}
# Dynamic Modeling and Control
There are two popular approaches to modeling a pendulum-driven sphere. One approach is to approximate the sphere as two rolling cylinders, one for the drive direction and one for steering. This method is commonly used for similar prototypes and works well with LQR-style control. An early version of this model and controller was published in [this paper](https://ieeexplore.ieee.org/abstract/document/10610555), with an improved controller using shell compensation described in [this paper](https://ieeexplore.ieee.org/abstract/document/10833720).


![](gallery/drive%20Steer%20as%20cylinders.png "A diagram representing the drive and steer directions of the ball as cylinders")

While the cylindrical approach simplifies control design, additional terms are often required to account for coupling between the drive and steering directions. More complete studies derive the full dynamics of a sphere rolling on a plane using a contact Jacobian formulation.

## Typical Derivation of Contact Jacobian
![](gallery/roboball_rolling_kinematics.png "Simplified rendering of a ball rolling in space")


In the figure above, `r0` denotes the stationary inertial frame and `r1` is attached to the rolling sphere. Define point `P1` as the center of the sphere, the origin of `r1`. Expressed in the sphere’s frame, this point is represented as:

$$ {}^{r1}P1 = [0, 0, 0, 1] $$

From this point, move a distance `R` down to the point of contact between the sphere and the plane. This vector, expressed in the inertial world frame, is:

$$ {}^{r0}v2 = [0, 0, -R, 0] $$

To obtain the contact constraints, transform `P1` and `v2` into a common frame using the transform ${}^{r0}T_{r1}$, then subtract them to find the contact point location `P2` expressed in the world frame:

$$ {}^{r0}P2 = {}^{r0}T_{r1} {}^{r1}P1 - {}^{r0}v2 $$

Differentiating `P2` with respect to time and reorganizing it into a Pfaffian form ($A\dot{q}$) yields the contact Jacobian for a sphere rolling on a plane.

Combined with a dynamics algorithm of your choice, the full dynamics of the rolling sphere as:

$$ M(q)\ddot{q} + H(q, \dot{q}) = A^T\dot{q} + \tau $$

This is perhaps the most common approach to obtaining the dynamics of a system, and many variations can be found in the literature. However, there are a few practical inconveniences worth noting:

1. ${}^{r0}T_{r1}$ is often defined using Euler angles, which are prone to singularities. A rolling sphere can pass through these singularities, so care must be taken to model such motion accurately. Using a quaternion representation can avoid this, but it introduces an extra degree of freedom and the challenge of converting body velocities between 3-DOF and 4-DOF spaces.  
2. As system complexity grows, deriving dynamics equations becomes a bookkeeping exercise, whether done by hand or symbolically. This challenge is one of the key issues addressed by Roy Featherstone in his book [*Rigid Body Dynamics Algorithms*](https://link.springer.com/book/10.1007/978-1-4899-7560-7).

My favorite quote from the book’s preface:
```
Rigid-body dynamics has a tendency to become a sea of algebra - R. Featherstone
```
Since RoboBall is a multi-student project I wanted to find more approachble ways to derive a dynamic model that could be passed from student to student. Using an implementation of featherstones algorithims in [Drake](https://drake.mit.edu/), a simple urdf can yeild a numerical full dynamics model, trading lagrangian derivation to a programing exercise.

My work extending the ball into this area and notes on how to tune the soft body model for the ball was published in this [RA-L paper](https://ieeexplore.ieee.org/abstract/document/11197665).

As an added bonus, drake displays results in a 3D urdf render instead of individual graphs of the states. It makes interpreting the results of dynamics studies more intuitive and fun. 

## Screenrecord of URDF in Drake (with the soft-body model)
<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/urdf_render.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
