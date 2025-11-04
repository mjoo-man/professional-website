---
title: "Roboball Modeling"
date: 2025-06-04T09:57:14-06:00
draft: false
description: ""
summary: "A description on how to model RoboBall in pyDrake"
---


{{< katex >}}
# Dynamic Modeling and Control
There are two polular approaches to modeling a pendulum driven sphere. One way is to assume that the sphere is assumed to be modelled by two rolling cylinders in the drive and steering direction. This is a popular approach for similar prototypes and fits well with LQR style control. An early version of this model an controller is published in [this paper](https://ieeexplore.ieee.org/abstract/document/10610555) and controller with shell compensation in [this paper](https://ieeexplore.ieee.org/abstract/document/10833720).

![](gallery/drive%20Steer%20as%20cylinders.png "A diagram representing the drive and steer directions of the ball as cylinders")

While the cylinder approach is simpler for control design, often additional terms need to be added to account for the coupling between the drive and steering directions. Studies focused on this design derive the full dynamics of a sphere rolling on a plane with a contact jacobian.

![](gallery/roboball_rolling_kinematics.png "Simplified rendering of a ball rolling in space")

In the figure above `r0` is the stationary inertial frame and `r1` is attached to the rolling sphere itself. You can then define a point `P1` as the center of the sphere that is the origin of `r1`. Expressed in the spheres frame this point is represented by:

$$ {}^{r1}P1 = [0,0,0,1]$$

From this point you can travel a distance `R` down to the point of contact of the sphere on a plane. This vector is simply expressed in the inertial world frame as below:

$$ {}^{r0}v2 = [0,0,-R, 0] $$

To get the constraints, reflect `P1` and `v2` into a common frame using a transform ( ${}^{r0}T_{r1}$ ) and subtract them to obtain the point of contact location (`P2`) expressed in the world frame:

$$ {}^{r0}P2 = {}^{r0}T_{r1} {}^{r1}P1 - {}^{r0}v2$$

Differentiating `P2` with respect to time and reorganizing into a Praffian form ( $A\dot{q}$ ) yeilds the contact jacobian for a sphere rolling on a plane.

This in conjunction with a dynamics algorithm of your choice can yeild the full dynamics of a sphere rolling on a plane as:

$$ M(q)\ddot{q} + H(q, \dot{q}) = A^T\dot{q} + \tau $$

This is (probably) the most common way to obtain the dynamics of a system, and various flavors of this method can be found in literature. However, there are a number of inconvienences in this approach that can get annoying. 

1. $ {}^{r0}T_{r1} $ is usually defined with a set of euler angles and thus at risk of a singularity. A rolling sphere is allowed to roll through the singularity, so care needs to be taken when trying to model that motion. This could be fixed by adding a quaternioin representation. However that would add an extra degree of freedom and the headache of converting a body velocity representation from a 3-dof space to a 4-dof space.
2. As the number of degrees of freedom of a system increase, finding the dynamics becomes a bookeeping excersice. Either by hand or symbolically, this is the primary problem Roy Featherstone tried to address in his book [Rigid Body Dynamics Algorithms](https://link.springer.com/book/10.1007/978-1-4899-7560-7)

My favorite quote from the books preface:
```
Rigid-body dynamics has a tendency to become a sea of algebra - R. Featherstone
```

As a result of Featherstones work a variety of robotics simulators have spring up in the last decade. Most of which cite his work as the source of their algorithms. 

I leveraged the tools in that work to find an easier way to study RoboBalls dynamics. The implementation I found the most useful and easiast to get started was [Drake](https://drake.mit.edu/). Which also happens to include a soft body contact model.

My work extending the ball into this area and notes on how to tune the soft body model for the ball was published in this [RA-L paper](https://ieeexplore.ieee.org/abstract/document/11197665).

As an added bonus, drake displays results in a 3D urdf render instead of individual graphs of the states. It makes interpreting the results of dynamics studies more intuitive and fun. 

## Screenrecord of URDF in Drake (with the soft-body model)
<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/urdf_render.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Rolling Asteroid Dynamics