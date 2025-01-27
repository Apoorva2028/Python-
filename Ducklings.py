import random, time, shutil, sys

# Constants:
PAUSE = 0.2
DENSITY = 0.2
DUCKLING_WIDTH = 5
WIDTH = shutil.get_terminal_size()[0] - 1  # Terminal width

HEADS = ['>', '=', '<']  # Open, closed, or left-facing
EYES = ['"', '\'', '^^', '``']
WINGS = ['>', '^', 'v', '<']
FEET = [' ^^ ', ' ^ ^ ']
BODIES = [' ', '  ']  # Chubby and very chubby

class Duckling:
    def __init__(self, randomize=True, head=None, eyes=None, body=None, wing=None, feet=None):
        """Create a duckling with random or specific features."""
        if randomize:
            self.head = random.choice(HEADS)
            self.eyes = random.choice(EYES)
            self.body = random.choice(BODIES)
            self.wing = random.choice(WINGS)
            self.feet = random.choice(FEET)
        else:
            self.head = head
            self.eyes = eyes
            self.body = body
            self.wing = wing
            self.feet = feet

    def __str__(self):
        """Return the duckling's full appearance as a string."""
        return f"{self.head}{self.eyes}({self.body}{self.wing}{self.body}){self.feet}"


def generate_ducklings():
    """Generate and display ducklings on the screen."""
    duckling_lanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:
        for lane_num, duckling in enumerate(duckling_lanes):
            if duckling is None and random.random() < DENSITY:
                # Create a new random duckling:
                duckling_lanes[lane_num] = Duckling()

            if duckling is not None:
                # Display the duckling:
                print(str(duckling).ljust(DUCKLING_WIDTH), end='')
                # Remove the duckling once displayed:
                duckling_lanes[lane_num] = None
            else:
                # Print empty space if no duckling:
                print(' ' * DUCKLING_WIDTH, end='')

        print()  # Newline for the next row
        sys.stdout.flush()
        time.sleep(PAUSE)


def main():
    print("Duckling Screensaver (Press Ctrl+C to quit)")
    time.sleep(1)
    try:
        generate_ducklings()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
