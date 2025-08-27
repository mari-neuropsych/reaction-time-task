import time
import random


def reaction_time_task(trials=5):
    print("Welcome! Let's test your reaction time.")
    input("Press Enter when you are ready...")

    reaction_times = []

    for trial in range(1, trials + 1):
        wait_time = random.uniform(1, 3)  # Random delay between 1 and 3 seconds
        time.sleep(wait_time)

        start_time = time.time()
        input(f"Trial {trial}: Press Enter NOW!")
        end_time = time.time()

        reaction_time = end_time - start_time
        reaction_times.append(reaction_time)
        print(f"Your reaction time: {reaction_time:.3f} seconds\n")

    average_time = sum(reaction_times) / len(reaction_times)
    print(f"Average reaction time: {average_time:.3f} seconds")


if __name__ == "__main__":
    reaction_time_task()
