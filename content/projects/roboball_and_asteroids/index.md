---
title: "Asteroid Dynamics and Rolling Robots"
date: 2025-11-04T10:03:29-06:00
draft: true
description: ""

weight: 4
tags: ["RoboBall", "Dynamics", "ICRA 2026"]
---

{{< katex >}}
# The Problem

Tests with RoboBall often ended with the system wobbling until it eventually started flipping end over end. Tests with more robust control systems only pushed this mode of instability to occur at higher speeds but would not remove it. This paper shows that the answer lies in a classic phenomenon from spacecraft dynamics that has gone largely unnoticed in ground robotics.

# The Core Idea
High-speed spherical robots often develop a growing wobble that can escalate into end-over-end flipping. The paper shows that this behavior is not a control bug or modeling artifact, but a fundamental dynamic effect caused by the robot’s inertia interacting with rolling constraints.
Specifically, rolling spherical robots with oblate inertial profiles experience a relaxation effect closely related to the Intermediate Axis Theorem (also known as the tennis-racket or Dzhanibekov effect). Under dissipation, rotating bodies naturally reorient their angular momentum toward their major inertial axis. For rolling robots, this manifests as a gradual shift from stable forward rolling into unstable “hubcap-to-hubcap” motion.


<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/ICRA_Final_clips/nutation_instability.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


Relaxation dynamics are well understood in tumbling asteroids but have **never been systematically applied to rolling systems with contact constraints**.

# This paper:
- Extends classical relaxation theory to spherical robots rolling on the ground
- Shows that rolling constraints couple rotational and translational energy, creating an effective dissipation mechanism
- Backs up the claim by conducting experiments on solid ground and water to chance the contact dynamics. 


# Key Findings
- Free oblate bodies are stable, but once rolling constraints are introduced, stability changes fundamentally.
- Translational rolling acts like structural dissipation in asteroids, driving momentum realignment.
- Experiments with an empty rolling shell, a constrained pendulum, and tests on land versus water confirm the theoretical predictions.
- Looser constraints (e.g., rolling in water with slip) dramatically reduce or eliminate the instability.


# Impact on Future Spherical Robot Design
Many spherical robot models assume uniform inertia, use decoupled planar dynamics, or ignore 3D rotational effects for simplicity. My results show that inertia shape and rolling constraints fundamentally limit high-speed stability, regardless of control quality.


Robot designers have two practical paths forward:

1. **Inertial design**
Configure the shell so rolling occurs about the major inertia axis, which naturally stabilizes motion.


2. **Control Design**
Incorperating the  relaxation angle with an appropriate internal actuation method could make the system aware of the effect and actively cancel it. 
Note that the control effort is proportional to speed so flywheels may be a better option than RoboBall's torque constrained pendulum.


# Big Picture
This work bridges satellite attitude dynamics and ground robotics, offering a compact framework to understand inertial effects in spherical robot performance
and guide both mechanical design and control strategies for future robots.


> This paper was recently accepted for presentation at ICRA 2026. This link is for a preprint, the final version will be available shortly.

<embed src="ICRA_2026_Nutations_preprint.pdf" type="application/pdf" width="100%" height="600px" />

[Download the PDF](ICRA_2026_Nutations_preprint.pdf)
