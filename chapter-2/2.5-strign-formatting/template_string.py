from string import Template

name = "Miles"

t = Template('Hey, $name!')
print(t.substitute(name=name))

