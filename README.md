# PoolCam

## Product Description
As a semester-long project for an engineering class, Madison Shimbo, Youssef Boutros-Ghali, Kobe Minnick, and Payam Bostani created a learning tool for inexperienced players of billiards pool to help new players overcome the problem of the steep and/or intimidating learning curve of the game.

## How It Works
The product is attached to the pool table and hovered over the desired area for analysis. Using a Raspberry Pi and a Raspberry Pi camera, the product is able to identify the cue ball and the target ball (the one you choose as the one you want to end up hitting) through a live camera feed using color/shape recognition. Using vector math and the Python library OpenCV, the product is able to calculate and draw a visualization of the optimal path and angle the user needs to hit the cue ball at to get the target ball into a given hole as a guide. This visualization is then projected onto a nearby wall for the user to easily refer to.

See images below as references for how the color/shape recognition and masking worked:

Before masking (live footage):

![Example Before Masking](/README_images/example_before_masking.jpg)

After masking (cue ball recognition):

![Example After Masking - Cue Ball](/README_images/example_cue_ball_mask.png)

After masking (target ball recognition):

![Example After Masking - Eight Ball](/README_images/example_eight_ball_mask.png)

## Product Design
The Raspberry Pi and camera used as well as the projector and other related technology was encased in a wooden box with a 3D-printed box to hold the Raspberry Pi in place with a hole for the camera view. This box was attached to arms that could attach to a pool table.
![Demo photo](/README_images/demo_1.jpg)  

![Isometric View of Wooden Box](/README_images/box_isometric_view.jpg)
![Top View of Wooden Box](/README_images/box_top_view.jpg)
![Bottom View of Wooden Box](/README_images/box_bottom_view.jpg)
## Other Details

**Technologies/Tools Used: Python, Raspberry Pi, CAD, Fusion360**

RAD Project Group 36 NYU 2019
