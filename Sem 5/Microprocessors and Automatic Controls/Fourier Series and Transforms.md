---
Author: Vighnesh Nayak
Date: 26/10/2023
Course: Microprocessors and Automatic Controls
tags: [controls]
---
# Fourier Series and Transforms
---

## Fourier Series for Periodic functions $f$.
Fourier series is the expansion of any periodic function in terms of sum of **sine and cosine waves.** Summing up the infinite terms of the series gives the periodic function. 

---
Fourier series in **real form** is given by,
$$\mathcal{F}(f)=a_0+\sum_{n=1}^{\infty}\left(a_n\cos{\left(\frac{n\pi x}{l}\right)}+b_n\sin{\left(\frac{n\pi x}{l}\right)}\right) $$
$$a_0=\frac{1}{2l}\int_{-l}^{l}f(x)dx,$$
$$a_n=\frac{1}{l}\int_{-l}^{l}f(x)\cos{\frac{n\pi x}{l}}dx,$$
$$b_n=\frac{1}{l}\int_{-l}^{l}f(x)\sin{\frac{n\pi x}{l}}dx$$

---
In **complex form**,

$$\mathcal{F}(f)=\sum_{n=-\infty}^{\infty}c_ne^{in\pi\frac{x}{l}}$$
$$c_n=\frac{1}{2l}\int_{-l}^{l}f(x)e^{-in\pi\frac{x}{l}}\,dx$$

---
## Fourier Transform for Aperiodic functions $f$.

$$f_T(t)=\mathcal{F}(f)=\sum_{n=-\infty}^{\infty}c_ne^{in\omega_0t}, \quad \quad \omega_0=\frac{2\pi}{T},T=2l$$
$$c_n=\frac{1}{T}\int_{-l}^{l}f(t)e^{-in\omega_0t}\,dt$$

Let $n\omega_0=\omega$, $\implies \Delta\omega=\omega_0$.
For aperiodic functions $T\to\infty$. $\implies \omega_0\to0, \Delta\omega\to0$
Replacing $T$ with $\frac{2\pi}{\omega_0}$
$$f_T(t)=\sum_{n=-\infty}^{\infty}\frac{\omega_0}{2\pi}\left(\int_{-T/2}^{T/2}f(t)e^{-i\omega t}dt\right)e^{i\omega t} $$
$$f_T(t)=\sum_{n=-\infty}^{\infty}\frac{1}{2\pi}\left(\int_{-\infty}^{\infty}f(t)e^{-i\omega t}\,dt\right) \Delta\omega $$
Since $\Delta\omega\to0$ changing summation to integral.
$$f_T(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\mathcal{F}(\omega)e^{i\omega t}d\omega,$$
$$\mathcal{F}(\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t} $$

$\mathcal{F}(\omega)$ is called the Fourier transform of $f(t)$.

$f(t)$ is called the Inverse Fourier transform of $\mathcal{F}(\omega)$.

---
## Disadvantages.
- Fourier Transform being and oscillating integral over infinite interval can very easily diverge.
- In control applications, we are often interested in signals that start at time zero (T = 0) and are zero before this initial time instant.
#### Hence we use [Laplace Transforms](Laplace%20Transforms.md) more often in controls.
