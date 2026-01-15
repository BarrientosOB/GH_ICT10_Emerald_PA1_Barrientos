from pyscript import document,display


def getting_info(e):
    document.getElementById('div1').innerHTML = ""
    Ftemp = float(document.getElementById('Ftemp').value)

    Ctemp = (Ftemp - 32) * 5.0/9.0

    display(f"Your temperature in Celsius is: {Ctemp:.2f} °C", target="div1")

    if Ctemp >= 37.5:
        display("You have a fever.", target="div1")
    else:
        display("You do not have a fever.", target="div1")