import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 8))

# Define the properties of the balls
BOX_WIDTH = 10
BOX_HEIGHT = 10
ball_1_position = np.array([2, 2])
ball_1_velocity = np.array([3, -2.8])
ball_2_position = np.array([4, 7])
ball_2_velocity = np.array([-14, 7])
m1 = 10
m2 = 100
radius1 = 0.7
radius2 = 1.3
BALL_RADIUS = radius1 + radius2

# Constants used for velocity updates after collisions
a = (m1 - m2) / (m1 + m2)
b = 2 * m2 / (m1 + m2)
c = 2 * m1 / (m1 + m2)
dt = 0.01

# Collision conditions
def collide(position1, position2):
    distance = np.linalg.norm(position1 - position2)
    return distance < 2.2

def update_velocity(velocity1, velocity2):
    new_velocity1 = a * velocity1 + b * velocity2
    new_velocity2 = c * velocity1 - a * velocity2
    return new_velocity1, new_velocity2

def update_position(position, velocity, radius, wall_removed):
    new_position = position + velocity * dt
    for i in range(2):
        if new_position[i] - radius < 0 or new_position[i] + radius > (BOX_WIDTH, BOX_HEIGHT)[i]:
            velocity[i] *= -1
    if not wall_removed:
        if new_position[0] + radius > BOX_WIDTH / 2 and position[0] + radius <= BOX_WIDTH / 2:
            velocity[0] *= -1
    return new_position, velocity

ax = fig.add_subplot(111, aspect='equal')

wall_removed = False

for i in range(1000):
    if i == int(5 / dt):
        wall_removed = True

    ax.set_xlim(0, BOX_WIDTH)
    ax.set_ylim(0, BOX_HEIGHT)

    ball1 = plt.Circle(ball_1_position, radius1, color = 'orange')
    ball2 = plt.Circle(ball_2_position, radius2, color = 'blue')
    ax.add_artist(ball1)
    ax.add_artist(ball2)

    ball_1_position, ball_1_velocity = update_position(ball_1_position, ball_1_velocity, radius1, wall_removed)
    ball_2_position, ball_2_velocity = update_position(ball_2_position, ball_2_velocity, radius2, wall_removed)

    if collide(ball_1_position, ball_2_position):
        ball_1_velocity, ball_2_velocity = update_velocity(ball_1_velocity, ball_2_velocity)

    ball1.set_center(ball_1_position)
    ball2.set_center(ball_2_position)

    if not wall_removed:
        ax.axvline(BOX_WIDTH / 2, color='red')

    E1 = 1/2 * m1 * (ball_1_velocity[0]**2 + ball_1_velocity[1]**2)
    E2 = 1/2 * m2 * (ball_2_velocity[0]**2 + ball_2_velocity[1]**2)
    ax.text(0.5, 10.5, f'KE red = {round(E1,3)}\n KE blue = {round(E2,3)}\n total KE = {round(E1+E2,3)}', bbox=dict(facecolor='green', alpha=0.5))
    plt.pause(0.01)
    ax.clear()

plt.show()
