ask_head = input("Does list have head? Y/N ")
if ask_head.lower() == "y":
    is_headed_list = True
    head_text = input("Paste head text here: ")
    tagged_head_text = f"<head>{head_text}</head>"
elif ask_head.lower() == "n":
    is_headed_list = False
else:
    print("Bad input! Run me again.")
incomplete_tagged_list_items = input("List items? Use syntax: 'De ligno,De sepulcro,De vestimento'").replace(",","</item><item>")
tagged_list_items = f"<item>{incomplete_tagged_list_items}</item>"
simple_or_Inline = input("(S)imple list or (I)nline list?")
if simple_or_Inline.lower() == "s":
    is_simple = True
elif simple_or_Inline.lower() == "i":
    is_simple = False
else:
    print("Bad input! Run me again.")
if is_simple and is_headed_list:
    print(f'<list rend="simple">{tagged_head_text}{tagged_list_items}</list>')
elif not is_simple and is_headed_list:
    print(f'<list rend="inline">{tagged_head_text}{tagged_list_items}</list>')
elif not is_simple and not is_headed_list:
    print(f'<list rend="inline">{tagged_list_items}</list>')
elif is_simple and not is_headed_list:
    print(f'<list rend="simple">{tagged_list_items}</list>')