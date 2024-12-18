import re
import csv
import os

# Set input and output directories relative to the current working directory
input_dir = os.path.join(os.getcwd(), 'input')
output_dir = os.path.join(os.getcwd(), 'output')

os.makedirs(output_dir, exist_ok=True)

timestamp_pattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]"
memory_pattern = r"([A-Za-z\(\)\/]+):\s+(\d+) kB"

metrics = [
    "MemTotal", "MemFree", "Buffers", "Cached", "SwapCached", "Active", "Inactive",
    "Active(anon)", "Inactive(anon)", "Active(file)", "Inactive(file)", "SwapTotal",
    "SwapFree", "AnonPages", "Mapped", "Shmem", "CommitLimit", "Committed_AS"
]

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_metrics.csv")

        print(f"Processing file: {input_file_path}")

        with open(input_file_path, 'r') as file:
            data = file.read()

        print("Finding timestamps...")
        timestamps = re.findall(timestamp_pattern, data)

        headers = ['Timestamp'] + metrics

        with open(output_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            
            for timestamp in timestamps:
                timestamp_index = data.index(f"[{timestamp}]")
                memory_block_start = timestamp_index + len(timestamp) + 2
                memory_block_end = data.find("\n\n", memory_block_start)
                memory_block = data[memory_block_start:memory_block_end]

                print(f"Matching memory metrics for {timestamp}...")
                row = [timestamp]
                for metric in metrics:
                    match = re.search(fr"{re.escape(metric)}:\s+(\d+) kB", memory_block)
                    if match:
                        value = match.group(1)
                    else:
                        value = 'N/A'
                    row.append(value)

                print("Writing memory metrics to CSV...")
                writer.writerow(row)

        print(f"Memory metrics have been written to {output_file_path}")

print("All files have been processed.")
