from src.common import imread_gray, imwrite
from src.degrade import add_gaussian_noise
from src.level_medium import gaussian_smooth, wiener_filter, nlm_filter
from src.metrics import psnr, ssim_wrap

# Load clean image
img = imread_gray("data/clean/SSR.jpg")  # update name if needed

# Add Gaussian noise
noisy = add_gaussian_noise(img, sigma=20)

# Apply filters
gauss = gaussian_smooth(noisy)
wiener = wiener_filter(noisy)
nlm = nlm_filter(noisy)

# Save output
imwrite("data/results/m_noisy.png", noisy)
imwrite("data/results/m_gaussian_smooth.png", gauss)
imwrite("data/results/m_wiener.png", wiener)
imwrite("data/results/m_nlm.png", nlm)

# Print quality scores
print("\n--- Medium Level Results ---")
print("Gaussian Smooth  -> PSNR:", psnr(img, gauss), "SSIM:", ssim_wrap(img, gauss))
print("Wiener Filter    -> PSNR:", psnr(img, wiener), "SSIM:", ssim_wrap(img, wiener))
print("NLM Filter       -> PSNR:", psnr(img, nlm), "SSIM:", ssim_wrap(img, nlm))
