def list_files(current_filetree: dict, current_path="") -> list:
    file_list = []

    for node in current_filetree:
        next_file_tree = current_filetree[node]
        if not next_file_tree:
            file_list.append(f"{current_path}/{node}")
        else:
            next_filepaths = list_files(next_file_tree, f"{current_path}/{node}")
            file_list.extend(next_filepaths)

    return file_list
