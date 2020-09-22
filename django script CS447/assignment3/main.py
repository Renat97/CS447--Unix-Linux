# assignment3 CS447 by Renat Norderhaug, project on File I/O and django templating
#!/bin/python3
import json #Used to load json
from jinja2 import Environment, FileSystemLoader #Templating

def main(args):
	joined=""
	e = Environment(loader=FileSystemLoader('templates/'))

	json_file = json.load(open('entries.json','r'))

	for i in json_file:
		top = i.get('top')

	if top:
	  joined = "\n".join(top)

	kernelIP = i.get('kernel_path')
	if kernelIP:
	  joined = "".join(kernelIP)

	initp = i.get('initrd_path')
	if initp:
	  joined = "".join(initp)

	title = i.get('title')
	if title:
	  joined = "".join(title)
	template = e.get_template("base.tmpl")


	menuentry = template.render(kernel_path=joined, initrd_path=joined, top = joined, title = joined)


	print(menuentry)

if __name__ == "__main__":
  args = None
  main(args)
