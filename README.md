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
| 7   | 2023-03-01 | [Orange You Glad to Hear?](https://youtu.be/YR41meGTwW4)            |
|     | 2023-03-08 | No Episode :(                                                       |
| 8   | 2023-03-15 | [The Dark Brandon Rises](https://youtu.be/SJHRT1t6aVk)              |

## CAD

[Onshape Document](https://cvilleschools.onshape.com/documents/03b6c87fd63f0cfe1abe3b9f/w/c0d37a57fae264806faea58d/e/ea3240c36bb4a6a681fb9b2a)

### The Design

The idea behind this project is to make a series of partial ring connectors that can be assembled to make a much larger frame. The major problem we've been working against is having enough volume to carry the weight of the Pi and Frame. The print beds of the 3D printers are only 210 mm by 210 mm, which is a massive size constraint. So we made a ring into six sections attached by balsa wood spars that would be much larger than just a single ring.

Each ring section has three connection points: Two on the ends and one in the middle. The balsa spars alternate between connection points, which adds rigidity without adding much weight.

The main goal was to optimize volume while at the same time adding as little weight as possible. The ring connectors are as light as possible while still retaining structure, and balsa wood is incredibly light. The entire frame in Onshape only weighs 105.102 grams (this is actually heavier than the true frame because all ring sections are printed in vase mode which makes them hollow), but has an internal volume of about 480 Liters or 16.951 Cubic Feet.

### The Assembly

There are three components to the Zeppelin: The Frame, The Helium Bladder, and The Pi. The frame consists of four rings that alternate connection points. The Bladder is inside the frame and filled with helium. The Pi is attached to the frame on the outside.

### Difficulties

The biggest challenge was just fine-tuning the connector points so that they were a tight fit around the balsa spars, but not too tight that assembly was impossible. After several test prints, we eventually landed on a perfect fit.

Originally there was going to be a 5th ring that would fit outside the bladder, but we scrapped this idea once we decided that the bladder would be internal. The 5th ring was scrapped in favor of a single unique attachment (Pi Bird) that would hold the Pi Plate.

The other massive challenge over shadowing the whole project was that of weight. Originally the frame's connector rings were 7 mm thick which provided a fairly rigid structure but was also too heavy. We dropped it to 4 mm which cut nearly 60 grams from the frame at the cost of it being dangerously flexible. The stress points of the frame were not the rings but actually the balsa spars which weren't as flexible as the rings. Fortunately despite its reduced strength, the frame was still able to hold up just fine.

### The Images

Up-close of connector for balsa-wood spars:

![Balsa-wood Spar Connector](/Images/Spar-Connector.png)

Full 6-Section Assembly:

![6-Section Assembly](/Images/Assembly.png)

Up-close of Pi Bird and Pi Plate for Pi and other wiring components:

![Pi Bird](/Images/Pi-Plate.png)

## Helium Bladder

### The Bladder Design

We knew from the very start of our project that we were going to need some sort of container for the helium. Initially, we were planning on the frame being internal, but there were many problems with this, the main one being “How do we get the air out and the helium in without crushing the frame.” Upon further research, we discovered that zeppelins actually have an internal bladder as well. This made things much easier.

The Bladder had to accomplish three things:

1. Keep the helium in.
2. Be super light.
3. Be easy to seal so that we wouldn't have to buy fancy industrial equipment for our project.

### Material

We had two options with the material that we could use for the bladder, and we had planned to make it out of Mylar. Heat sealing is the best and easiest way to seal the bladder, but we had some difficulties with heat-sealing Mylar due to its sealing temperature being quite high. In addition, since it did not want to adhere to itself, we also looked into Polyethylene plastic, which is what trash bags are typically made of.

#### Pros of Mylar

- Cheap
- Light
- It's what fancy balloons are made of

#### Cons of Mylar

- It does heat seal but not with the equipment we had on hand, which means we would need to use a contact adhesive
- The Mylar we were able to get was inconveniently sized, meaning we would need to seal several sheets together

#### Pros of Polyethylene

- Free (provided by the school)
- Very easy to heat seal with supplies on hand
- Allowed for more trial and error because we had a functionally unlimited amount
- It's also what fancy balloons are made of

#### Cons of Polyethylene

- Not as light as Mylar
- Pretty bulky, which is bad for a design that has to be light and volume efficient
- Heat sealing leaves points of weakness around the seams

### Trials

In the end we choose polyethylene. The ability to heat seal with just a hair straightener made it a much better option espically since the addition of a contact adhesive necessary to seal mylar would make it's weight advantage void.

We went through many tests of the sealing method and determined that, while heating seal does weaken the trash bag around the seal leading to micro tears, as long as too much pressure isn't put on the seams they would hold air, and hopefully helium, just fine.

The final design ended up being two trash bags sealed together by their openings and cut open at the ends and resealed in order to maximize volume.

## Code

Code diagram for design with no propellers (initial design):

![CodeBlockDiagram](/Images/CodeBlockNoMovementControl.png)

Code diagram for design with propellers (potential final design):

![CodeBlockDiagram2](/Images/CodeBlockMovementControl.png)

If you looked at the code file and comments this would likely all become apparent, but in spite of brevity I am going to explain how the code works in its entirety. There is a [boot.py](<(/Code/example_cpue_temp/boot.py)>) file which checks whether pin GP0 is connected to the ground pin, if it is, then the pico will be in "write" mode (it will be writing data to the specified file on storage), otherwise it will be in "read" mode, allowing you to read any of the data on the pico through a connected computer. After that the pico will run the code.py file (currently named [Code_v1.py](https://github.com/bwright70/Pi-in-the-Sky/blob/main/Code/Code_v1.py) in our repo) which collects data and writes it to the storage if in write mode, and just gets sort of mad if in read mode. It begins by pulling all the values from the altimeter and accelerometer, then it writes them in seperate columns in an internal storage file, currently formatted as a CSV file.

[Current code file](https://github.com/bwright70/Pi-in-the-Sky/blob/main/Code/Code_v1.py)

The code for the second version of this project is essentially the same but includes sort of pseudo-code to use propeller motors based on hypothetical inputs. Thanks to Paul Schakel and Sam Funk for the motor code in this version ([Here's their repo](https://github.com/sfunk02/drone)). [Version 2](/Code/Code_v2.py)

### Wiring

Wiring diagram:

![Wiring](/Images/WiringDiagram.png)

This wiring is hopefully self explanatory.
