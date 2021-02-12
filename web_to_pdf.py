import pdfkit
ORIENTATION = ""
SIZE = []

URL = 'https://www.amazon.ae/Apple-SuperDrive-Double-Layer-Connector-MD564ZM/dp/B008AL9VXI'
#SIZES = ["A0","A6","A9","B0","B3","C5E","Comm10E","DLE","Executive","Folio","Ledger","A4" , "Tabloid" , "Letter" ]

def generate_pdf(URL):
    SIZES = ["A6" , "Tabloid" , "Letter", "B3" ]
    for i in range(len(SIZES)):
        options = {
           'page-size': SIZES[i],
           'no-pdf-compression' : ''
        }
        Formats=["Mobile","Tabloid","Small web","Large web"]
        pdfkit.from_url(URL, "format_{}.pdf".format(Formats[i]), options=options)
        
        
        
        
    



generate_pdf(URL)
