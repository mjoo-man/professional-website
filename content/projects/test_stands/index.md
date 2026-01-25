---
title: "RoboBall Testing Stands"
date: 2026-01-24T17:17:43-06:00
draft: false
description: ""
weight: 2

tags: ["RoboBall", "Hardware Design"]

---
We finished RoboBall's pendulum within 9 months from its first
design review. However we would not finalize a design for the soft outer shell until ayear afterwards. To make headway on controls and software components before the soft shell was completed, a series of testbeds were built to mimic RoboBalls rolling dynamics. 

## 1st Gen: The Hanging Stand
This stand hung the pendulum between two static beams, shown in the video. The driveshaft
hex was rigidly clamped to disable relative motion between the pendulum and the ground. This stand was perfect for the initial operations tests and assembly, but its did not accurately model the reactive rolling dynamics.
<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/hanging_stand.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 2nd Gen: Gyro Stand
The next generation test stand used a set of flywheels to compensate for the lack of
inertia of the hanging stand. These flywheels would mimic the shell’s
reflected inertia to verify that the pendulum pitches upward with forward velocity.
However, the belts would slip after achieving final velocity and lose active flywheel braking. This
issue, in tandem with the safety risks of unsheathed flywheels, led us to scrap the stand after its
functional test.
<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/gyro_stand.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 3rd Gen: Steering Stand
The initial hanging concepts of testing stands did not capture the rolling coupling between the shell and ground. This steering stand isolated the pendulum’s continuous drive axis from the limited steering axis. Initial balancing tests with an LQR controller were promising. Still, the difference in inertias and contact dynamics between this stand and the shell prototypes made transitioning controllers from the testbed to the robot unrealistic.
<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/steering_stand.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 4th Gen: Drive Stand
The final stand was simply a set of wheels with hex adapters mounted to the outer ends of
the driveshaft. This stand proved the most useful, as it served the purpose of the hanging stand
to check alignments and calibrations. Simple rolling tests with the pendulum could be conducted
without assembling the shell. The stand even appears in early field tests, and is the only one still used by the RoboBall team today!
<video controls autoplay muted loop style="width:100%; border-radius:12px;">
  <source src="/videos/drive_stand.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>