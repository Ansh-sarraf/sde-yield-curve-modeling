import numpy as np
import matplotlib.pyplot as plt

# --- 1. Parameter Initialization (Matches Section 3.2) ---
r0 = 0.03  # Initial short rate (3%)
kappa = 0.30  # Mean-reversion speed
theta = 0.05  # Long-run mean (5%)
sigma = 0.02  # Instantaneous volatility
T = 5.0  # Time horizon in years
N = 1260  # Number of time steps (252 days * 5 years)
dt = T / N  # Step size
M = 1000  # Number of simulated paths

# --- 2. Random Matrix Generation ---
# Draw all random standard normals at once for speed
np.random.seed(42)  # For reproducible graphs in your paper
Z = np.random.standard_normal((M, N))

# --- 3. Path Simulation (Euler-Maruyama) ---
# Initialize the matrix to hold all paths
r = np.zeros((M, N + 1))
r[:, 0] = r0

# Iterate through time steps
for i in range(N):
    # Vectorized update across all M paths simultaneously
    drift = kappa * (theta - r[:, i]) * dt
    diffusion = sigma * np.sqrt(dt) * Z[:, i]
    r[:, i + 1] = r[:, i] + drift + diffusion

# --- 4. Bond Price & Yield Curve Computation ---
# Maturity grid: 30 steps up to 10 years
T_max = 10.0
K = 30
tau = np.linspace(T_max / K, T_max, K)

yield_curve = np.zeros(K)

for k, t in enumerate(tau):
    # Vasicek Affine Formula
    B = (1 - np.exp(-kappa * t)) / kappa
    A = np.exp((theta - (sigma ** 2) / (2 * kappa ** 2)) * (B - t) - (sigma ** 2 / (4 * kappa)) * B ** 2)

    # Calculate bond price using the initial rate r0 (for the current yield curve)
    P = A * np.exp(-B * r0)

    # Convert to continuously compounded yield
    yield_curve[k] = -np.log(P) / t

# --- 5. Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')

# Plot 1: Simulated Paths (Plotting only first 100 for visual clarity)
plt.figure(figsize=(10, 5))
time_grid = np.linspace(0, T, N + 1)
for j in range(100):
    plt.plot(time_grid, r[j, :], lw=0.8, alpha=0.5)
plt.axhline(theta, color='black', linestyle='--', label='Long-run Mean (θ)')
plt.title('Vasicek Model: Simulated Short Rate Paths (Euler-Maruyama)')
plt.xlabel('Time (Years)')
plt.ylabel('Interest Rate')
plt.legend()
plt.tight_layout()
plt.savefig('simulated_paths.png', dpi=300, bbox_inches='tight') # <-- ADD THIS LINE
plt.show()

# Plot 2: Implied Yield Curve
plt.figure(figsize=(10, 5))
plt.plot(tau, yield_curve * 100, color='darkblue', marker='o', linestyle='-', linewidth=2)
plt.title('Implied Yield Curve from Vasicek Model at t=0')
plt.xlabel('Time to Maturity (Years)')
plt.ylabel('Yield (%)')
plt.tight_layout()
plt.savefig('yield_curve.png', dpi=300, bbox_inches='tight') # <-- ADD THIS LINE
plt.show()