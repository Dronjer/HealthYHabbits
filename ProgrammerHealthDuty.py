from time import time
import pygame
from pygame import mixer


# This program will run for indefinite period until and unless user stop it.


# Writing a function to get the current date and time
def get_time_and_date():
    import datetime
    return datetime.datetime.now()


# Writing a function to get the music start working. Initialising it first.
pygame.init()

mixer.init()


def play_music(file):
    mixer.music.load(file)
    mixer.music.play()


def stop_music():
    mixer.music.stop()


# defining 3 function to drink water, perform eye movements and do exercise.
def drink_water():
    print('Please drink water and press any key on the keyboard to stop the music')
    play_music('DrinkWater.mp3')
    with open('HealthHabitsTraking.txt', 'a') as f:
        f.write(f'{get_time_and_date()} Drank Water \n')
    a = input()
    if a:
        stop_music()


def eye_exercise():
    print('Please do some eye movements and relax. Press any key on the keyboard to stop the music')
    play_music('Eye Excercise.mp3')
    with open('HealthHabitsTraking.txt', 'a') as f:
        f.write(f'{get_time_and_date()} Exercise of Eyes Performed \n')
    c = input()
    if c:
        stop_music()


def physical_activity():
    print('Please do some physical activity and press any key on the keyboard to stop the music')
    play_music('Physical Activity.mp3')
    with open('HealthHabitsTraking.txt', 'a') as f:
        f.write(f'{get_time_and_date()} Did Physical Activity \n')
    b = input()
    if b:
        stop_music()


if __name__ == "__main__":

    # Initializing the current time for all the 3 task
    last_time_water = time()
    last_time_eye = time()
    last_time_activity = time()

    # Initializing the time period in seconds for specific tasks
    hydration = 5
    eye_time = 7
    activity_time = 13

    while True:

        if time() - last_time_water > hydration:
            drink_water()
            last_time_water = time()

        elif time() - last_time_eye > eye_time:
            eye_exercise()
            last_time_eye = time()

        elif time() - last_time_activity > activity_time:
            physical_activity()
            last_time_activity = time()
