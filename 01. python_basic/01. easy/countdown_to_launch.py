from time import sleep

countdown_timer = int(input("Enter a number for the countdown to launch: "))

while countdown_timer > 0:
    print(countdown_timer)
    sleep(1)
    countdown_timer -= 1

print("Launch!")