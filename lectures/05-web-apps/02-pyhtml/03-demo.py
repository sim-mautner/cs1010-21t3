from pyhtml import html, title, body, p, h1, head, a, br, img

def main():
    my_html = html(
        head(
            title('Welcome Page')
        ),
        body(
            h1('Hello from COMP1010'),
            p('This is week 4 of the course.'),
            br(), # adding an extra newline
            br(),
            br(),
            a(href="https://www.w3schools.com/")('Go to w3schools'), # link to w3schools
            br(),
            img(src="https://tinyurl.com/mehrkbd6", width="200px")
        )
        
    )
    print(my_html)

if __name__=="__main__":
    main()