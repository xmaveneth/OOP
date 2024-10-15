class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        result = self.clock1.get_time() - self.clock2.get_time()
        if result < 0:
            return "00: 00: 00"
        hours = result // 3600
        minutes = (result - hours * 3600) // 60
        seconds = result % 60
        return f"{str(hours).rjust(2, '0')}: {str(minutes).rjust(2, '0')}: {str(seconds).rjust(2, '0')}"

    def __len__(self):
        result = self.clock1.get_time() - self.clock2.get_time()
        if result < 0:
            return 0
        return result

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)