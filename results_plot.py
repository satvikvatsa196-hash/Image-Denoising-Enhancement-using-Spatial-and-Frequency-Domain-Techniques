import matplotlib.pyplot as plt



methods = ["Median (Easy)", "NLM (Medium)", "RL+NLM (Hard)"]

psnr = [29.10, 30.45, 17.03]     # Enter 3 PSNR values here
ssim = [0.94, 0.96, 0.28]        # Enter 3 SSIM values here

# Plot PSNR
plt.figure()
plt.plot(methods, psnr, marker='o')
plt.title("PSNR Comparison")
plt.xlabel("Methods")
plt.ylabel("PSNR (dB)")
plt.grid(True)
plt.show()

# Plot SSIM
plt.figure()
plt.plot(methods, ssim, marker='o')
plt.title("SSIM Comparison")
plt.xlabel("Methods")
plt.ylabel("SSIM")
plt.grid(True)
plt.show()
