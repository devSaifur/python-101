def list_files(current_file_tree: dict, current_path="") -> list:
    file_list = []

    for file in current_file_tree:
        if not current_file_tree[file]:
            file_list.append(f"/{file}")
        else:
            return file_list

    return file_list
