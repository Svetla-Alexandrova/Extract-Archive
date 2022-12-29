from pathlib import Path

root_dir = Path(".")
searched_item = "15"

for path in root_dir.rglob('*'):
  if path.is_file():
    if searched_item in path.stem:
      print(path.absolute())







# from pathlib import Path
# import zipfile

# root_dir = Path(".")
# destination_path = Path('destination')

# for path in root_dir.glob("*.zip"):
#     with zipfile.ZipFile(path, 'r') as zf:
#         final_path = destination_path / Path(path.stem)
#         zf.extractall(path=final_path)
        
