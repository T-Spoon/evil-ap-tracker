# Track marketers tracking MACs

Experiment to detect evil APs used by creepy marketers who are using a Control Frame Attack to track MAC addresses belonging to privacy entitled customers.

Control Frame Attack is a technique that neutralizes MAC address randomization.

[A Study of MAC Address Randomization in Mobile Devices and When it Fails](https://arxiv.org/pdf/1703.02874.pdf) *Jeremy Martin, Travis Mayberry, Collin Donahue, Lucas Foppe, Lamont Brown, Chadwick Riggins, Erik C. Rye, and Dane Brown*

## Hypothesis
Given 3 possible connection states:
1. Unauthenticated and unassociated
2. Authenticated and unassociated
3. Autenticated and associated

A station is under Control Frame Attack if it recieves a Request To Send (RTS)
control frame AND:
1. Not in state 3.
OR
2. Transmitter is not AP of state 3.

## Procedure
1. Identify MAC address of test target station
2. Attack station: Craft RTS frame for target MAC address via SCAPY
3. Attack station: Every 0.5s send crafted RTS frame
4. Attack station: Monitor for Clear To Send (CTS) frames which confirms
   physical presence of target station
5. Target station: Monitor RTS frames and check for condition in hypothesis
6. Target station: Walk in and out of range of Attack station.

## Results
TODO

## Conclusion
TODO
