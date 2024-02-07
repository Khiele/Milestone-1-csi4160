A Raspberry Pi set up with a USB webcam is required to run this project.

Steps to run the project Include:

Raspberry Pi:

Start by obtaining a Raspberry Pi board. Ensure it has the necessary ports for connecting peripherals.
USB Camera:

Connect a compatible USB camera to one of the USB ports on the Raspberry Pi. Make sure the camera is recognized by the Raspberry Pi.

Software Setup:

Raspberry Pi OS:

Install Raspberry Pi OS on a microSD card and insert it into the Raspberry Pi. You can use tools like Raspberry Pi Imager for this task.
Update and Upgrade:

After booting up the Raspberry Pi, open a terminal and run the following commands to ensure your system is up-to-date:
sudo apt-get update
sudo apt-get upgrade

Python and OpenCV:

Install Python and OpenCV, a computer vision library, on the Raspberry Pi. OpenCV can be installed using the following command:
sudo apt-get install python3-opencv

fswebcam:

Install the fswebcam package, which allows capturing images from the USB camera:
sudo apt-get install fswebcam

Download the haarcascade_frontalface_default.xml file to your home directory:
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml -O ~/haarcascade_frontalface_default.xml
This command downloads the file and saves it as haarcascade_frontalface_default.xml in your home directory (~/).

Esnure that all file pathing is correct and specific to your Linux file system, change directories and code referencing pathing as needed.

That's it! Run the script using the Raspberry Pi connected to a desktop to make use of its graphical interface for real time results.
Run the code with this command:
python face_track_copy.py 

This script can be modified to your liking and improved upon for specific usage. Please reference the offical report for more details and results attached below:
[CSI 4160 - Milestone 1 Report.docx.pdf](https://github.com/Khiele/Milestone-1-csi4160/files/14201464/CSI.4160.-.Milestone.1.Report.docx.pdf)


