import sys, os, json

this_folder = os.path.dirname(__file__)
schema_folder = os.path.join(this_folder,"schemas")
file = open(f"{schema_folder}/basic.json")

basic_schema = json.loads(file.read())

def hello(name: str) -> None:
    print(f"Hello, {name}!")

if __name__ == "__main__":
    hello("World")
