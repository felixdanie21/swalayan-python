from .models import Menu, Modul


# fungsi ambil menu
def ambil_menu(modulkode):
    if modulkode == 'dashboard':
        return ''
    elif modulkode == 'developer':
        dbmenu = [
            {
                "menukode": "D0100",
                "menunama": "IMPORT CSV",
                "menukontroler": "import_csv",
                "menuinduk": "D0000",
                "menustatus": "M",
                "menulevel": "1"
            },
        ]
        return dbmenu
    else:
        dbmenu = Menu.objects.filter(
            menulevel='1', modulkode=modulkode).order_by('menukode')
        for menu in dbmenu:
            submenu = Menu.objects.filter(menuinduk=menu.menukode)
            menu.submenu = submenu
        return dbmenu

# fungsi insert csv


def insert_csv(table, row):
    if table == 'menu':
        if not Menu.objects.filter(menukode=row[1]).first():
            menu = Menu.objects.create(
                modulkode=row[0],
                menukode=row[1],
                menunama=row[2],
                menukontroler=row[3],
                menuinduk=row[4],
                menustatus=row[5],
                menulevel=row[6],
            )
    elif table == 'modul':
        if not Modul.objects.filter(modulkode=row[0]).first():
            modul = Modul.objects.create(
                modulkode=row[0],
                modulnama=row[1],
            )
