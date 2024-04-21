import networkit as nk
import time
import os

# Load the graph from the txt file
graph_path = "com-youtube.ungraph.txt"
G = nk.readGraph(graph_path, nk.Format.EdgeListTabOne)

# List of CPU core counts to test (from 1 core to max cores, incrementing by 2)
# The machine from pedro fam has 8 cores 
cpu_core_counts = [1]
current_number = 1
max_cores = os.cpu_count()
while current_number < max_cores:
    current_number *= 2
    cpu_core_counts.append(current_number)


for num_threads in cpu_core_counts:
    # Set OMP_NUM_THREADS environment variable
    os.environ["OMP_NUM_THREADS"] = str(num_threads)

    # Perform label propagation
    print(f"Executing with {num_threads} threads")
    res = nk.community.detectCommunities(G)
