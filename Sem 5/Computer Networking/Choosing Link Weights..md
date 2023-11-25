---
Author: Vighnesh Nayak
Date: 02/11/2023
Course: Computer Networking
tags: [networking]
---
# Choosing Link Weights.
---
 ## Using latency:
- latency=queuing delay + speed of light delay + transmission delay
- Calculate the average latency of a link over a time window.
- **Problems**:
	- Oscillations of link weights under heavy load due to variations in queuing delays.
		- This causes rapid changes in paths which may also cause reordering of packets.
		- May create routing loop due to rapid changes in paths.
	- Large range of link weights due to which some links get penalized (due to high weights) too much.
	- Satellite links are penalized too much due to large distance.
---
## By Utilization.
![Pasted image 20231102195317](/static/images/Pasted%20image%2020231102195317.png)

- Terrestrial links are preferred to satellite links with same speed.
---
## OSPF.
$$\text{Weight}=\max\left(\frac{10^8}{\text{link speed(bps)}},1\right)$$

---
## Manual by Network Operation Center (NOC).

