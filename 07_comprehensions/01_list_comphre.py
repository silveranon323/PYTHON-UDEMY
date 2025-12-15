menu=[
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

iced_tea=[tea for tea in menu if tea.startswith("Iced")]
print(iced_tea)