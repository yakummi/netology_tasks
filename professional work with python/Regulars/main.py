from start import reader, writer, split_names, duplicate_deleting, phone_editor

if __name__ == '__main__':
    writer(phone_editor(duplicate_deleting(split_names(reader()))))