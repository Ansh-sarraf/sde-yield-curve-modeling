# Applications of First-Order and Stochastic Differential Equations in Yield Curve Modeling

**Author:** Ansh Sarraf (BSD-DH-2406), Second Year
**Institution:** Indian Statistical Institute, Delhi Centre

## Overview
This project explores the mathematical framework underlying interest rate dynamics, transitioning from deterministic models to stochastic processes[cite: 4]. Accurately modeling the yield curve is essential for pricing fixed-income securities, but traditional first-order ordinary differential equations (ODEs) fail to capture the inherent, unpredictable volatility of financial markets[cite: 4]. This study examines Stochastic Differential Equations (SDEs), focusing primarily on the Vasicek interest rate model, to provide a more realistic representation of short-rate movements over time[cite: 4].

## Key Contributions
* **Mathematical Formulation:** Decomposes interest rate movements into a deterministic, mean-reverting drift component and a stochastic diffusion term driven by Brownian motion[cite: 4].
* **Numerical Simulation:** Implements the Euler-Maruyama discretization scheme in Python using NumPy and Matplotlib to simulate an ensemble of short-rate trajectories[cite: 4].
* **Yield Curve Construction:** Translates simulated initial states into implied zero-coupon yield curves using closed-form affine term structure formulae[cite: 4]. 
* **Model Diagnosis:** Identifies the structural limitation of the Vasicek model—its allowance of strictly negative interest rates—and proposes the Cox-Ingersoll-Ross (CIR) model with the Feller condition $(2\kappa\theta\ge\sigma^{2})$ as an extension for future work to guarantee strictly positive rates[cite: 4].

## Repository Contents
* `Yield_Curve_SDE_Report.pdf`: The complete mathematical derivation, methodology, and numerical analysis[cite: 4].
* `vasicek_simulation.py`: The Python implementation of the Euler-Maruyama simulation and yield curve visualizations[cite: 4].

## Results
The computational pipeline successfully simulated an ensemble of 1,000 short-rate paths over a 5-year horizon $(\Delta t=1/252)$[cite: 4]. The simulated paths visually corroborated the core theoretical properties of the Vasicek SDE, demonstrating an exponential decay toward the 5% long-run mean and a bounded variance expansion approaching stationarity[cite: 4]. The resulting implied yield curve exhibited a financially intuitive normal, concave shape, reflecting a 114 basis point term premium and a 22 basis point convexity correction arising from the non-linear exponential pricing formula[cite: 4].
