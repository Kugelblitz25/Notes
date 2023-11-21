---
Author: Vighnesh Nayak
Date: 26/10/2023
Course: Microprocessors and Automatic Controls
tags:
 - controls
---
# Laplace Transforms
---

[Fourier Series and Transforms](Fourier%20Series%20and%20Transforms.md) allows us to write.
$$F(t)=\frac{1}{2\pi}\int_{-\infty}^\infty\left(\int_\infty^\infty F(t)e^{-i\omega t}\, dt  \right)e^{i\omega t} \,dw $$
Let,
$$
\begin{equation}
	F(t)=\begin{cases}
			e^{-\gamma t}f(t), & \text{if } t\ge0\\
			0, & \text{if } t<0
		 \end{cases}
\end{equation}
$$
$$
\implies H(t)e^{-\gamma t}f(t)=\frac{1}{2\pi}\int_{-\infty}^\infty \left( \int_0^\infty e^{-(\gamma+i\omega)t}f(t)\,dt \right)e^{i\omega t}\, d\omega
$$
define $s=\gamma+i\omega$,
$$
H(t)f(t)=\frac{1}{2\pi i}\int_{\gamma-i\infty}^{\gamma+i\infty} \left(\int_0^\infty e^{-st}f(t)\, dt \right)e^{st}\,ds
$$
Therefor **Laplace Transform** is defined as,
$$
\mathcal{L}\{f(t)\}=f(s)=\int_0^\infty f(t)e^{-st}\, dt
$$
and **Inverse Laplace Transform** is defined as,
$$
\mathcal{L}^{-1}\{f(s)\}=H(t)f(t)=\frac{1}{2\pi i}\int_{\gamma-i\infty}^{\gamma+i\infty}f(s)e^{st}\,ds
$$
---
## Properties.
- Laplace and inverse Laplace Transforms are linear.
	$$ \mathcal{L}\{\alpha u(t)+v(t)\}=\alpha\mathcal{L}\{u(t)\}+\mathcal{L}\{v(t) \} $$
	$$ \mathcal{L}^{-1}\{\alpha u(t)+v(t)\}=\alpha\mathcal{L}^{-1}\{u(t)\}+\mathcal{L}^{-1}\{v(t) \} $$
- $\mathcal{L}\{u(t)*v(t)\}=\mathcal{L}\{u(t)\}\cdot\mathcal{L}\{v(t)\}$. where $*$ denotes convolution.
- $\mathcal{L}\{u(t)\cdot v(t)\}=\mathcal{L}\{u(t)\}*\mathcal{L}\{v(t)\}$.
- Similarly for inverse Laplace transform.
- Other properties are given in Laplace table.
---
## Initial value theorem.
$$f(0)= \lim_{s\to\infty}sF(s) $$
- Assuming $\lim_{t\to0}f(t)$ exists and,
- $f(t),f^{'}(t)$ are Laplace transformable. 
---
## Final value theorem.
$$f(\infty)=\lim_{s\to0}sF(s) $$
- Assuming $\lim_{t\to\infty}f(t)$ exists and,
- $f(t),f^{'}(t)$ are Laplace transformable. 
- $sF(s)$ has no pole of $j\omega$ on axis or RHP(Right Hand Plane).
---
### Proof.
$$\lim_{s\to0}\mathcal{L}\{f^{'}\}=\lim_{s\to0}\int_0^\infty f^{'}(t)e^{-st}\, dt=\lim_{s\to0}\left( sF(s)-f(0) \right) $$
$$\int_0^\infty f^{'}(t)\,dt = \lim_{s\to0}sF(s) - f(0) $$
$$f(\infty)-f(0) = \lim_{s\to0}sF(s) - f(0) $$
$$f(\infty)=\lim_{s\to0}sF(s) $$

---

