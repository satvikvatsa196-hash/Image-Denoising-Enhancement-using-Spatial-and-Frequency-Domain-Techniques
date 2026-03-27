#Project Title:

Image Denoising & Enhancement using Spatial and Frequency Domain Techniques

#Developed By:

Shubham Ranjan 

Satvik Vatsa 

Department of Information Technology,

IIIT Bhopal

#Setup Guide
1️. Create virtual environment
python -m venv venv

2️. Activate environment
Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

3️. Install dependencies
pip install -r requirements.txt

4. How to Run
- Easy Level (Salt & Pepper Noise Removal)
python run_easy.py




- Medium Level (Gaussian Noise Removal)
python run_medium.py


Output:

Gaussian smoothing

Wiener filter

Non-Local Means (best)

- Hard Level (Motion Blur + Noise Removal)
python run_hard.py


#Techniques used:

Richardson-Lucy Deblurring

Blind Wiener Deconvolution

NLM Denoising + Sharpening

#Plot Results (PSNR & SSIM Comparison)
python results_plot.py

This generates comparison graphs.

#Features

- Salt & Pepper noise removal
- Gaussian noise smoothing
- Motion blur reduction
- PSNR & SSIM quality metrics
- Auto-save output images
- Real-world enhancement simulation

# Applications

- CCTV image enhancement
- Medical image denoising
- Drone & satellite clarity improvement
- Photo restoration
- Forensic image processing
- Low-light camera noise removal

# Notes
- Put your input image in data/clean/
- Ensure the image name in run scripts matches your file
- Hard level depends on PSF accuracy — result varies with blur severity
- If output looks too soft, adjust sharpening parameters in level_hard.py
