"""
Scenario: 3cars_Cross & Head-on
3 cars are in the cross and head-on rules

Definition for data in this scenario:
    cars_num: number of cars, int
    cars_init: initial positions of cars, array[x1,y1; x2, y2; ...]
    cars_goal: target positions of cars, array[x1,y1; x2, y2; ...]
    cars_speed(m/s): (constant) speeds of cars, array[v1; v2; ...]
    cars_head(degree): initial heading angles of cars, array[h1; h2; ...]
    (assume the spaces for all cars are same)
    ship_actions: action spaces of each ship, array[action1, action2, ...]
"""
from functions import *
cars_num = 3

cars_init = np.zeros((cars_num, 2))
cars_goal = np.zeros((cars_num, 2))
cars_speed = np.zeros((cars_num, 1))
cars_head = np.zeros((cars_num, 1))

cars_init[0, :] = np.array([5000, 0])
cars_goal[0, :] = np.array([5000, 10000])
cars_speed[0] = 20
cars_head[0] = 90

cars_init[1, :] = np.array([0, 5000])
cars_goal[1, :] = np.array([10000, 5000])
cars_speed[1] = 20
cars_head[1] = 0

cars_init[2, :] = np.array([10000, 5000])
cars_goal[2, :] = np.array([0, 5000])
cars_speed[2] = 20
cars_head[2] = 180

# actions of cars
ship_action_space = 1 # heading angle
angle_limit = 2   # heading angle changing range (-2,2)


# calculate below data based on given data
cars_given_pos = np.vstack((cars_init.reshape(-1), cars_goal.reshape(-1)))
cars_pos_min = cars_given_pos.min(0)
cars_pos_max = cars_given_pos.max(0)
cars_x_min = []
cars_y_min = []
cars_x_max = []
cars_y_max = []
cars_dis = []
for ship_idx in range(cars_num):
    cars_x_min.append(cars_pos_min[ship_idx * 2])
    cars_y_min.append(cars_pos_min[ship_idx * 2 + 1])
    cars_x_max.append(cars_pos_max[ship_idx * 2])
    cars_y_max.append(cars_pos_max[ship_idx * 2 + 1])
    cars_dis.append(euc_dist(cars_init[ship_idx, 0], cars_goal[ship_idx, 0],
                              cars_init[ship_idx, 1], cars_goal[ship_idx, 1]))
cars_dis_max = np.array(cars_dis).max(-1)
cars_vel_min = cars_speed.min(0)

if __name__ == '__main__':
    # print(cars_init)
    # print(cars_head)
    # obs = np.column_stack((cars_init, cars_head))
    # # obs = np.concatenate((cars_init, cars_head.T), axis=0)
    # print(obs)

    print(cars_given_pos)
    print(cars_x_min)
    print(cars_x_max)
    print(cars_dis_max)
    print(cars_vel_min)

    if cars_x_min[0] == cars_x_max[0]:
        print(2 * (5000 - cars_x_min[0]) / 1000 - 1)
