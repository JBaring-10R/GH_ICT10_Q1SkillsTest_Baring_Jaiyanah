from js import document
from pyscript import when

# --- Compute total ---
@when("click", "#submit")
def compute_total(event=None):
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    items = {
        "item1": ("Chocoberry Ice Cream Sandwich", 103),
        "item2": ("Classic Neapolitan Smoothie", 163),
        "item3": ("Strawberry Shortcake", 800),
        "item4": ("Cocoa Cream Frappe", 185),
        "item5": ("Neapolitan Crepe Roll", 235),
    }

    total = 0
    selected = []

    for key, (food, price) in items.items():
        if document.getElementById(key).checked:
            total += price
            selected.append(f"{food} - ₱{price}")

    if selected:
        summary = f"""
        <h3>Order Summary</h3>
        <p><b>Name:</b> {name}</p>
        <p><b>Address:</b> {address}</p>
        <p><b>Contact:</b> {contact}</p>
        <p><b>Items Ordered:</b><br>{'<br>'.join(selected)}</p>
        <h4>Total Amount: ₱{total}</h4>
        """
    else:
        summary = "<p>˚₊‧꒰ა ᴘʟᴇᴀꜱᴇ ꜱᴇʟᴇᴄᴛ ᴀᴛ ʟᴇᴀꜱᴛ ᴏɴᴇ ɪᴛᴇᴍ. ໒꒱ ‧₊˚</p>"

    document.getElementById("summary").innerHTML = summary


@when("click", "#clear")
def clear_form(event=None):
    document.getElementById("orderForm").reset(); document.getElementById("summary").innerHTML = ""