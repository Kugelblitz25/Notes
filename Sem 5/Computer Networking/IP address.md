---
Author: Vighnesh Nayak
Date: 02/11/2023
Course: Computer Networking
tags: [networking]
---
# IP address
---
- Manual configuration.
---
## IPv4
- 32 bits $\rightarrow2^{32}$  unique address.
- This is not enough for current size of internet.
- *Network Address Translation (NAT)* is used to reuse IP addresses.
- **Format**: 4 8-bit *decimal* numbers separated by *decimal point*.
	- Ex: 255.255.255.255 (all 1's $\rightarrow$ reserved for broadcast).
	- 10.\*.\*.\* and 192.\*.\*.\* $\rightarrow$ private IP's.
		- These can be reused in a different private network.
- All public IP's must be unique.
- **Header**: ![Pasted image 20231102214659](/static/images/Pasted%20image%2020231102214659.png)
	- *Size* : 20 bytes.
	- *Protocol* : Type of protocol used by next layer.
		- 6 : TCP
		- 17 : UDP
		- 1 : ICMP
	- *Time To Live* : Decremented at each router. If it reaches zero delete packet. This to take care of loops.
- **Routing Table**:
	- Instead of storing individual IP's store prefix of IP's. 
	- Each network can be assigned a class of IP's.
	- *Class A* address: 8-bits network prefix + 24-bits host
	- *Class A* address: 16-bits network prefix + 16-bits host
	- *Class C* address: 24-bits network prefix + 8-bits host
- **Subnetting**: Given a slice of IP addresses of a network divide among LAN's, setup/config internal routers.
	- *Mask*: Says which bits in IP address to use to decide which LAN to route to.
- **Super-netting**: Combining several networks/ASes with similar prefix into a common prefix. Done by *Internet Service Provider (ISP)* using *CIDR*.
	- *Classless Inter Domain Routing*: Defining prefixes using arbitrary length of bits.

---
## IPv6
- 128-bits $\rightarrow2^{128}$ unique addresses. 

---
## Dynamic Host Configuration Protocol (DHCP)
