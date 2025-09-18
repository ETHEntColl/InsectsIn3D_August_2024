# Create Model

### SETUP

Before you start to process the images created by the ‘disc3D’ scanner make sure that the folder ‘ETHZ-ENTXXXXXX’ is stored locally on ‘C:\InsectScanner\Data\DataCurrent\WEEK XX’. 

<aside>
📌 If the data is not stored locally, the processing time will double due to the data transfer limit of the network.

</aside>

---

### 1 STEP

<img src="img/01.jpg" width="800"/>
![Metashape UI](01.jpg)

Metashape UI

### 2 STEP

![Menu bar / Window / Add folder](02.jpg)

Menu bar / Window / Add folder

![Add Photos context window](03.jpg)

Add Photos context window

Add the ‘edof’ folder with ~396 images from:
‘C:\InsectScanner\Data\DataCurrent\WEEK XX\ETHZ-ENTXXXXXX\edof. 

### 3 STEP

![Menu bar / File / Import Reference](04.jpg)

Menu bar / File / Import Reference

![Import CSV ](04a.jpg)

Import CSV 

Add the ‘CamPos.txt’ file
‘C:\InsectScanner\Data\DataCurrent\

Coordinate System: mm
**Delimiter:** Space
**Columns:** Label: 1; x: 2; y: 3; z: 4
**Accuracy:** ✔️ all 5

### 4 STEP

<img src="img/DSC09559.jpg" width="800"/>
![ScanInformation.pdf](camera_constant_snipping.jpg)

ScanInformation.pdf

![Menu bar / Tool / Camera calibration](04b.jpg)

Menu bar / Tool / Camera calibration

![Camera calibration context window](04c.jpg)

Camera calibration context window

Context window menu point ‘Initial’:
**Type:** Precallibrated
**Copy the ‘f:’** value from the 'ScanInformation.pdf' (Camera constant)

### 5 STEP

![Menu bar / Workflow / Align Photos](05.jpg)

Menu bar / Workflow / Align Photos

**Accuracy:** Highest
**Key point limit:** 250,000
**Tie point limit:** 250,000
**Generic preselection:** ✔️
**Nelio: Generic preselection off**
**Reference preselection:** ✔️
**Exclude stationary tie points:** ✔️

![Align Photos context window](06.jpg)

Align Photos context window

### 6 STEP

<img src="img/DSC09559.jpg" width="800"/>
![Metashape UI](07.jpg)

Metashape UI

The calculated cloud points should visualise a clear picture of the specimen.

### 7 STEP

![Tools / Optimise Cameras…](OptimizeF_01.jpg)

Tools / Optimise Cameras…

![OptimizeF 02.jpg](OptimizeF_02.jpg)

**Fit f:** ✔️

### 8 STEP

![Menu bar / Workflow / Build Mesh](05_new.jpg)

Menu bar / Workflow / Build Mesh

![Build Mesh context window](08.jpg)

Build Mesh context window

**Source data:** Depth maps
**Surface type:** Arbitrary (3D)
**Quality:** Ultra high
**Face count:** High
**Interpolation:** Enabled (default)
**Calculate vertex colours:** ✔️ (optional)
**Reuse depth maps:** ✔️

### TWEAKS

For advanced usage of the tweaks please check below:

<aside>
‼️

[Tweak advanced](https://www.notion.so/Tweak-advanced-85b657e1a6624d4a97f6adeec4329139?pvs=21) 

</aside>

![Tools / Preferences](Tweak.jpg)

Tools / Preferences

![Advanced / Tweaks](02_Tweak.jpg)

Advanced / Tweaks

![Tweaks](03_Tweak.jpg)

Tweaks

**BuildModel/ooc_surface_blow_up** 0.75

**BuildModel/ooc_surface_blow_off** 0.75

![Off 2.jpg](Off_2.jpg)

*BuildModel/occ_surface_blow_off 2*

![Up 2.jpg](Up_2.jpg)

*BuildModel/occ_surface_blow_up 2*

![NoTweak.jpg](NoTweak.jpg)

*No tweak*

![TvlTweak.jpg](TvlTweak.jpg)

*Tvl tweak*

![BlowTweak.jpg](BlowTweak.jpg)

*Blow tweak*

---

![With tweak from Ernst blowOffUp.jpg](With_tweak_from_Ernst_blowOffUp.jpg)

BuildModel/occ_surface_blow

![With tweak from 1.4 Metashape.jpg](With_tweak_from_1.4_Metashape.jpg)

*BuildModel/tvl1_mesh = false*

![With tweak from Ernst blowOffUp 02.jpg](With_tweak_from_Ernst_blowOffUp_02.jpg)

![With tweak from 1.4 Metashape02.jpg](With_tweak_from_1.4_Metashape02.jpg)

### 9 STEP

![Tools / Mesh / Smooth ](01_smooth.jpg)

Tools / Mesh / Smooth 

**Strength:** 2.00

**Christian: No Smooth**

<p align="left">
  <img src="img/02_smooth.jpg" height="400"/>
  <img src="img/03_smo03_smoothoth.jpg" height="400"/>
</p>

Without smooth 

<p align="left">
  <img src="img/04_smooth.jpg" height="400"/>
  <img src="img/04_smooth.jpg" height="400"/>
</p>

With smooth 

<p align="left">
  <img src="img/05_smooth.jpg" height="400"/>
  <img src="img/06_smooth.jpg" height="400"/>
</p>

### 10 STEP

<p align="left">
  <img src="img/10.jpg" height="400"/>
  <img src="img/11.jpg" height="400"/>
</p>

**Texture type:** Diffuse map
**Source data:** Images
**Mapping mode:** Generic
**Blending mode:** Mosaic (default)
**Texture size/count:** 4096 x 1

### 11 STEP

<img src="img/12.jpg" width="800"/>

Metashape UI

### 12 STEP

<img src="img/13_Export.jpg" width="400"/>

Export model