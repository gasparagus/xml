from lxml import etree


with open('C:\Users\glombardo\Desktop\Mesh\Files\desc2017.xml') as infile:
	with open('outfile.csv','a') as outfile:
		context = etree.iterparse(infile, events=('end',), tag='DescriptorUI')
		for event, elem in context:
			outfile.write('%s\n' % elem.text.encode('utf-8'))
			elem.clear()
			while elem.getprevious() is not None:
				del elem.getparent()[0]