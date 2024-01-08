# file_management


Certainly! Below is a README template for your GitHub repository:

```markdown
# File Cleanup and Organization Script

This Python script organizes files in a specified directory based on their extensions into different folders. Additionally, it cleans up unnecessary and empty files and sets icons for the organized folders.

## Folder and File Structure

The script categorizes files into the following folders based on their extensions:

- **Images**: .png, .jpg, .jpeg, .tiff, .dwg
- **Documents**: .pdf, .doc, .docx, .csv, .xlsx, .xls
- **Code**: .cpp, .c, .rs, .java, .cs, .swift, .html, .css, .js
- **Text**: .txt, .log, .dat, .key
- **Video**: .mp3, .mov, .mp4, .gif, .mkv
- **Icon**: .ico, .icns

## Cleanup Threshold

Files that are empty and have been in the directory for more than a week are considered unnecessary and are deleted.

## Usage

1. Ensure that you have the required packages installed:

   ```bash
   pip3 install pyobjc-core pyobjc-framework-Cocoa
   ```

2. Update the `sourcedir` variable with the path to the directory you want to organize.

3. Run the script:

   ```bash
   python main.py
   ```

## Getting Started

### Prerequisites

- Python 3.x
- Required packages: pyobjc-core, pyobjc-framework-Cocoa

### Installation

Clone the repository:

```bash
git clone https://github.com/ganeshnikhil/file_management.git
cd file_management
```


### Usage

Update the `sourcedir` variable in `main.py` with the path to your target directory. Run the script:

```bash
python main.py
```

## Functions

- **set_icon(folder_name, sourcedir):** Sets icons for the folders based on the provided images.

- **is_unnecessary(file_path):** Checks if a file has been empty for more than a week.

- **is_empty_file(file_path):** Checks if a file is empty.

- **delete_empty_file(full_filepath):** Deletes empty files that are unnecessary.

- **move_file(dest, sourcedir, name):** Moves a file to the specified destination folder, handling naming conflicts.

- **organize_files(sourcedir):** Organizes files into folders based on their extensions.

- **clean_up(sourcedir):** Cleans up unnecessary files and sets icons for the folders.

## Example

```python
if __name__ == '__main__':
   sourcedir = "/path/to/your/directory"
   organize_files(sourcedir)
   clean_up(sourcedir)
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Icons used in this project are sourced from [Iconfinder](https://www.iconfinder.com/).

Feel free to customize the script and README file as needed.
```

Make sure to update placeholders like `ganesh nikhil` and provide a proper link to the license file if you have one. Also, include any acknowledgments or credits for external resources used in your project.
