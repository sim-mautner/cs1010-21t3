from pyhtml import html, title, body, h1, head, ol, li, ul

def get_html_list(items):
    list_items_pyhtml = []
    for item in items:
        list_items_pyhtml.append(li(item))
    return list_items_pyhtml

def main():

    hobbies = ['exercising', 'baking', 'board games']
    desserts = ['chocolate', 'cake', 'gelato', 'tiramisu', 'ice cream']
    

    my_html = html(
        head(
            title('Welcome Page')
        ),
        body(
            h1('Hello from COMP1010'),
            ol(get_html_list(hobbies)),
            ul(get_html_list(desserts))
        )
        
    )
    print(my_html)

if __name__=="__main__":
    main()