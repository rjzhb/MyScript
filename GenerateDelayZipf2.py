import numpy as np
import csv

def zipf_generator(windowlen, a=1.0, num_samples=100):
    """
    Generate samples from a Zipf distribution with adjustable uniformity.

    Parameters:
    windowlen (int): The length of the window.
    a (float): The shape parameter (a > 0). Increase a to make the distribution more uniform.
    num_samples (int): The number of samples to generate.

    Returns:
    list: A list of randomly generated samples in the range (0, windowlen/2).
    """
    assert a > 0, "a must be greater than 0"
    assert windowlen > 0, "windowlen must be greater than 0"

    max_value = windowlen // 2
    x = np.arange(1, max_value + 1, dtype=float)
    weights = x ** (-a)
    weights /= weights.sum()

    samples = np.random.choice(x, num_samples, p=weights)

    return list(samples)


def write_csv(samples, filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['delay'])
        for sample in samples:
            csv_writer.writerow([sample])
            

# Example usage:
windowlen = 1000000
a = 1000  # Increase this value to make the distribution more uniform
num_samples = 1000000
samples = zipf_generator(windowlen, a, num_samples)

output_filename = 'zipf_distribution_1000.csv'
write_csv(samples, output_filename)


