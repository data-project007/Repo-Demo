#This code is written by me.

# Print odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(f"Odd number found: {i}")

logging.info(f"Initialized OddNumberGenerator with limit: {self.limit}")

    def use_standard_loop(self):
        """Classic approach using a for-loop and if-statement."""
        odds = []
        for i in range(self.limit + 1):
            if i % 2 != 0:
                odds.append(i)
        return odds

    def use_list_comprehension(self):
        """The Pythonic way: compact and efficient."""
        return [i for i in range(self.limit + 1) if i % 2 != 0]

    def use_filter_lambda(self):
        """Functional programming approach using filter and lambda."""
        return list(filter(lambda x: x % 2 != 0, range(self.limit + 1)))

    def use_step_parameter(self):
        """The most efficient way: letting range do the work."""
        return list(range(1, self.limit + 1, 2))

def display_results(method_name, data):
    """Helper function to format the output."""
    print(f"\n--- Method: {method_name} ---")
    print(f"Result: {data}")
    print(f"Total Count: {len(data)}")
