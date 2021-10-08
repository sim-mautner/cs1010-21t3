from pyhtml import html, title, body, p, h1, head

def main():
    my_html = html(
        head(
            title('Welcome Page')
        ),
        body(
            h1('Hello from COMP1010'),
            p('This is week 4 of the course.')
        )
        
    )
    print(my_html)

if __name__=="__main__":
    main()