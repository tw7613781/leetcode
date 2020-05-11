import random
import time

def random_walk(n):
    '''
    return the distance abs(x) + abs(y) after n random walk on a 2-d map
    '''
    x, y = 0, 0
    for i in range(n):
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        x += dx
        y += dy
    distance = abs(x) + abs(y)
    return distance

if __name__ == '__main__':
    '''
    if the distance is less or equal than 4, the man needn't take transport home 
    '''
    walk_length = 30
    sample_size = 100000
    for step in range(1, walk_length):
        tick = time.perf_counter()
        no_of_no_transport = 0
        for i in range(sample_size):
            distance = random_walk(step)
            if distance <= 4:
                no_of_no_transport += 1
        percentage = float(no_of_no_transport / sample_size) * 100
        print(f'walk_lenth is {step}, the rate of no_transportation is {percentage}')
        tock = time.perf_counter()
        print(f'walk_length: {step} - simple size: {sample_size} - time consume: {1e3*(tock-tick):.6f} ms')
    
        
