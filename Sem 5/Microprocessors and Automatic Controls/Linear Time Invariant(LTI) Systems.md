---
Author: Vighnesh Nayak
Date: 26/10/2023
Course: Microprocessors and Automatic Controls
tags: [controls]
---
# Linear Time Invariant(LTI) Systems
---

Control Systems can be
- **SISO**:
- **MIMO**:
- **Memoryless** systems: the current output only depends upon current input (independent of future and past inputs.)
- **Systems with memory**: The current output depends upon past, current and, future inputs.
- **Causal** systems: The current output depends upon past and current inputs only.
	$$
	\begin{equation}
		\left\{ \begin{array}{lr}
			x(t_0)\\
			u(t),\quad t\ge t_0
		\end{array}
		\right\}\to y(t),\quad t\ge t_0
	\end{equation}
	$$
	- where $x(t_0)$ is the [ state of system](State%20Space%20Representation%20of%20LTI%20systems..md) at $t_0$.
- **Lumped** System: Number of [state variables](State%20Space%20Representation%20of%20LTI%20systems..md) is **finite**.
- **Distributed** System: Number of [state variables](State%20Space%20Representation%20of%20LTI%20systems..md) if **infinite**.
- **Linear** Systems: A system is said to be linear if for any given 2 input-state-output combinations following holds true.
	$$
	\begin{equation}
		\left\{ \begin{array}{lr}
			\alpha x_1(t_0)+x_2(t_0)\\
			\alpha u_1(t)+u_2(t),\quad t\ge t_0
		\end{array}
		\right\}\to \alpha y_1(t)+y_2(t),\quad t\ge t_0
	\end{equation}
	$$
- **Time-Invariant** System: A system is said to be linear if for every input-state-output combination following holds true.
	$$
	\begin{equation}
		\left\{ \begin{array}{lr}
			x(t_0+T)\\
			u(t-T),\quad t\ge t_0+T
		\end{array}
		\right\}\to y(t-T),\quad t\ge t_0+T
	\end{equation}
	$$
- A system is said to be **relaxed** at $t_0$ if $x(t_0)=0$. In this case $y(t)$ depends only on $u(t),t\ge t_0$.
---
## Input-Output description
Let $\delta_\Delta(t-t_i)$ be a pulse located at time $t_i$ with a unit area (as the pulse-width goes to zero it will become a Dirac-delta function). Using these pulses any general input over the entire time axis can be approximated as,
$$u(t) = \sum_i \delta_\Delta(t-t_i) u(t_i)\Delta $$
Let $g_\Delta(t,t_i)$ be the output of $\delta_\Delta(t-t_i)$,
$$\implies \delta_\Delta(t-t_i)\to g_\Delta(t,t_i) $$

---
## Linear Time-Invariant systems.
$$\delta_\Delta(t-t_i)u(t_i)\Delta\to g_\Delta(t,t_i)u(t_i)\Delta $$
$$\sum_i\delta_\Delta(t-t_i)u(t_i)\Delta\to \sum_i g_\Delta(t,t_i)u(t_i)\Delta $$
$$u(t)\approx\delta_\Delta(t-t_i)u(t_i)\Delta\to g_\Delta(t,t_i)u(t_i)\Delta\approx y(t) $$
$$y(t)\approx\sum_ig_\Delta(t,t_i)u(t_i)\Delta $$
As $\Delta\to0$ , Summation converts to integral and $g_\Delta\to g$.
$$y(t)=\int_{-\infty}^\infty g(t,\tau)u(\tau)\,d\tau $$
Using causality and relaxed system at $t=t_0$.
$$y(t)=\int_{t_0}^t g(t,\tau)u(\tau)\,d\tau $$
Using Time-Invariance $g(t,\tau)=g(t-T,\tau-T)=g(t-\tau,0)=g(t-\tau),$ and $t_0=0$.
$$y(t)=\int_0^tg(t-\tau)u(\tau)\,d\tau $$
$$\implies y(t)=g(t)*u(t) $$
where $*$ denotes convolution.
Taking [Laplace Transforms](Laplace%20Transforms.md) of $y(t)$.
$$y(s)=G(s)u(s) $$
$G(s)$ is called the [Transfer Functions](Transfer%20Functions.md) of LTI system.

---
### Steady state response for complex exponential input.
$$u(t)=e^{j\omega t} $$
$$y(t)=\int_0^tg(\tau)e^{j\omega (t-\tau)}\,d\tau $$
$$y(t)=e^{j\omega t}\int_0^t g(\tau)e^{-j\omega\tau}\,d\tau $$
If we redefine $g(t)$ to be zero outside $(0,t)$,
$$y(t)=e^{j\omega t}\int_{-\infty}^{\infty}g(\tau)e^{-j\omega \tau} $$
$$y(t)=G(\omega)e^{j\omega t} $$
where $G(\omega)$ is the [Fourier Transform](Fourier%20Series%20and%20Transforms.md) of impulse response.
Hence, the interpretation is that for an LTI system if the input is a sinusoid, the output is a sinusoid of the same frequency with amplitude scaled by magnitude of $G(\omega)$ and phase shifted by phase of $G(\omega)$.  

---
