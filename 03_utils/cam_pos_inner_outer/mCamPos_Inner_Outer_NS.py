import os

base_directory = "C:\\InsectScanner\\Data\\DataCurrent\\0_PREPROCESS\\0_CALCULATION_MASKMODEL"
subfolders = os.listdir(base_directory)

for subfolder in subfolders:
    camera_positions = []
    cam_pos_file_path = os.path.join(base_directory, subfolder, "CamPos.txt")
    
    # Reading the camera positions from CamPos.txt
    with open(cam_pos_file_path, "r") as file:
        for line in file.readlines():
            camera_positions.append(line)

    inner_positions = []
    outer_positions = []
    merged_positions = []

    # Generating inner camera positions
    for cam_pos in camera_positions:
        inner_position = cam_pos.replace("image", "inner")
        inner_positions.append(inner_position)

    # Generating outer camera positions
    for cam_pos in camera_positions:
        outer_position = cam_pos.replace("image", "outer")
        outer_positions.append(outer_position)

    # Merging original, inner, and outer camera positions
    merged_positions = camera_positions + inner_positions + outer_positions

    # Writing the merged positions to mCamPos.txt
    output_file_path = os.path.join(base_directory, subfolder, "mCamPos.txt")
    with open(output_file_path, "w") as output_file:
        for position in merged_positions:
            output_file.write(position)