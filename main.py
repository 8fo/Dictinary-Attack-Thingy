with open("result.txt", "w") as f:
  f.write("")

target = input("Target: ")

with open("templates.txt", "r") as f:
  templates=f.read().replace("<$target>", target).split("\n")

with open("result.txt", "a") as f:
  for template in templates:
    f.write(template + "\n")
