import pathlib
import yaml

file_path = pathlib.Path("./config.yaml").resolve()
text = {'name': 'Boyo', 'age': 18, 'children': ['Odogwu', 'Dorcas']}
with file_path.open(mode="w")as new_file:
    yaml.dump(text, new_file, sort_keys=False)

with file_path.open(mode="r")as f:
    # print(yaml.safe_load(f))
    text_file = yaml.load(f, Loader=yaml.Loader)

print(text_file)
