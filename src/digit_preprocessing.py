import re
import os
from .. import root_dir

# constant and path variables
labels = ["0", "1", "2", "3", "4", "5", "6",
          "7", "8", "9", "character"]

darknet_dir = root_dir.darknet_path()
crop_char_img_dir = os.path.join(root_dir.data_path(), "crop_char_img")

os.makedirs(crop_char_img_dir, exist_ok = True)
char_count = 0
number_plate = ""

# coding
with open(os.path.join(darknet_dir, "result.txt"), "r") as file:
    line = file.readline()
    line = file.readline()
    line = file.readline()
    line = file.readline()

    while (not line.find("Predicted") == -1):
        print(number_plate)

        if "Enter Image Path" in line:
            image_path = (line.split(":")[1])[1:]
            print(image_path)
            number_plate = ""
      
        while(True):
            line = file.readline()
            detected_class_label = (line.split("(")[0]).split(":")[0]

            # for detected class labels
            if detected_class_label in labels:

                # for digit class
                if(detected_class_label != "character"):
                    number_plate += detected_class_label
                
                # for character class
                else:
                    char_count += 1

                    # increasing area (skip this portion, if you don't need it)
                    cor = re.findall(r'\d+', (line.split("(")[1]))
        
                    left = int (cor[0]) - 10
                    if (left < 0): left = 0
                
                    top = int (cor[1]) - 25
                    if (top < 0): top = 0

                    width = int (cor[2]) + 30
                    height = int (cor[3]) + 50

                    # making bounding box coordinates in imagemagick format (WxH+X+Y)
                    crop = str(width) + "x" + str(height) + "+" + str(left) + "+" + str(top)

                    # saving output directory
                    output_dir = os.path.join(crop_char_img_dir, detected_class_label)
                    os.makedirs(output_dir, exist_ok = True)

                    input_path = os.path.join(darknet_dir, image_path)
                    output_path = os.path.join(output_dir, str(char_count) + ".jpg")
                    os.system("convert -crop " + crop + " " + input_path + " " + output_path)
                
            else:
                break