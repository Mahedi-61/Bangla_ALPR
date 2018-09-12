import re
import os

labels = ["license"]
darknet_dir = "/home/mahedi/Desktop/LP/blp_recognition/libs/darknet"

os.chdir(darknet_dir)
os.makedirs("crop_img", exist_ok = True)
license_count = 0

with open(os.path.join(darknet_dir, "result.txt"), "r") as file:
    line = file.readline()
    line = file.readline()
    line = file.readline()
    line = file.readline()

    while (not line.find("Predicted") == -1):

        if "Enter Image Path" in line:
            image_path = (line.split(":")[1])[1:]
            # print(image_path)
        
        while(True):
            line = file.readline()
            detected_class_label = (line.split("(")[0]).split(":")[0]

            if detected_class_label in labels:
                # print(detected_class_label)
                license_count += 1

                # increasing area (skip this portion, if you don't need it)
                cor = re.findall(r'\d+', (line.split("(")[1]))
       
                left = int (cor[0]) - 25
                if (left < 0): left = 0
            
                top = int (cor[1]) - 25
                if (top < 0): top = 0

                width = int (cor[2]) + 50
                height = int (cor[3]) + 50

                # making bounding box coordinates in imagemagick format (WxH+X+Y)
                crop = str(width) + "x" + str(height) + "+" + str(left) + "+" + str(top)

                # saving output directory
                output_dir = os.path.join(darknet_dir, "crop_img", detected_class_label)
                os.makedirs(output_dir, exist_ok = True)

                input_path = os.path.join(darknet_dir, image_path)
                output_path = os.path.join(output_dir, str(license_count) + ".jpg")
                os.system("convert -crop " + crop + " " + input_path + " " + output_path)

            else:
                break


