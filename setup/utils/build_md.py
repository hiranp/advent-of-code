import os
import datetime
import collections

current_year = datetime.datetime.now().year
base_link = "https://github.com/hiranp/advent-of-code/blob/main/"


def parse(e):
    # name = os.path.splitext(e)[0]
    name = os.path.basename(e)
    return f"[{name}]({base_link}{e})"


path = f"{current_year}"
print(f"Looking for solutions in {path}")
print(f"Building README.md for {current_year}/")

readme_content = "## Puzzles list\n"
solutions = collections.defaultdict(list)

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        ext = os.path.splitext(filename)[1]
        if (
            ext in [".py", ".go", ".js", ".cpp", ".c", ".java"]
            and "init" not in filename
        ):
            # Extract day from the path 2023/1/src/solver1.py after the year
            day = dirpath.split("/")[-2]
            year = dirpath.split("/")[-3]
            solutions[day].append(os.path.join(dirpath, filename))

readme_content += f"\n\n## {year}"
for day, files in sorted(solutions.items()):
    readme_content += (
        f"\n\n### Day {day} : https://adventofcode.com/{year}/day/{day}\n\n"
    )
    tmp = [f"{i+1}. {parse(e)}" for i, e in enumerate(sorted(files, reverse=True))]
    readme_content += "\n".join(tmp)

print(readme_content)

# Replace the content of the README.md after "## Puzzles list: with the new content
with open("README.md", "r") as f:
    readme = f.read()
    readme = readme.split("## Puzzles list")[0]
    readme += readme_content
    print(readme)
    with open("README.md", "w") as f:
        f.write(readme)
