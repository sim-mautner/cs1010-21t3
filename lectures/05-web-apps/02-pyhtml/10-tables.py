from pyhtml import html, head, body, title, table, tr, td, th

def main():

    tutors = {'M15A':'Will',
        'T12A':'Liz',
        'T12B':'Ellie',
        'F12A':'Kai',
        'F15A':'Krishne'}
    
    table_rows_html = []
    header_row = tr(
        th('Class'), th('Tutor')
    )
    table_rows_html.append(header_row)
    for tute,tutor in tutors.items():
        table_rows_html.append(
            tr(td(tute), td(tutor))
        )


    my_html = html(
        table(
            table_rows_html
        )
    )
    print(my_html)

if __name__ == "__main__":
    main()