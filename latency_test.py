import requests
import time

api_url = 'http://127.0.0.1:5000/random_decimal'


num_requests = 100

# Initialize empty list to store latencies
latencies = []

for _ in range(num_requests):
  start_time = time.time()
  response = requests.get(api_url)
  response.raise_for_status()  # Raise exception for non-2xx status codes
  end_time = time.time()

  latency = (end_time - start_time) * 1000  # Convert to milliseconds
  latencies.append(latency)

# Calculate and print summary statistics (optional)
average_latency = sum(latencies) / len(latencies)
print(f"Average latency: {average_latency:.2f} ms")
print(f"Minimum latency: {min(latencies):.2f} ms")
print(f"Maximum latency: {max(latencies):.2f} ms")