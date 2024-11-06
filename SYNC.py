class Sync:
    def __init__(self):
        self.buffer = [None] * 10  # Buffer with 10 slots
        self.mutex = 1  # Mutex to control access to buffer
        self.empty = 10  # Number of empty slots
        self.full = 0  # Number of full slots
        self.in_index = 0  # Next slot to place produced item
        self.out_index = 0  # Next slot to consume item from
    def wait(self, x):
        return x - 1 if x > 0 else 0  # Decrease semaphore value but not below 0
    def signal(self, x):
        return x + 1  # Increase semaphore value
    def producer(self):
        if self.empty > 0 and self.mutex == 1:  # Check if there's space in buffer
            self.empty = self.wait(self.empty)  # Lock empty slot
            self.mutex = self.wait(self.mutex)  # Lock buffer
            self.buffer[self.in_index] = int(input("Produce data: "))  # Produce item
            self.in_index = (self.in_index + 1) % 10  # Move to next index
            self.mutex = self.signal(self.mutex)  # Unlock buffer
            self.full = self.signal(self.full)  # Increase full slots
        else:
            print("Buffer is full!")
    def consumer(self):
        if self.full > 0 and self.mutex == 1:  # Check if there's data to consume
            self.full = self.wait(self.full)  # Lock full slot
            self.mutex = self.wait(self.mutex)  # Lock buffer
            print(f"Consumed: {self.buffer[self.out_index]}")  # Consume item
            self.out_index = (self.out_index + 1) % 10  # Move to next index
            self.mutex = self.signal(self.mutex)  # Unlock buffer
            self.empty = self.signal(self.empty)  # Increase empty slots
        else:
            print("Buffer is empty!")
if __name__ == "__main__":
    sync = Sync()  # Create Synchronization instance
    while True:
        choice = int(input("1. Producer\n2. Consumer\n3. Exit\nEnter choice: "))  # User menu
        if choice == 1:
            sync.producer()  # Call producer
        elif choice == 2:
            sync.consumer()  # Call consumer
        elif choice == 3:
            break  # Exit loop
        else:
            print("Invalid choice!")  # Invalid input
