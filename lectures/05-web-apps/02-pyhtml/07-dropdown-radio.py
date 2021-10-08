from pyhtml import html, title, body, h1, head, form, select, option, label, input_

def main():

    my_html = html(
        head(
            title('Welcome Page')
        ),
        body(
            h1('Hello from COMP1010'),
            form(
                select(
                    option("A"),
                    option("B"),
                    option("C")
                ),
                label("Option 1", input_(type="radio", name="group1")),
                label("Option 2", input_(type="radio", name="group1"))
            )
        )
        
    )
    print(my_html)

if __name__=="__main__":
    main()