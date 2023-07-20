import statsmodels.api as sm
from statsmodels.graphics import tsaplots
import matplotlib.pyplot as plt


yt = [6.7, 5.9, 5.2, 4.8, 4.4, 4.8, 5.4, 5.6, 5.4, 5.5, 5.5, 4.3, 4.9, 4.5, 5.3, 3.9, 5.5, 4.8, 4.8, 3.5, 4.6, 3.1, 6.2,
      5.3, 5.7, 5.8, 4.6, 4.9, 3.6, 5.4, 5.4, 5.1, 4.7, 3.8, 4.8, 4.6, 5.9]

print(sm.tsa.acf(yt, nlags=18, fft=False))
fig = tsaplots.plot_acf(yt, lags=18, alpha=0.05, fft=False)
plt.show()
