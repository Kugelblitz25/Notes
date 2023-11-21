---
Author: Vighnesh Nayak
Date: 01/11/2023
Course: Computer Networking
tags:
  - networking
---
# [Network Layer](Network%20Layer.md) Switching
---
- It is used for Large networks like *Internet*.
- Layer-3 Switches are also called **Routers**.
- It uses **hierarchical addressing** in the form of **[IP address](IP%20address.md)**.
- **Autonomous Systems (AS)**: a collection of IP networks and routers under the control of a single organization or entity. Each *AS* is identified by a unique *Autonomous System Number (ASN).* 
	- They internally can have any routing protocol $\to$ *[#Intra-domain routing](#Intra-domain%20routing)*.
- **Border Gateway Protocol (BGP)**: is the *[Inter-domain routing.](#Inter-domain%20routing.)* protocol used between ASes.
	- Works with *Intra-domain* routing to make *Internet* work.
	- Overall path in the *Internet* is not optimal path.

---
## Intra-domain routing.
- Classified into 2 types.
	- **[Distance Vector routing.](#Distance%20Vector%20routing.)**
		- *RIP (Routing Information Protocol)*.
	- **[Link-State routing.](#Link-State%20routing.)**
		- *OSPF (Open shortest Path First)*.
		- *IS-IS (Intermediate System to Intermediate System)*.
- Basic objective of these protocols is in a given graph of routers and **[weight of links](Choosing%20Link%20Weights..md)** find the shortest paths while avoiding loops.

---
### Distance Vector routing.
- Based on *distributed [Bellman-Ford Algorithm](Bellman-Ford%20Algorithm.md)*.
- Uses *RIP (Routing Information Protocol)*.
- Each router need to know only the next router in shortest path. 
- ![Pasted image 20231101120453](./attachments/Pasted%20image%2020231101120453.png)
- Each router send its ID and Distance to itself to all neighbours.
- A sends out: (A,0) and hears: (B,0),(F,0),(C,0).
- Routing table of A at this point is given by

	| Dest | Next hop | Cost |
	| ---- | -------- | ---- |
	| A    | -        | 0    |
	| B    | B        | 1    |
	| C    | C        | 1    |
	| F     |    F      |  1    |

- Then each router send its routing table to all neighbours.
- A hears: 
	- from B: (C,1),(A,1)
	- from C: (A,1), (D,1)
	- from F: (A,1),(G,1)
- Now all the routers update their routing tables with updated shortest paths.
	
	| Dest | Next hop | Cost |
	| ---- | -------- | ---- |
	| A    | -        | 0    |
	| B    | B        | 1    |
	| C    | C        | 1    |
	| F    | F        | 1    |
	| D    | C        | 2    |
	| G     |  F        |  2    |
- This process continues till all routers have complete routing tables.
- **Triggered Updates**: Routing updates to neighbours that are triggered by any events.
	- ex: Failure of a link triggers update with distance as infinity.
- **Periodic Updates**: Update the information about routing table to neighbours.
- **Advantages**: Simple and Easy to impliment.
- **Disadvantages**: 
	- [#Count-To-Infinity Problem (CTI)](#Count-To-Infinity%20Problem%20(CTI)) and route loops.
	- Takes time for convergence of routing tables.

---
#### Count-To-Infinity Problem (CTI)
- Since no node has the complete knowledge of the network it will create issues.
- This problem occurs when there is a network topology change, and the routing information takes time to converge to a stable state. It can lead to routing loops and incorrect routing decisions.
- Ex: ![Pasted image 20231102182840](./attachments/Pasted%20image%2020231102182840.png)
- ![Pasted image 20231102182947](./attachments/Pasted%20image%2020231102182947.png)
- In this way depending upon the timing of updates each node thinks that downed node can be reached by the other and keep incrementing the distance values till infinity.
- This will also create a loop since any packet to the downed node keeps oscillating between A and B.
- *RIP* has maximum distance value of $d_{max}$ , which if reached is considered as infinity and packet is lost. 
- For simple networks we can use [#Split-Horizon.](#Split-Horizon.) or [#Split-Horizon with Poison Reverse](#Split-Horizon%20with%20Poison%20Reverse) , they may not work for larger networks with packet loss.
---
#### Split-Horizon.
- Do not advertise information about a destination to a neighbour if that neighbour is the next hop to destination.
---
#### Split-Horizon with Poison Reverse
- A node tells its next hop to a destination that its distance to destination is $\infty$.

---
### Link-State routing.
- Each node send to all others (*broadcast*) information about cost to immediate neighbours.
- Each node has complete information about the network.
- Each node finds shortest path tree to all other nodes in the network using **[Dijkstra Algorithm.](Dijkstra%20Algorithm..md)**
- If any link fails, the nodes connected to the failed link *broadcast* this information and all nodes re-run **Dijkstra algorithm**. 
- **Advantages**:
	- No routing loops or *CTI* problems.
	- Convergence to routing tables is fast.
- **Disadvantages**: Algorithm is much more complex than *[#Distance Vector routing.](#Distance%20Vector%20routing.)*

---
## Inter-domain routing.
