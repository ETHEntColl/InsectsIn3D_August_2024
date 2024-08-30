import exiftool
import glob
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
import os


output_path = "MCSN.csv" # Where the dataframe should be written to
root = "Z:\\01_SCANNED_AND_PROCESSED\\02 FINAL\\05_MCSN_Preview_20240716\\" # The path to the images with the rating

exif = exiftool.ExifTool()
exif.start()

df = pd.DataFrame(columns=['Name', 'Rating', 'Keywords'])

images = glob.glob(root + "*.jpg")
count = [0, 0, 0, 0, 0, 0]
for image in tqdm(images):
    # Extract the rating and jeywirds
    x = exif.get_tags(['rating'], image)
    keywords = exif.get_tags(['Keywords'], image)
    name = os.path.basename(image).rstrip('image.jpg').rstrip('3d.jpg')
    name = name.rstrip('_top_').rstrip('_bottom_').rstrip('_side_')
    row = [name, 0, '']
    if 'XMP:Rating' in x.keys():
        count[int(x['XMP:Rating'])] += 1
        row[1] = int(x['XMP:Rating'])
    if 'IPTC:Keywords' in keywords.keys():
        keys = keywords['IPTC:Keywords']
        if isinstance(keys, list):
            row[2] = ','.join(keys)
        else:
            row[2] = keys
    else:
        count[0] += 1
    df.loc[len(df)] = row
exif.terminate()


# Merge all images that describe the same insect
def merge_rows(group):
    # Handle Rating column
    ratings = group['Rating'].values
    non_zero_ratings = [r for r in ratings if r != 0]
    
    if len(non_zero_ratings) > 1:
        print(group)
        # raise ValueError("Multiple non-zero ratings found, can't merge")
    
    merged_rating = non_zero_ratings[0] if non_zero_ratings else 0
    
    # Handle Keywords column
    merged_keywords = ','.join(group['Keywords']).strip(',')
    
    return pd.Series({
        'Name': group['Name'].iloc[0],
        'Rating': merged_rating,
        'Keywords': merged_keywords
    })

# Export
df = df.groupby('Name').apply(merge_rows).reset_index(drop=True)
df.to_csv(output_path, sep=';')