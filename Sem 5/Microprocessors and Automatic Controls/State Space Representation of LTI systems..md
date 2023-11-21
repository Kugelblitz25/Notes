---
Author: Vighnesh Nayak
Date: 26/10/2023
Course: Microprocessors and Automatic Controls
tags:
 - controls
---
# State Space Representation of LTI systems.
---

The state $x(t_0)$ of a system at time $t_0$ is the information at $t_0$ that, together with the input $u(t)$, for $t\ge t_0$, determines uniquely the output $y(t)$ for all $t\ge t_0$.

A general LTI system can be represented by.
$$\dot{x}(t)=Ax(t)+Bu(s)$$
$$y(t)=Cx(t)+Du(t)$$
where $x,u,y$ are vectors and $A,B,C,D$ are matrices of appropriate dimensions.

Using [Laplace Transforms](Laplace%20Transforms.md),
$$sx(s)-x(0) = Ax(s)+Bu(s) $$
$$y(s)=Cx(s)+Du(s) $$
Rearranging we get,
$$x(s)=\left(sI-A\right)^{-1}x(0)+\left(sI-A\right)^{-1}Bu(s) $$
$$y(s)=C\left(sI-A\right)^{-1}x(0)+C\left(sI-A\right)^{-1}Bu(s)+Du(s)  $$
For zero-state response, $x(0)=0$.

---
