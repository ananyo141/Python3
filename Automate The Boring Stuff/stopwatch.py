#!python3
# Create a stopwatch 
import time

def main():
    counter = 0
    print("Usage: Press <Enter>: Start a new lap\n"
                "Type 'exit': to stop")
    
    lapBuffer = []      # contain lap details
    prev_lap = None
    while True:
        # manage input
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
            print(f"Started counter at {time.ctime(start_time)}, Lap: # {counter}")
            continue
        # Setup a new lap
        new_lap = time.time()
        if prev_lap == None:
            lapTime = round(new_lap - start_time, 3)
        else:
            lapTime = round(new_lap - prev_lap, 3)
            
        # print each lap details
        print(f"Lap # %-4d: %7.3f seconds (%5.2f) " % (counter, new_lap - start_time, lapTime), end='')
        lapBuffer.append(lapTime)
        prev_lap = new_lap
    
    # quit if not enough data to calculate statistics
    if counter <= 1:
        print("Not enough data (laps)")
        quit()

    print(f"\nTotal time: {round(prev_lap - start_time, 3)} seconds with {counter} laps")
    print(f"Best lap: {min(lapBuffer)},  Slowest Lap: {max(lapBuffer)},   "
          f"Average Lap: {round(sum(lapBuffer)/len(lapBuffer), 3)}")

if __name__ == '__main__':
    main()
