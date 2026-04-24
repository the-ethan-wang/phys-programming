# blocks, strings, and pulleys

Simple block, strings, and pulley systems  

Missing pulleys and block+string+gravity systems

Tested against my solutions, they work for the questions in the worksheet.

Objects are given from left to right, and positive direction is right.

For block+string+gravity, objects are given bottom to top, positive direction is up.

## Sample output

### Block systems

```
-------------------Sample block-------------------
Net acceleration of system: 10.00ms^-2
Net force of system: 10.00N
Forces on each block:
Block 1 | 1.00Kg | 10.00N | Applied: 10.00N, Contact Reaction: 0.00N


--------------------Question 1--------------------
Net acceleration of system: 6.00ms^-2
Net force of system: 48.00N
Forces on each block:
Block 1 | 3.00Kg | 18.00N | Applied: 48.00N, Contact Reaction: -30.00N
Block 2 | 5.00Kg | 30.00N | Contact: 30.00N


--------------------Question 2--------------------
Net acceleration of system: -6.00ms^-2
Net force of system: -48.00N
Forces on each block:
Block 1 | 3.00Kg | -18.00N | Contact: -18.00N
Block 2 | 5.00Kg | -30.00N | Applied: -48.00N, Contact Reaction: 18.00N


--------------------Question 3--------------------
Net acceleration of system: 8.00ms^-2
Net force of system: 112.00N
Forces on each block:
Block 1 | 2.00Kg | 16.00N | Applied: 112.00N, Contact Reaction: -96.00N
Block 2 | 4.00Kg | 32.00N | Contact: 96.00N, Contact Reaction: -64.00N
Block 3 | 8.00Kg | 64.00N | Contact: 64.00N


--------------------Question 4--------------------
Net acceleration of system: -3.00ms^-2
Net force of system: -33.00N
Forces on each block:
Block 1 | 7.00Kg | -21.00N | Contact: -21.00N
Block 2 | 4.00Kg | -12.00N | Applied: -33.00N, Contact Reaction: 21.00N


--------------------Question 5--------------------
Net acceleration of system: 5.00ms^-2
Net force of system: 40.00N
Forces on each block:
Block 1 | 3.00Kg | 15.00N | Applied: 40.00N, Contact Reaction: -25.00N
Block 2 | 5.00Kg | 25.00N | Contact: 25.00N
--------------------------------------------------
```

### Block + String systems

```
--------------------Question 1--------------------
Net acceleration of system: 4.00ms^-2
Net force of system: 160.00N
Forces on each block:
Block 1 | 15.00Kg | 60.00N | Tension: 60.00N
Block 2 | 25.00Kg | 100.00N | Applied: 160.00N, Tension: -60.00N


--------------------Question 2--------------------
Net acceleration of system: -8.00ms^-2
Net force of system: -96.00N
Forces on each block:
Block 1 | 8.00Kg | -64.00N | Applied: -96.00N, Tension: 32.00N
Block 2 | 4.00Kg | -32.00N | Tension: -32.00N


--------------------Question 3--------------------
Net acceleration of system: -3.00ms^-2
Net force of system: -150.00N
Forces on each block:
Block 1 | 14.00Kg | -42.00N | Applied: -150.00N, Tension: 108.00N
Block 2 | 6.00Kg | -18.00N | Tension: -108.00N, Tension: 90.00N
Block 3 | 30.00Kg | -90.00N | Tension: -90.00N


--------------------Question 4--------------------
Net acceleration of system: 6.00ms^-2
Net force of system: 156.00N
Forces on each block:
Block 1 | 12.00Kg | 72.00N | Tension: 72.00N
Block 2 | 6.00Kg | 36.00N | Tension: -72.00N, Tension: 108.00N
Block 3 | 8.00Kg | 48.00N | Applied: 156.00N, Tension: -108.00N


--------------------Question 5--------------------
Net acceleration of system: 0.25ms^-2
Net force of system: 6.25N
Forces on each block:
Block 1 | 4.00Kg | 1.00N | Tension: 1.00N
Block 2 | 3.00Kg | 0.75N | Tension: -1.00N, Tension: 1.75N
Block 3 | 12.00Kg | 3.00N | Tension: -1.75N, Tension: 4.75N
Block 4 | 6.00Kg | 1.50N | Applied: 6.25N, Tension: -4.75N
--------------------------------------------------
```

### Block + String + Gravity systems

```
uhhh WIP
```