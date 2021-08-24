#!python3
# Create a stopwatch 
import time

def main():
    counter = 0
    print("Usage: Press <Enter>: Start a new lap")
    
    lapBuffer = []
    prev_lap = None
    while True:
        command = input()
        if command.lower() == "exit":
            break
        elif command != "":
            print('Wrong key press!')
            continue

        # Setup counter and start time for first lap
        counter += 1
        if counter == 1:
            start_time = time.time()
            print(f"Started counter at {time.ctime(start_time)}, Lap: {counter}")
            continue
        # Setup a new lap
        new_lap = time.time()
        if prev_lap == None:
            lapTime = round(new_lap - start_time, 3)
        else:
            lapTime = round(new_lap - prev_lap, 3)
            
        print(f"Lap {counter}: {lapTime} seconds ", end = '')
        lapBuffer.append(lapTime)

        prev_lap = new_lap
    
    if counter == 0:
        quit()

    print(f"\nTotal time: {round(prev_lap - start_time, 3)} seconds with {counter} laps")
    print(f"Best lap: {min(lapBuffer)},  Slowest Lap: {max(lapBuffer)},   Average Lap: {round(sum(lapBuffer)/len(lapBuffer), 3)}")

if __name__ == '__main__':
    main()
