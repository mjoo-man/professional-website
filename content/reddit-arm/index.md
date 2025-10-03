+++
date = '2021-10-12'
title = 'How not to build a robot arm'

showReadingtime = false
showWordCount = false
showDate = true
noindex = true

draft = true
+++

Possibly one of the biggest "learning experiences" I've had towards the end of my undergrad and start of grad school. I'm writing this as a reach the end of my phd so i'll include a little bit of hindsight. 

## Some Context
I was in my last semester of undergrad and enrolled in MEEN 408/612: Robotic Manipulators with Dr. Dharba. It was a challenging but really cool class that is a large reason why I wanted to go into robotics as a career. 

Part of the class focuses on different control strategies for manipulator arms. I was hooked. However I had no way of poking round with the control schemes other than with the equations in MATLAB, gross. 

Around this time I had me Dr. Ambrose and agreed to a Phd in his lab. Prior to this I had saved up a decent chunk of change to self-fund a masters. As a phd student I would get my tuition paid for so I would not need the money I saved right away. 

My next logical step? I loved 612, and I no longer need to self fund a masters. What if I tried to buy an arm to implement some of the things I learned in class? 

great idea.

# Open Source Robot Arm
I figured the most cost effective way to get a arm would be to build one myself. I found a source from reddits called [Annin Robotics](https://www.anninrobotics.com/) that sold predesigned robot arms. They sold the mechanical parts directly with a related kit from StepperOnline for motors and drivers. The kit can with a Bill of Materials for everything I'd need to procure off amazon for wiring, electrical housing, and 3D printing. $3k and a mess of amazon orders later I had the makings of what would was shaping up to be a fun winter break before grad school.

None of the parts came in on time, and I started building at the same time that we began designs for RoboBall

Naturally, the gold and white pendulum took more of my time. In the process of designing the pendulum with Ambrose there were some design lesson that were not carried out in the arm. 

# A Comparison of Protoypes, a Lesson in Design
I think the best way to enumerate the differences is a side by side comparison of how different design teqchniques were implemented. 

## Lession 1 - Bolt Variety.
The AR3 arm came with a myriad of various bolts, from set screws, socket, button, and counter sunk threads. All in metric for that matter. Whereas for RoboBall we were instructed to only use one of four types of socket head screws: 4-40, 6-32, 8-32, and 10-32. And most of the time used 4s or 10s rarely anything else. 

I didnt ow big of a deal this would make on assembly until I lost a set screw. Only to realize Home Depot doesnt carry metric machine screws, I had to settle for a $5 amazon order for a 50-pck when I only needed one. 
Pictures? 
## Lesson 2 - Designing for Assembly and Maintenance.
The Annin

## Month day - summary

# Bulleted Notes
<!-- 
## Image Carousel
{{< carousel images="gallery/*" aspectRatio="16-9" interval="2500">}}

## single picture with caption
![Alt text](featured.JPG "Parker and Tex Walking to the bank")

## a galery of pictures
{{< gallery >}}
  <img src="gallery/IMG_8595.JPG" class="grid-w50 md:grid-w33 xl:grid-w25" />
  <img src="gallery/IMG_8598.JPG" class="grid-w50 md:grid-w33 xl:grid-w25" />
  <img src="gallery/IMG_8599.JPG" class="grid-w50 md:grid-w33 xl:grid-w25" />
  <img src="gallery/IMG_8600.JPG" class="grid-w50 md:grid-w33 xl:grid-w25" />
  
{{< /gallery >}} -->
