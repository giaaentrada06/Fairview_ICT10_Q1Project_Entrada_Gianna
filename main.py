from pyscript import display, document

def order(e):
    total = 0
    items = []
    if document.getElementById("Better than the movies").checked:
        items.append("Better than the movies")
        total += 540.20
    if document.getElementById("The Song of Achilles").checked:
        items.append("The Song of Achilles")
        total += 500.20
    if document.getElementById("The Six of Crows").checked:
        items.append("The Six of Crows")
        total += 400.70
    if document.getElementById("Frankenstein and Cleopatra").checked:
        items.append("Frankenstein and Cleopatra")
        total += 599

    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    if items:
        summary = f"Name: {name}\nAddress: {address}\nContact: {contact}\nItems: {', '.join(items)}\nTotal: ₱{total}"
    else:
        summary = "No items selected."
    display(summary, target="summary")
    