---
Author: Vighnesh Nayak
Date: 02/11/2023
Course: Computer Networking
tags: [networking]
---
# Address Resolution Protocol (ARP)
---
- Finding MAC address given IP address.
- Sits between [DLL](DLL.md) and [Network Layer](Network%20Layer.md).
- It is also sometimes considered as a sublayer of **Network Layer**.
-  *Ethernet frame*: 
	
	| Preamble | DST MAC | SRC MAC | Type | APR Packet | CRC |
	| -------- | ------- | ------- | ---- | ---------- | --- |
	| Preamble |  all 1's | SRC MAC |   0x0806   |  ARP req |CRC|

- *ARP Request*:
	 
	| Sender MAC | Sender IP | Target MAC | Target IP |
	| ---------- | --------- | ---------- | --------- |
	| $A_{MAC}$  | $A_{IP}$  | all 0's    | $B_{IP}$  |

- *ARP Response*:
	
	| Sender MAC | Sender IP | Target MAC | Target IP |
	| ---------- | --------- | ---------- | --------- |
	| $B_{MAC}$  | $B_{IP}$  | $A_{MAC}$    | $A_{IP}$  |

