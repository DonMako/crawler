import jinja2
import webbrowser



def generate_page(image):

    outputfile = 'mygraphe.html'

    subs = jinja2.Environment(loader = jinja2.FileSystemLoader('./')).get_template('template.html').render(mydata=image)
    
    with open(outputfile,'w') as f:
        f.write(subs)

    return outputfile



def display_page(file):

    new = 2

    url = file
    webbrowser.open(url,new=new)



def page_from_scratch(image):

    display_page(generate_page(image))
