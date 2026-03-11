import qrcode

with open("top_500_websites.csv","r") as file:
    next(file)

    for i in file:
        data01=i.strip("\n")
        data02=data01.split(",")
        
        link=data02[1]
        site_name=data02[0]

        img=qrcode.make(link)
        img.save(f"{site_name}.jpg")