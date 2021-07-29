1. Simple Assignment – Draw boxes on an Image
Here your objective is to draw rectangles (or boxes) around traffic lights in an image. Use opencv and 
python to easily achieve this. The locations of the boxes, along with more properties, will be specified 
in “data files”.
• You will be given a set of images (jpeg) and corresponding data files (xml). Here is the link. 
You should be able to read the image in python using opencv and draw boxes as well with 
opencv in python.
• Each rectangle is represented as 4 values – x_min, x_max, y_min, y_max, present in the data 
files. These data files are in XML format (which is a markup language). All you’ll need to do is 
read these data files in the same python code and get (or extract) the positions of the boxes from 
the xml data
• After drawing all rectangles on the image, write the images to file (save them) and submit the 
saved images back
• Bonus Points: Display state of the Traffic Light in as a text – Each rectangle also in addition has 
“name” which is state of the traffic light, your task is to display this as a text for each traffic 
light on the image.
• Tips:
◦ Write your code in a modular (with functions) fashion
◦ Use cv2 in python – this should have all necessary functions to achieve this task
◦ There may be images with no rectangles/traffic lights as well.
◦ Draw all rectangles for traffic lights given in the data files (xml files).
