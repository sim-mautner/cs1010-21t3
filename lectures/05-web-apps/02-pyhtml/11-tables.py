from pyhtml import html, head, body, title, table, tr, td, th

def main():

    classes = [
        {'class':'M15A', 'tutor':'Will', 'time':'Monday 3pm-6pm'},
        {'class':'T12A', 'tutor':'Liz', 'time':'Tuesday 12pm-3pm'},
        {'class':'T12B', 'tutor':'Ellie', 'time':'Tuesday 12pm-3pm'},
        {'class':'F12A', 'tutor':'Kai', 'time':'Friday 12pm-3pm'},
        {'class':'F15A', 'tutor':'Krishne', 'time':'Friday 3pm-6pm'}
    ]
    
    table_rows_html = []
    header_row = tr(
        th('Class'), th('Tutor'), th('Time')
    )
    table_rows_html.append(header_row)
    
    for tute in classes:
        table_rows_html.append(tr(
            td(tute['class']), td(tute['tutor']), td(tute['time'])
        ))


    my_html = html(
        table(
            table_rows_html
        )
    )
    print(my_html)

if __name__ == "__main__":
    main()