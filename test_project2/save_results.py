import os
import json
from pathlib import Path
from typing import Any, Dict, List, Set, Union

def json_serializer(obj: Any) -> Any:
    """Custom JSON serializer for non-serializable objects."""
    if isinstance(obj, set):
        return list(obj)
    if isinstance(obj, float) and (obj == float('inf') or obj == float('-inf')):
        return str(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def save_results(
    trial: int, 
    v_value: int, 
    graph_type: str,
    e_value: int,  # Add this parameter
    V: List[str], 
    E: Dict[str, List[tuple]], 
    matrix_V: List[str], 
    matrix_E: List[List[Union[float, int]]],
    start_node: str,
    a_distances: Dict[str, float], 
    a_predecessors: Dict[str, Union[str, None]], 
    a_operations: int, 
    matrix_time: float,
    b_distances: Dict[str, float], 
    b_predecessors: Dict[str, Union[str, None]], 
    b_operations: int, 
    heap_time: float
) -> None:
    """Save trial results to a JSON file with improved error handling and path management."""

    trial_data = {
        'graph': {
            'V': list(V),
            'E': E,
            'matrix_V': matrix_V,
            'matrix_E': matrix_E,
        },
        'start_node': start_node,
        'dijkstra_matrix': {
            'distances': a_distances,
            'predecessors': a_predecessors,
            'operations': a_operations,
            'time': matrix_time
        },
        'dijkstra_heap': {
            'distances': b_distances,
            'predecessors': b_predecessors,
            'operations': b_operations,
            'time': heap_time
        }
    }

    # Create directory structure: results/<graph_type>/trial_<trial>/
    folder_path = Path("results") / graph_type / f"trial_{trial}"
    folder_path.mkdir(parents=True, exist_ok=True)

    # Filename: Consistent with visualization filenames
    if graph_type == "fixed_v":
        filename = f"E{e_value}_{graph_type}_n{trial}.json"
    else:
        filename = f"V{v_value}_{graph_type}_n{trial}.json"

    trial_file = folder_path / filename

    try:
        with open(trial_file, 'w') as f:
            json.dump(trial_data, f, indent=2, default=json_serializer)
        print(f"Saved trial data to {trial_file}")
    except IOError as e:
        print(f"Error saving trial data to {trial_file}: {e}")
    except Exception as e:
        print(f"Unexpected error saving trial data: {e}")

