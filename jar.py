class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies")
        if self.cookies + n > self.capacity:
            raise ValueError("Cookie jar is full")
        self.cookies += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies")
        if n > self.cookies:
            raise ValueError("Not enough cookies in the jar")
        self.cookies -= n

    @property
    def size(self):
        return self.cookies

