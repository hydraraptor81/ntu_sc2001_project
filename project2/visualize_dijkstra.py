# visualize_dijkstra.py
import matplotlib.pyplot as plt
import csv
import os

def plot_dijkstra_comparison(results, output_dir="plots"):
    """
    Plot comparison graphs for Dijkstra's algorithm implementations

    Args:
        results: List of dictionaries with keys:
                 'type', 'v_count', 'e_count', 'matrix_avg_time', 
                 'heap_avg_time', 'matrix_avg_operations', 'heap_avg_operations'
        output_dir: Directory to save plots and CSVs
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Separate results by type
    sparse_results = [r for r in results if r['type'] == 'sparse']
    dense_results = [r for r in results if r['type'] == 'dense']
    fixed_v_results = [r for r in results if r['type'] == 'fixed_v']

    # Save to CSV
    with open(f"{output_dir}/dijkstra_results.csv", 'w', newline='') as csvfile:
        fieldnames = ['type', 'v_count', 'e_count', 'matrix_avg_time', 
                     'heap_avg_time', 'matrix_avg_operations', 'heap_avg_operations']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

    # Part (a) Graphs - Adjacency Matrix Implementation
    # Graph 1: Adjacency Matrix - Sparse vs Dense varying |V| (time)
    if sparse_results and dense_results:
        # Match by v_count
        sparse_dict = {r['v_count']: r for r in sparse_results}
        dense_dict = {r['v_count']: r for r in dense_results}
        common_v = sorted(set(sparse_dict.keys()) & set(dense_dict.keys()))

        if common_v:
            sparse_times = [sparse_dict[v]['matrix_avg_time'] for v in common_v]
            dense_times = [dense_dict[v]['matrix_avg_time'] for v in common_v]

            plt.figure(figsize=(10, 6))
            plt.plot(common_v, sparse_times, 'o-', label='Sparse Graphs', linewidth=2, markersize=8)
            plt.plot(common_v, dense_times, 's-', label='Dense Graphs', linewidth=2, markersize=8)
            plt.xlabel('|V| (Number of Vertices)')
            plt.ylabel('Average Time (seconds)')
            plt.title('Part (a): Adjacency Matrix Implementation\nSparse vs Dense Graphs - Varying |V|')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.savefig(f"{output_dir}/part_a_matrix_sparse_vs_dense_time.png", dpi=300, bbox_inches='tight')
            plt.close()

            # Operations count
            sparse_ops = [sparse_dict[v]['matrix_avg_operations'] for v in common_v]
            dense_ops = [dense_dict[v]['matrix_avg_operations'] for v in common_v]

            plt.figure(figsize=(10, 6))
            plt.plot(common_v, sparse_ops, 'o-', label='Sparse Graphs', linewidth=2, markersize=8)
            plt.plot(common_v, dense_ops, 's-', label='Dense Graphs', linewidth=2, markersize=8)
            plt.xlabel('|V| (Number of Vertices)')
            plt.ylabel('Average Number of Operations')
            plt.title('Part (a): Adjacency Matrix Implementation\nSparse vs Dense Graphs - Varying |V| (Operations)')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.savefig(f"{output_dir}/part_a_matrix_sparse_vs_dense_operations.png", dpi=300, bbox_inches='tight')
            plt.close()

    # Part (b) Graphs - Adjacency List + Heap Implementation
    # Graph 2: Adjacency List - Sparse vs Dense varying |V| (time)
    if sparse_results and dense_results:
        # Match by v_count
        sparse_dict = {r['v_count']: r for r in sparse_results}
        dense_dict = {r['v_count']: r for r in dense_results}
        common_v = sorted(set(sparse_dict.keys()) & set(dense_dict.keys()))

        if common_v:
            sparse_times = [sparse_dict[v]['heap_avg_time'] for v in common_v]
            dense_times = [dense_dict[v]['heap_avg_time'] for v in common_v]

            plt.figure(figsize=(10, 6))
            plt.plot(common_v, sparse_times, 'o-', label='Sparse Graphs', linewidth=2, markersize=8)
            plt.plot(common_v, dense_times, 's-', label='Dense Graphs', linewidth=2, markersize=8)
            plt.xlabel('|V| (Number of Vertices)')
            plt.ylabel('Average Time (seconds)')
            plt.title('Part (b): Adjacency List + Heap Implementation\nSparse vs Dense Graphs - Varying |V|')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.savefig(f"{output_dir}/part_b_heap_sparse_vs_dense_v_time.png", dpi=300, bbox_inches='tight')
            plt.close()

            # Operations count
            sparse_ops = [sparse_dict[v]['heap_avg_operations'] for v in common_v]
            dense_ops = [dense_dict[v]['heap_avg_operations'] for v in common_v]

            plt.figure(figsize=(10, 6))
            plt.plot(common_v, sparse_ops, 'o-', label='Sparse Graphs', linewidth=2, markersize=8)
            plt.plot(common_v, dense_ops, 's-', label='Dense Graphs', linewidth=2, markersize=8)
            plt.xlabel('|V| (Number of Vertices)')
            plt.ylabel('Average Number of Operations')
            plt.title('Part (b): Adjacency List + Heap Implementation\nSparse vs Dense Graphs - Varying |V| (Operations)')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.savefig(f"{output_dir}/part_b_heap_sparse_vs_dense_v_operations.png", dpi=300, bbox_inches='tight')
            plt.close()

    # Graph 3: Adjacency List - Fixed |V| varying |E| (time)
    if fixed_v_results:
        e_counts = [r['e_count'] for r in fixed_v_results]
        heap_times = [r['heap_avg_time'] for r in fixed_v_results]

        plt.figure(figsize=(10, 6))
        plt.plot(e_counts, heap_times, 'o-', linewidth=2, markersize=8)
        plt.xlabel('|E| (Number of Edges)')
        plt.ylabel('Average Time (seconds)')
        plt.title(f'Part (b): Adjacency List + Heap Implementation\nFixed |V|={fixed_v_results[0]["v_count"]} - Varying |E|')
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/part_b_heap_fixed_v_varying_e_time.png", dpi=300, bbox_inches='tight')
        plt.close()

        # Operations count
        heap_ops = [r['heap_avg_operations'] for r in fixed_v_results]

        plt.figure(figsize=(10, 6))
        plt.plot(e_counts, heap_ops, 'o-', linewidth=2, markersize=8)
        plt.xlabel('|E| (Number of Edges)')
        plt.ylabel('Average Number of Operations')
        plt.title(f'Part (b): Adjacency List + Heap Implementation\nFixed |V|={fixed_v_results[0]["v_count"]} - Varying |E| (Operations)')
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/part_b_heap_fixed_v_varying_e_operations.png", dpi=300, bbox_inches='tight')
        plt.close()

    # Part (c) Graphs - Comparing Matrix vs Heap Implementations
    # Graph 4: Matrix vs Heap - Sparse graphs varying |V|
    if sparse_results:
        v_counts = [r['v_count'] for r in sparse_results]
        matrix_times = [r['matrix_avg_time'] for r in sparse_results]
        heap_times = [r['heap_avg_time'] for r in sparse_results]

        plt.figure(figsize=(10, 6))
        plt.plot(v_counts, matrix_times, 'o-', label='Adjacency Matrix', linewidth=2, markersize=8)
        plt.plot(v_counts, heap_times, 's-', label='Adjacency List + Heap', linewidth=2, markersize=8)
        plt.xlabel('|V| (Number of Vertices)')
        plt.ylabel('Average Time (seconds)')
        plt.title('Part (c): Implementation Comparison\nSparse Graphs - Varying |V|')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/part_c_sparse_varying_v_time.png", dpi=300, bbox_inches='tight')
        plt.close()

        # Operations count
        matrix_ops = [r['matrix_avg_operations'] for r in sparse_results]
        heap_ops = [r['heap_avg_operations'] for r in sparse_results]

        plt.figure(figsize=(10, 6))
        plt.plot(v_counts, matrix_ops, 'o-', label='Adjacency Matrix', linewidth=2, markersize=8)
        plt.plot(v_counts, heap_ops, 's-', label='Adjacency List + Heap', linewidth=2, markersize=8)
        plt.xlabel('|V| (Number of Vertices)')
        plt.ylabel('Average Number of Operations')
        plt.title('Part (c): Implementation Comparison\nSparse Graphs - Varying |V| (Operations)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/part_c_sparse_varying_v_operations.png", dpi=300, bbox_inches='tight')
        plt.close()

    # Graph 5: Matrix vs Heap - Dense graphs varying |V|
    if dense_results:
        v_counts = [r['v_count'] for r in dense_results]
        matrix_times = [r['matrix_avg_time'] for r in dense_results]
        heap_times = [r['heap_avg_time'] for r in dense_results]

        plt.figure(figsize=(10, 6))
        plt.plot(v_counts, matrix_times, 'o-', label='Adjacency Matrix', linewidth=2, markersize=8)
        plt.plot(v_counts, heap_times, 's-', label='Adjacency List + Heap', linewidth=2, markersize=8)
        plt.xlabel('|V| (Number of Vertices)')
        plt.ylabel('Average Time (seconds)')
        plt.title('Part (c): Implementation Comparison\nDense Graphs - Varying |V|')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/part_c_dense_varying_v_time.png", dpi=300, bbox_inches='tight')
        plt.close()

        # Operations count
        matrix_ops = [r['matrix_avg_operations'] for r in dense_results]
        heap_ops = [r['heap_avg_operations'] for r in dense_results]

        plt.figure(figsize=(10, 6))
        plt.plot(v_counts, matrix_ops, 'o-', label='Adjacency Matrix', linewidth=2, markersize=8)
        plt.plot(v_counts, heap_ops, 's-', label='Adjacency List + Heap', linewidth=2, markersize=8)
        plt.xlabel('|V| (Number of Vertices)')
        plt.ylabel('Average Number of Operations')
        plt.title('Part (c): Implementation Comparison\nDense Graphs - Varying |V| (Operations)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/part_c_dense_varying_v_operations.png", dpi=300, bbox_inches='tight')
        plt.close()

    # Graph 6: Matrix vs Heap - Fixed |V| varying |E|
    if fixed_v_results:
        e_counts = [r['e_count'] for r in fixed_v_results]
        matrix_times = [r['matrix_avg_time'] for r in fixed_v_results]
        heap_times = [r['heap_avg_time'] for r in fixed_v_results]

        plt.figure(figsize=(10, 6))
        plt.plot(e_counts, matrix_times, 'o-', label='Adjacency Matrix', linewidth=2, markersize=8)
        plt.plot(e_counts, heap_times, 's-', label='Adjacency List + Heap', linewidth=2, markersize=8)
        plt.xlabel('|E| (Number of Edges)')
        plt.ylabel('Average Time (seconds)')
        plt.title(f'Part (c): Implementation Comparison\nFixed |V|={fixed_v_results[0]["v_count"]} - Varying |E|')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/part_c_fixed_v_varying_e_time.png", dpi=300, bbox_inches='tight')
        plt.close()

        # Operations count
        matrix_ops = [r['matrix_avg_operations'] for r in fixed_v_results]
        heap_ops = [r['heap_avg_operations'] for r in fixed_v_results]

        plt.figure(figsize=(10, 6))
        plt.plot(e_counts, matrix_ops, 'o-', label='Adjacency Matrix', linewidth=2, markersize=8)
        plt.plot(e_counts, heap_ops, 's-', label='Adjacency List + Heap', linewidth=2, markersize=8)
        plt.xlabel('|E| (Number of Edges)')
        plt.ylabel('Average Number of Operations')
        plt.title(f'Part (c): Implementation Comparison\nFixed |V|={fixed_v_results[0]["v_count"]} - Varying |E| (Operations)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/part_c_fixed_v_varying_e_operations.png", dpi=300, bbox_inches='tight')
        plt.close()

    print(f"Plots saved to {output_dir} directory")

'''
    # Example data structure:
    sample_result = {
        'type': 'sparse',  # or 'dense' or 'fixed_v'
        'v_count': 100,
        'e_count': 99,
        'matrix_avg_time': 0.001,
        'heap_avg_time': 0.0005,
        'matrix_avg_operations': 10000,
        'heap_avg_operations': 5000
'''
