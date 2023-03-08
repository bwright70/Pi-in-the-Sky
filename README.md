# Joe B.I.E.ndenburg (Not A Blimp)

## Table of Contents

README.md:

- [README.md](/README.md)
- [Youtube Channel](#youtube-channel)
- [CAD](#cad)
  - [The Design](#the-design)
  - [The Assembly](#the-assembly)
  - [Difficulties](#difficulties)
  - [CAD Images](#the-images)

Other Pages:

- [PLANNING.md](/PLANNING.md)

Directories:

- [Code](/Code/CODE.md)
- [Images](/Images/IMAGES.md)

## YouTube Channel

| #   | Date       | Video                                                               |
| --- | ---------- | ------------------------------------------------------------------- |
| 0   | 2023-01-18 | [CAD Catch-up](https://youtu.be/xfZlytLQ_GU)                        |
| 1   | 2023-01-18 | [Code Catch-up](https://youtu.be/OjiJY7ihrKs)                       |
| 2   | 2023-01-25 | [The Frame's Here!!](https://youtu.be/7JANqRXmuZ0)                  |
| 3   | 2023-02-02 | [Ball🎈🎈n(s?)!!!!](https://youtu.be/61AMVDbxwmk)                   |
| 4   | 2023-02-08 | [Buoyant Spice and Joey Trash](https://youtu.be/qYgovjCG950)        |
| 5   | 2023-02-15 | [Issues, but No Tissues](https://youtu.be/tmu2Px-Pnoc)              |
| 6   | 2023-02-22 | [Money, Money, Money (Must Be Funny)](https://youtu.be/B1QbSnAPkFs) |

## CAD

[Onshape Document](https://cvilleschools.onshape.com/documents/03b6c87fd63f0cfe1abe3b9f/w/c0d37a57fae264806faea58d/e/ea3240c36bb4a6a681fb9b2a)

### The Design

The idea behind this project is to make a series of partial ring connectors that can be assembled to make a much larger frame. The major problem we've been working against is having enough volume to carry the weight of the Pi and Frame. The print beds of the 3d printers are only 210mm by 210mm which is a massive size constraint. So we made a ring into six sections attached by balsa wood spars that would be much larger than just a single ring.

Each ring section has three connection points: Two on the ends and one in the middle. The balsa spars alternate between connection points which adds ridgitity without adding much weight.

The main goal was to optimize volume while at the same time adding as little weight as possible. The ring connectors are as light as possible while still retaining structure and balsa wood is incredibly light. The entire frame in onshape only weighs 105.102 grams (this is acutally heavier than the true frame because all ring sections are printed in vase mode which makes them hollow), but has an internal volume of about 480 Liters or 16.951 Cubic Feet

### The Assembly

There are three components to the Zepplin: The Frame, The Balloon, and The Pi. The frame consists of four rings that alternate connection points. The Balloon is inside the frame and filled with helium. The Pi is attached to the frame on the outside.

### Difficulties

The biggest challenge was just fine tuning the connector points so that they were a tight fit around the balsa spars but not too tight that assembly was impossible. After several test prints we eventaully landed on a perfect fit.

Originally there was going to be a 5th ring that would fit outside the mylar balloon but we scrapped this idea once we decided that the balloon would be internal the 5th ring was scrapped in favor of a single unique attachment that would hold the Pi Bird.

### The Images

Up-close of connector for balsa-wood spars:

![Balsa-wood Spar Connector](/Images/Spar-Connector.png)

Full 6-Section Assembly:

![6-Section Assembly](/Images/6-Section-Assembly.png)

Up-close of Pi-bird, aka attachment plate for Pico and other wiring components:

![Pi Bird](/Images/Pi-Bird.png)

## Helium Bladder

### The Design

We knew from the very start of our project that we were going to need some sort of container for the helium. Intially we were planning on the frame being internal, but there were many problems with this, the main one being 'How do we get the air out and the helium in without crushing the frame', and upon futher research we discovered that zeppelins actually have an internal bladder as well. This made things much easier. 

The Bladder had to accomplish three things:
1. Keep the helium in 
2. Be super light
3. Be easy to seal so that we wouldn't have to buy fancy industrial equipment for our project 

### Material

We had two options with the material that we could make the bladder out of. Orignally we planned to make the bladder out of Mylar. Heat sealing is the best and easiest way to seal the bladder, and, after some difficulties with heat sealing mylar due to it's sealing temperature being quite high and it not wanting it adhere to itself, we also looked into Polyethylene which is what trash bags are typically made of. 

#### Pros of Mylar:
- Cheap 
- Light 
- It's what fancy balloons are made of 

#### Cons of Mylar: 
- It does heat seal but not with the equipment we had on hand which means we would need to use a contact adhesive 
- The mylar we were able to get was inconviently sized meaning we would need to seal several sheets together

#### Pros of Polyethylene: 
- Free (provided by the school)
- Very easy to heat seal with supplies on hand 
- Allowed for more trial and error because we had a functionally unlimited amount 
- It's also what fancy balloons are made of 

#### Cons of Polyethylene:
- Not as light as Mylar 
- Pretty bulky which is bad for a design that has to be light and volume efficent 

### Trials 

In the end we choose polyethylene. The ability to heat seal with just a hair straightner made it a much better option espically since the addition of a contact adhesive nessissary to seal mylar would make it's weight advantage void. 

We went through many tests of the sealing method and determined that, while heating seal does weaken the trash bag around the seal leading to micro tears, as long as too much pressure isn't put on the seams they would hold air, and hopefully helium, just fine. 

The final design ended up being two trash bags sealed together by their openings and cut open at the ends and resealed in order to maximize volume.

## Code

Code diagram for design with no propellers (initial design):

![CodeBlockDiagram](/Images/CodeBlockNoMovementControl.png)

Code diagram for design with propellers (potential final design):

![CodeBlockDiagram2](/Images/CodeBlockMovementControl.png)

[Current code file](https://github.com/bwright70/Pi-in-the-Sky/blob/main/Code/Code_v1.py)

### Wiring

Wiring diagram:

![Wiring](/Images/WiringDiagram.png)
