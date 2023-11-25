---
Author: Vighnesh Nayak
Date: 31/10/2023
Course: Computer Networking
tags: [networking]
---
# Medium Access Control (MAC)
---
Medium Access Control (MAC) is a sublayer of the [data link layer](DLL.md) in the [OSI (Open Systems Interconnection)](OSI%20(Open%20Systems%20Interconnection)) model of network communication. The MAC layer is responsible for managing access to the shared communication medium in a network, such as a local area network (LAN) or wireless network. Its primary purpose is to coordinate and control access to the transmission medium to prevent data collisions and ensure that data is transmitted efficiently and reliably.

## Wired Medium

LAN's [^1] with bus topology does not scale well with number of nodes due to increase in frequency of collision. This problem is solved by having multiple smaller LAN's with [switches](DLL%20Switching..md) in between. Switches essentially provide scalability.

---
## Wireless Medium

---
### CSMA-CA (Carrier Sensing Multiple Access with Collision Avoidance)
![Pasted image 20231031182445](/static/images/Pasted%20image%2020231031182445.png)
- Used in Wi-Fi.
- We use Collision Avoidance since collision detection is not possible.
- **Acknowledgement (ACK)** packets are used to detect collision.
- **Hidden Terminal Problem** : occurs when a node  can communicate with a wireless access point  (AP), but cannot directly communicate with other nodes that are communicating with that AP. This leads to difficulties in medium access control sublayer since multiple nodes can send data packets to the AP simultaneously, which creates interference at the AP resulting in no packet getting through.

---
#### Virtual Carrier Sensing.
**Network Allocation Vector (NAV)** : Amount of time a node wants to use the medium. Equivalently amount of time for which medium will be busy.  The stations listening on the wireless medium read the _Duration_ field and set their NAV, which is an indicator for a station on how long it must defer from accessing the medium. The NAV may be thought of as a counter, which counts down to zero at a uniform rate. When the counter is zero, the virtual carrier-sensing indication is that the medium is idle; when nonzero, the indication is busy.

One Frame Transmission requires exchange of 4 frames.
- Frame-1 : **RTS (Request To Send)**
	- From **Sender**
	- Contains $NAV_{RTS}$ .
- Frame-2 : **CTS (Clear To Send)**
	- From **Receiver**
	- Contains $NAV_{CTS}$.
- Frame-3 : **Data Frame**
- Frame-4 : **ACK**

> **SIFS** : Short Interframe Space

After transmission of each frame there is a wait of **SIFS** to give enough time switching between **TX**^[Transmission] and **RX**^[Receiver] modes and to process each frame. 

**Exposed Terminal Problem** : When 2 *TX* nodes are exposed to each other but not to the *RX* nodes of other. 
	ex: $C\leftarrow D\quad A\rightarrow B$
$C$ is not exposed to $A$ and $D$ is not exposed to $B$.
Theoretically both $A$ and $D$ can transmit simultaneously. But using **Virtual Carrier Sensing** only one of them will transmit at a time. This leads to waste of time.

> **DIFS** : Distributed Interframe Space

After receiving *ACK* all nodes wait for **DIFS** to allow for complete processing of data. This also ensures that no node transmits between *SIFS*, since *DIFS*>*SIFS*.

**Contention Window (CW)** : A discrete time window a device must wait before attempting to transmit data on a wireless channel. The contention window is measured in time slots. It's initially set to a minimum value, often referred to as $CW_{min}$. Each time slot accounts for time delay and switch between *TX* and *RX* modes.

**Random Backoff** : Before a device transmits data, it randomly selects a backoff value within the current contention window range (between $CW_{min}$ and $CW_{max}$). This random backoff is measured in time slots as well. The randomization is used to minimize the chances of multiple devices attempting to transmit simultaneously and causing a collision.

**Channel Sensing** : The device listens to the channel and continuously checks for its availability. If the channel is busy (i.e., another device is transmitting), the device defers its transmission and continues to decrement its backoff timer.

---
#### Collision Avoidance.
If **ACK** or **CTS** is not received by sender, assume collision and **backoff** before retransmitting.



---
### OFDMA - Orthogonal Frequency Division Medium Access.
- Used in mobile networks like 4G-LTE.
- **TDMA** (Time Division Multiple Access) : non-overlapping time slots are allocated for different users for both *Uplink*^[From User to Base Station] and *Downlink*^[From Base Station to User] operation.
- **FDMA** (Frequency Division Multiple Access) : non-overlapping frequency ranges are allocated for different users for both *Uplink* and *Downlink* operation.
- **Preamble**: used for clock synchronization to base station, frame start point, attenuation, phase and delay estimation. 
- **Downlink-Uplink Map**: Mapping of time/frequency with users.
- **OFDMA** is combination of *TDMA* and *FDMA*.
	- In *downlink* frame frequency blocks in time slots are allocated to users.
	- Short gap to allow for switch of modes TX$\rightarrow$ RX.
	- Similar division for *uplink* frame.
	- Each blocks are orthogonal to each other.
- OFDMA is a multi-user, multi-carrier technology commonly used in wireless communication systems, such as Wi-Fi and 4G/5G cellular networks.
- Useful since different users may have different attenuation at different frequencies. We can allocate each user with frequency block that best suits them.
- Downlink-Uplink Map is dynamic to help mobile users.
- Only allocate block if user needs it. This can be achieved by use of **contention slots**. 
	- Contention slots are time intervals within the OFDMA frame structure during which multiple users or devices can compete for access to the shared communication channel.
	- 
- **OFDM** (Orthogonal Frequency Division Multiplexing):
	- 

---
### CDMA (Code Division Multiple Access)
- All user transmit at all times using all frequencies.
- Uses special **Spreading Function / Code**.
	- Each users are assigned different spreading codes.
	- Each codes are orthogonal to each other.
	- Users signal is multiplied by spreading code before *TX*.
	- At base station each users signal is obtained by multiplying total signal with corresponding spreading code.
- Robust to multi-path.
- Used in 3G and military communication.

[^1]: Local Area Network.
