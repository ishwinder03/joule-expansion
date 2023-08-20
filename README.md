# joule-expansion

This code simulates the Joule expansion, whereby 2 particles in an isolated box has a partition initially of half the total volume. This is then instantenously released such that the gas does no work on expansion (dW = 0) and internal energy is just a function of temperature. The temperature and therefore total kinetic energy remain constant as displayed as the individual energies are updated. The new particle velocities are determined from conservation of momentum and energy to simulate elastic collisions.

Problems arose when many particles were used such that some of them were overlapping with the walls of the box and not bouncing back as expected. My code centered the position coordinates onto the circle and compared the distance between 2 particles with the sum of their radii. This approach was most likely not as accurate for collisions with the walls for which these walls had no well defined centre within the function.
