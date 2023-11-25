---
Author: Vighnesh Nayak
Date: 01/11/2023
Course: Computer Networking
tags: ["#networking"]
---
# [DLL](DLL.md) Switching.
---
- This is used by [](Medium%20Access%20Control%20(MAC).md#Wired%20Medium|Ethernets) and use **MAC** addresses to switch.
- Switches connect multiple smaller bus topology LAN's^[Local Area Networks] from their ports.
	- They are also called as bridges.
	- They make use of **[forwarding tables](#Forwarding%20tables.)** for this task.
	- Forwarding tables are created dynamically during operation.
- If there is a loop in the network connected by multiple switches, since initially forwarding tables are empty, all the switches in the network forward the frames to all the ports. This creates an infinite loop.
	- ![Pasted image 20231101022155](/static/images/Pasted%20image%2020231101022155.png)
	- To mitigate this issue and break the loop **[Spanning Tree Protocol](#Spanning%20Tree%20Protocol)** is used.
	- This converts the Graph created by LAN's to a spanning tree by disabling some of the ports while keeping all the LAN's connected.
	- ![Pasted image 20231101023743](/static/images/Pasted%20image%2020231101023743.png)

---
## Forwarding tables.
- All ports and devices have unique *MAC* address.
- Initially the forwarding table is empty.
	- Whenever a frame reaches switch, switch populates the forwarding table with port on which source is located.
	- By default, if destination's port is not known, switch forwards the frame to all ports.
	- If destination's port is already known, then frame is forwarded to appropriate port (not forwarded in case destination is on the same port as source).
	- To address the problem of nodes changing the networks they are on, we use expiration time.
		- Each entry in forwarding table has a expiration time.
		- If the switch hear from the node from on same port as the entry in forwarding table before expiration, the expiration time is extended.
		- If the switch hear from the node from on different port as the entry in forwarding table before expiration, the table and expiration time are updated.
		- If the switch does not hear from the node before expiration, the entry in table is removed.

---
## Spanning Tree Protocol^[Created by Radia Perlman].
- Elect a *root switch*.
	- Switch with lowest *Bridge ID* is elected.
		- By default all bridges have same ID=32768. 
		- Range: 0-61440 in multiples of 4096.
	- Each bridge send message of the format (Y,D,X) to all its neighbours during election.
		- Y: smallest ID heard till now.
		- D: its distance from Y.
		- X: its ID
	- All bridges update their current *root* switch, and repeat.
	- Eventually all converge on single root.
- Each bridge finds which port is closest to root and assigns this port as *Root port*. A *tie-braking* rule exists for equidistant ports.
	- During election keep track of port from which *root* switch was heard.
	- *Tie braker*: ID.
- Among all switches connected to a LAN, elect one among them to forward frames on that LAN and mark corresponding as *Designated port*.
	- Choose switch with smallest distance to *root*.
- Disable any port that is not a *Root* or *Designated* port.  
---
## Shortcomings.
It's difficult to scale the networks using DLL switches due to following issues.
- Path is not optimal (shortest path).
- It's not using some links $\to$ poor resource utilization.
- Forwarding table is of the order O(N). This is problem for very large networks due to slow lookups and large space required to store the forwarding table.
	- The slow lookup is due to flat addressing.
- If any of the switches fail, we need to restart *spanning tree protocol*(STP).
	- To determine if any switch is down we need have periodic "Hello" messages from root.
	- Larger the network, more frequent STP reconstructions. 
	- STP is non trivial takes significant amount of resources.
- No common addressing schemes or common communication protocols.

To address these issues in larger networks like *Internet* we use [Network Layer Switching](Network%20Layer%20Switching.md).


