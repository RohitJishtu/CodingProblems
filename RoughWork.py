import os
import json

def extract_docstring(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines:
            if line.strip().startswith('"""') or line.strip().startswith("'''"):
                return line.strip().strip('"""').strip("'''")
        return None
    except Exception as e:
        return f"Error reading file: {e}"

def generate_metadata(root_dir):
    metadata = []

    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, root_dir)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    docstring = extract_docstring(full_path)
                    metadata.append({
                        "path": relative_path,
                        "lines": len(lines),
                        "docstring": docstring or "No docstring"
                    })
                except Exception as e:
                    metadata.append({
                        "path": relative_path,
                        "error": str(e)
                    })

    return metadata

if __name__ == "__main__":
    project_path = "."  # or replace with "path/to/CodingProblems"
    meta = generate_metadata(project_path)
    with open("metadata.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
    print("Metadata saved to metadata.json")
