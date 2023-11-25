---
Author: Vighnesh Nayak
Date: 06/11/2023
Course: Digital Image Processing
tags: [dip, cv]
---
# Color Models
---
- RGB - Monitors
- CMY/ CMYK - Printers
- YCbCr - efficient transmission and storage
- HSV / HSI -Human vision

## RGB

## CMY(K)
- cyan, magenta and yellow are opposites of red, green and blue respectively in a color spectrum.
- They are called secondary colors of light and primary colors of pigments.
- Since printing is a subtractive process, we use *CMY* extensively in color printing.
- Printer prints colored dots of different sizes and colors in a grid width small spacing. Small spacing makes it impossible for eyes to distinguish dots and they appear as a single color.
- This is called *color half-toning*.
- To save costs black is printed using different pigment even though it is a *full combination of CMY*. It is represented by *K*.
- *Negative after-images*: If cones of retina corresponding to a particular color are saturated due to long exposure, we tend to see negative after-images in the same shape as saturation image.

## HSI
- hue, saturation, intensity.
- Hue - angular quantity, Pure color
- Saturation - amount of white
- Intensity - amount of black
- This is intuitively how humans perceive colors.
- ![](https://lh7-us.googleusercontent.com/0vT9d5zJ2aOvz-vDrmwTNUdN_qITFBAwQDBSvqqpS3I6PbKELv6uA3zrpybkdLedgrQYpy52vSrrSSquJSRnmAdr9Oq_LYACywEYOsnE6JVPgLneD7mfV5aW1QnBPtrHTshb5as5HgBTe8IyKqR-AQ=s2048)
- Intensity increases as we move from black to white on the intensity line.
- Consider a plane perpendicular to the intensity line (in 3D). Saturation of a color increases as we move on that plane away from the point where the plane and the intensity line intersect.
- How to determine hue? Pick any point (e.g. yellow) in the RGB cube, and draw a triangle connecting that point with the white point and black point. All points inside or on this triangle have the same hue. Any such point would be a color corresponding to a convex combination of yellow, black and white, i.e. of the form a x yellow + b x black + c x red, where a, b, c are non-negative and sum to 1. By rotating this triangle about the intensity axis, you will get different hues.
- 
- ![](https://lh7-us.googleusercontent.com/IDReZtVRqLpxYIbekmdiEMKdZLEXQcoptZa6-Te-K49SbjzBTBwrSMbl424a7VOIaZ6_dRmOrgm1NWWViv3cEjgfSg5leYNlhImaT7a0VyxLH2HCo4L4QkTUJIVn9gWeT0ampKXYW4bhgt-coipf2A=s2048)
- **RGB to HSI** conversion: ![](https://lh7-us.googleusercontent.com/CaUfBxpapqCra0Rpyt4BsJbK4BqnSG5cX2GiFAvFlnroBpthfhB95gfm69myIJ3TwEN4McX5G2x5RBj_klxFqdLUG7Ni3O4Bi_Ia-vvGhjRjnQjvApyelQvIk3Z78LrnEtONGqvlRKLVifTmXLpo3w=s2048)
- Hue is independent of scaling of R,G,B and constant offsets added to R,G,B.
- ***By convention, red is considered 0 degrees.***
### Practical use of Hue
- ![](https://lh7-us.googleusercontent.com/kbzZ9Y0i7sYB66lmbpjCrcJyPLfCXUvOYYrxYNOWvsbY1Leu_mFA37wnkABkK2DaDwrfTpo1_HjaO0vi0RXdWibgzQvBGVxGdAPOzuls8J4fbxk5Ntgh8BlQXFd7Rd_0odzAH9tA0dkx8Av0jmT4CA=s2048)
- Ambient and specular components are assumed to be same across RGB [neutral reflection model](Neutral%20Reflection%20Model).
- Hue is invariant to specular reflection, strength of lighting, lighting direction and, viewing direction.
- Hue is thus said to be an “illumination invariant” feature.
- **Demerits**: if R=G=B hue is unstable.
- chromaticity vector are also illumination invariant.
	- ![](https://lh7-us.googleusercontent.com/hrA7Z30PJREX8X0JTrxT2Nh4prQFE0E4Xe-idO2gpvdZ8k-6TVqXENLXALcDVPvtm6twTTTPKC9aH9Uq-D7yNx0MuIRJ0geGdgsvJjDB46iTTKEsr88dgv-slLqMqlmhFs2yG3bc8FPAzwGNauVrIw=s2048)
- 