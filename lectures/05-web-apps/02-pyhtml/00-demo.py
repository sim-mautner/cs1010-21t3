from pyhtml import html, title, body, p

def main():
    my_html = html(
        p('Hello from COMP1010')
    )
    print(my_html)

if __name__=="__main__":
    main()