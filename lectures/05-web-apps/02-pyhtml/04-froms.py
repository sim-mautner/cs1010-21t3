from pyhtml import html, title, body, h1, head, form, input_, label

def main():
    my_html = html(
        head(
            title('Welcome Page')
        ),
        body(
            h1('Hello from COMP1010'),
            form(
                label('Name: ', input_(type="text")),
                input_(type="submit", value="Go")
            )
        )
        
    )
    print(my_html)

if __name__=="__main__":
    main()