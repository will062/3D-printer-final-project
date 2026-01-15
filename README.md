# 3D-printer-final-project
This project is a project is used to test and and figure out how to use a core-xy CNC and how the motors need to rotate to follow certain g-code paths for a 3d printer and a CNC.
# Brainstorming
There are 2 possible CNC mechanisms to take into consideration before chosing to design for the project. The first one is the x-axis and y-axis are controlled by independent motors like Prusa and Ender motors and there are 2 variations of linear actuation to make this happen. One is to use timing belts and pulleys and the other is to use lead screws. For the purpose of the 3d printing mechanism and costs the extra torque that the lead screw supplies does not benefit the design over choosing timing belts. The second option was a core-XY CNC mechanism used by the bambu labs. I chose the core-XY mechanism both because of the more complex pulleys mechanism and because I have a bambu labs at home so I can take inspiration from when it comes to design. I want to look at the functionality empiracallly of the core-XY and see if I can identify if it is better than the first CNC mechansim.
# Mechanical Design Process
I first started with a top down design strategy for the CNC system by defining the pulley system and designing the rest of the printer around it. Then I realized that this strategy was messy in organization so I switched to bottom up design by designing each componenet individually. In hindsight I probably should have stuck with top down design for the complex assmebly of the printer to save time changing compnenets. Timeline management and organization needs to happen if I want that to be successful. This is the Core-XY pulley system I started out with.

<img width="520" height="552" alt="reference" src="https://github.com/user-attachments/assets/a988ddf6-2e54-4b01-84e6-85da0ad2a825" />

During my transitioning to bottom down design I started with CADing the top part of the printer and changed the motor location to be on the back side of the printer instead of the front. During the design I needed to identify which motor I needed to control my printer. The ideal motor is a stepper motor because it will spin a set amount each time as pulse is sent to it unlike DC motors. Deciding the type of motor was primarily limited by cost but it is very tradition that 3D printers use Nema 17 motors so I looked for the lowest cost Nema 17 motors and its on brand motor controller. There are 2 different pulley systems as shown above with the 2 different color lines to represent the pulleys so I created 2 layers for the 3D printer to make sure the pulley system does not interact with each other.

<img width="1920" height="1009" alt="2d cnc v59 - Autodesk Fusion (Education License)  1_13_2026 10_29_18 PM" src="https://github.com/user-attachments/assets/437e4a03-2113-40da-bdef-c935add05e20" />

Other design considerations is the type of timing belts for the printer and I chose the GT2 belts because the smaller teeth is able to handle smaller and more percise motions. Additionally as a cost saving measure, I designed my own idler pulley for the timing belts using bearings which is able to use the cheap bearing to reduce friction as the pulleys spin. The belt is also the reason why a top down design is a better strategy for this project because it allows me to make sure each component is with the belt geomatry. Another design consideration was how to keep the printer square so I designed a set of clamps on the metal rods on the printer to ensure that the shaft is square against the 3d printer.

<img width="1919" height="1005" alt="Assembly v19_ (William) - Autodesk Fusion (Education License)  12_17_2025 4_48_25 PM" src="https://github.com/user-attachments/assets/f99e3015-53af-4b6b-9ff2-e900fe8c15cf" />
# Electrical Design
To control the 3d printer I used a microcontroller (arduino for testing and rasberry pi for final design), motor controller (DM332t stepper motor controller), and an external power supply. The motor is connected to the motor controller based on the corresponding phases on the motor. The phases represent the 2 difference coils that adjust the magnetic field within the motor to make the motor spin a percise step. The motor controller is powered by the external power supply and controlled by the micro-controller. For rasberry pi specifically a logic level shifter is necessarry because the motor controller registers 5 Volt signals while the GPIO in the rasberry pi is 3.3 V output. A camera can be added onto the rasberry pi for color quantization but that implementation has not been tested yet.

![71IycyW5Y1L _AC_SX679_](https://github.com/user-attachments/assets/16f95469-14a6-43bf-9948-d3b3c347e244)

External Power Supply

![41rgkHMY+ML _AC_SL1000_](https://github.com/user-attachments/assets/d62712a0-066e-4f17-bd16-2b3ee5ebccaf)

Stepper Motor

![61uzJ6NEMHL _SX522_](https://github.com/user-attachments/assets/293147c5-d5db-4d5d-82fe-b677c5d4749a)

Stepper Motor Controller

![71DGV6JC4lL _SL1200_](https://github.com/user-attachments/assets/d2547be0-be9a-4e4f-b460-3bc6ac830d64)

Logic Level Shifter

![electrical drawing](https://github.com/user-attachments/assets/83df7b59-7040-4609-9200-dd8260ef216b)

General Electical Drawing
# Software Logic
The code for the Arduino was a simple test code which was set the output pins and send a certain number of pulses to the motor switch the direction of the motor and send the same number of pulses to the motor. In that case it was 400 pulses so the motor spins one full rotation.

![My Project](https://github.com/user-attachments/assets/c0de9ce6-26fe-47e2-9778-59390e9735d8)

For Rasberry Pi I used the inputs from a controller control the motion of the stepper motor by using the pygame library to detect joystick inputs and converting those joystick inputs into moving the stepper motor. Left on the joystick turns the motor counterclockwise while righting on the joystick will turn the motor clockwise. In addition to that code I also created methods for further use in the future when I want to use 2 motors on the rasberry pi where I change how much each motor spins relative to each other.

For color quantization I used the openCV library and took the camera input and turned the input into a numpy array while turning the uint8 into float32. Then I used open CV library to convert the colors on the picture to 8 distinct colors before converting it back and showing the output of the camera before color quantization and after color quantization.

![Code block diagram](https://github.com/user-attachments/assets/f65c9c99-1940-46b4-9813-e6945847e1df)
