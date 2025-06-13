import joblib
import sys
import os

filepath = "data/kandinsky-3k-original/train/meta/00000.joblib"
folder = 'data/kandinsky-3k-original/train/meta'

def load_joblib_file(filepath):
    try:
        data = joblib.load(filepath)
        print(f"Loaded data from {filepath}:")
        print(data)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error loading file: {e}")


def count_false_label(data):
    """
    Count 1 if the label in data is boolean False, else 0.
    
    Args:
        data (dict): A dictionary loaded from a joblib file, expected to have a 'label' key.
        
    Returns:
        int: 1 if label is False (boolean), else 0.
    """
    label = data.get('label', None)
    return 1 if label is False else 0

def find_false_in_joblib_files(folder_path):
    total_false_count = 0
    matching_files = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.joblib'):
            file_path = os.path.join(folder_path, filename)
            try:
                data = joblib.load(file_path)
                count = count_false_label(data)
                if count > 0:
                    matching_files.append((filename, count))
                    total_false_count += count
            except Exception as e:
                print(f"Failed to load {filename}: {e}")

    return total_false_count, matching_files

def sort_files_by_number(files):
    def extract_number(filename):
        # filename is a full path, get basename
        base = os.path.basename(filename)
        # example: "123.joblib" -> extract "123"
        number_str = base.split(".")[0]
        try:
            return int(number_str)
        except ValueError:
            # if filename doesn't start with a number, return something large or small
            return -1

    files.sort(key=extract_number)

def last_false_label_file(false_files, sort_by_mtime=True):
    if sort_by_mtime:
        false_files.sort(key=lambda f: os.path.getmtime(f))
    else:

        sort_files_by_number(false_files)  # sort by filename number
    if false_files:
        last_file = false_files[-1]
        return last_file
    else:
        return None

if __name__ == "__main__":
    load_joblib_file(filepath)
    '''
    total_count, matching_files = find_false_in_joblib_files(folder)

    print(f"Total occurrences of 'false': {total_count}")
    print("Files containing 'false':")
    for fname, count in matching_files:
        print(f"  {fname}: {count} occurrence(s)")
    false_files = [fname for fname, _ in matching_files]
    last_false_file = last_false_label_file(false_files, sort_by_mtime=False)
    
    if last_false_file:
        print(f"Last .joblib file with label=False: {last_false_file}")
        last_data = load_joblib_file(os.path.join(folder, last_false_file))
    else:
        print("No files with label=False found.")'''
# {'label': True, 'meta': {'concepts': [[6, 2, 5, 1, 6, 2], [6, 1, 5, 2, 6, 1], [5, 2, 5, 2, 4, 1]]}}
# {'fig0': {'c': (array([0, 1, 2]), array([2, 1, 0]), array([1073., 2690., 2837.])), 'y': (0, 0)}, 'fig1': {'c': (array([0, 1, 2]), array([0, 1, 2]), array([ 850., 1805., 3922.])), 'y': (0, 0)}, 'fig2': {'c': (array([0, 1, 2]), array([1, 0, 2]), array([ 666., 2088., 2405.])), 'y': (0, 0)}, 'y': 1}