

import numpy as np
import cv2
from src.common import imread_gray, imwrite
from src.degrade import apply_motion_blur, add_gaussian_noise
from src.level_hard import rl_deblur, blind_wiener_deblur, post_denoise

# Load Clean Image
img = imread_gray("data/clean/Blurred-licence-plate.jpg")  

#  Create Motion Blur + Noise
psf_true = np.zeros((15,15))
psf_true[7, :] = 1
psf_true = cv2.GaussianBlur(psf_true, (3,3), 1)
psf_true /= psf_true.sum()

blurred = cv2.filter2D(img, -1, psf_true)
noisy_blur = add_gaussian_noise(blurred, sigma=0.005)  # small noise

# HARD LEVEL PROCESS

# Richardson-Lucy Deblur
rl = rl_deblur(noisy_blur, psf_true, iters=25)

# PSF Guess for Blind Wiener (approximation)
psf_guess = np.zeros((15,15))
psf_guess[7, :] = 1
psf_guess = cv2.GaussianBlur(psf_guess, (3,3), 1)
psf_guess /= psf_guess.sum()

# Blind Wiener Deblur
bw = blind_wiener_deblur(noisy_blur, psf_guess)

# Blind Wiener + NLM Denoise + Sharpen
bw_dn = post_denoise(bw)

# Save Results
imwrite("data/results/hard_rl.png", rl)
imwrite("data/results/hard_wiener.png", bw)
imwrite("data/results/hard_wiener_denoise.png", bw_dn)

#  Print Results 
from src.metrics import psnr, ssim

print("===== HARD LEVEL RESULTS =====")
print("RL:", psnr(img, rl), ssim(img, rl))
print("Blind Wiener:", psnr(img, bw), ssim(img, bw))
print("Blind Wiener + Denoise:", psnr(img, bw_dn), ssim(img, bw_dn))

# Show Output
import matplotlib.pyplot as plt

titles = ["Input Blurred", "RL", "Blind Wiener", "Wiener + Denoise+Sharpen"]
imgs = [noisy_blur, rl, bw, bw_dn]

plt.figure(figsize=(10,5))
for i,(t,im) in enumerate(zip(titles,imgs)):
    plt.subplot(1,4,i+1)
    plt.title(t)
    plt.imshow(im, cmap="gray")
    plt.axis("off")
plt.show()
