# program returns the basic price of items in some areas of Nigeria.

# initializing the market data into a list of dictonaries.
market_prices = [
    {
        "item": "fish",
        "lagos": 200,
        "abuja": 230,
        "benin city": 250,
        "type": "foodstuff",
    },
    {
        "item": "tomato",
        "lagos": 100,
        "abuja": 100,
        "benin city": 50,
        "type": "foodstuff",
    },
    {
        "item": "groundnut oil",
        "lagos": 120,
        "abuja": 150,
        "benin city": 100,
        "type": "foodstuff",
    },
    {
        "item": "rice",
        "lagos": 1000,
        "abuja": 1100,
        "benin city": 1200,
        "type": "foodstuff",
    },
    {
        "item": "Palm oil",
        "lagos": 100,
        "abuja": 150,
        "benin city": 100,
        "type": "foodstuff",
    },
    {
        "item": "beans",
        "lagos": 1200,
        "abuja": 1000,
        "benin city": 1500,
    },
    {
        "item": "yam",
        "lagos": 750,
        "abuja": 500,
        "benin city": 1000,
        "type": "foodstuff",
    },
    {"item": "salt", "lagos": 70, "abuja": 100, "benin city": 70, "type": "foodstuff"},
    {
        "item": "Android Phone",
        "lagos": 12500,
        "abuja": 12500,
        "benin city": 12500,
        "type": "phone",
    },
    {
        "item": "iPhone",
        "lagos": 12500,
        "abuja": 12500,
        "benin city": 12500,
        "type": "phone",
    },
    {
        "item": "disposable phone",
        "lagos": 5500,
        "abuja": 3500,
        "benin city": 7350,
        "type": "phone",
    },
    {"item": "polo", "lagos": 500, "abuja": 1000, "benin city": 700, "type": "shirt"},
    {
        "item": "sweat shirt",
        "lagos": 5000,
        "abuja": 7000,
        "benin city": 7000,
        "type": "shirt",
    },
    {
        "item": "packet shirt",
        "lagos": 5000,
        "abuja": 9000,
        "benin city": 7000,
        "type": "shirt",
    },
    {
        "item": "snickers",
        "lagos": 5000,
        "abuja ": 5000,
        "benin city": 7000,
        "type": "shoe",
    },
    {
        "item": "handcrafted ",
        "lagos": 15000,
        "abuja": 25000,
        "benin city": 19000,
        "type": "shoe",
    },
    {
        "item": "exotic",
        "lagos": 35000,
        "abuja": 50000,
        "benin city": 40000,
        "type": "shoe",
    },
    {
        "item": "jogging",
        "lagos": 5000,
        "abuja": 5000,
        "benin city": 7000,
        "type": "shoe",
    },
]


def get_item_names():
    all_items_names = []
    for item in market_prices:
        all_items_names.append(item["item"])
    return all_items_names


def add_new_item(item, region, price):
    market_prices.insert(0, {"item": item, region: price})
    print(f"you have added {item} to our database the price in {region} is {price}")
    return market_prices


def update_item_price(item, region, price):
    print(f"***** Updating price of {item} to {price} *****")
    check = False
    for items in market_prices:
        if items["item"] == item:
            before = items[region]
            items[region] = price
            after = items[region]
            print(f" before price = {before},  after price = {after} ")
            check = True

    if check is False:
        print("ITEM NOT FOUND!")
        request = input(f"Do you wnat to add {item} to database?(y/n):")

        if request.lower() == "n":
            get_user_input()
            return

        add_item()

    return check


def get_user_input():
    # get the input from a user
    print(
        """
        ************************************************
        Hello!, welcome to our price list python app,
        Reply "search" to search for an item,
        Reply "add" to add a new item to our database and
        Reply "quit" to exist the program
        ************************************************
        """
    )
    user_input = input("reply:")

    if user_input.lower() == "add":
        add_item_price()
        return

    if user_input.lower() == "search":
        search()
        return

    if user_input.lower() == "quit":
        print("Thanks for using this program, have a nice day")
        return


def add_item_price():
    # update prices of goods in your area
    print(
        """
        ************************************************
        you can add or update prices of goods in your area here:
        reply : "update" to update price of item,
        reply: "add" to add a new item,
        reply: "back" to go back to main menu.
        ************************************************
        """
    )
    user_input = input("reply:")

    if user_input.lower() == "add":
        add_item()

    if user_input.lower() == "back":
        get_user_input()

    if user_input.lower() == "update":
        get_item = input("what item do you want to update: ")
        update_item(get_item)


def add_item():
    regions = ("abuja", "lagos", "benin city", "benin")
    item_names = get_item_names()
    item_name = input("item name:")

    if item_name in item_names:
        print("name already exists")
        add_item_price()
        return

    item_region = input("where are you?(lagos, abuja, benin city:")

    if item_region not in regions:
        print("REGION NOT FOUND!")
        print(
            "please input one of the recognized areas, re enter the item details again"
        )
        add_item_price()
        return

    item_price = input("how much is it in your area?:")

    add_new_item(item_name, item_region, item_price)

    return item_price


def update_item(item):
    item_names_list = get_item_names()
    regions = ("abuja", "lagos", "benin city", "benin")

    if item not in item_names_list:
        print("ITEM DOES NOT EXISTS:")
        request = input("Do you wnat to add it ?(y/n): ")
        if request.lower() == "n":
            print(".....returning to main menu")
            get_user_input()
            return
        add_item()
        return

    confitmation_msg = input(f"do you want to update price for {item} (y/n):")

    if confitmation_msg.lower() == "n":
        print(".......returning to main menu")
        add_item_price()
        return

    if item in item_names_list:
        get_region = input("what region are you?: ")

        if get_region not in regions:
            print("REGION NOT FOUND!")
            print(
                "please input one of the recognized areas, re enter the item details again"
            )
            add_item_price()
            return

        get_updated_price = input(f" what is the new price in {get_region}: ")

        update_item_price(item, get_region, get_updated_price)


def search():
    # search for prices of goods in area overview
    print(
        """
        ************************************************
        you can find prices of items in your area here:
        reply : "search" to search for price of item,
        reply: "categories" to see various items in each categories,
        reply: "back" to go back to main menu.
        ************************************************
        """
    )
    user_input = input("reply:")

    if user_input.lower() == "search":
        search_input = input("what are you serching for?:")
        search_for_items(search_input)


def search_for_items(search_input):
    all_item_names = get_item_names()
    if search_input not in all_item_names:
        print("we could not find what you where looking for!")
        return

    for items in market_prices:
        items_price_lagos = items["lagos"]
        items_price_abuja = items["abuja"]
        items_price_benin = items["benin city"]

        if items["item"] == search_input.lower():
            # print(
            #     f"the basic price for {search_input} is: \n Lagos: {items_price_lagos} \n abuja: {items_price_abuja} \n Benin: {items_price_benin}"
            # )
            return {
                "items": search_input,
                "lagos": items_price_lagos,
                "benin": items_price_benin,
                "abuja": items_price_abuja,
            }


def search_multiple_items():
    print("you can search for multiple items here")

    # search_frequency = int(input("How many items do you want to search for?: "))
    search_frequency = input("How many items do you want to search for?: ")

    if not search_frequency.isdigit():
        print("this is right")
        return

    item_bundle = []

    for iteration_count in range(int(search_frequency)):
        user_input = input(f"item{iteration_count+1}: ")

        items = search_for_items(user_input)
        if type(items != dict):
            print("Enter \n'add' to add new item \n'type' to search by categories \n'back' to go back to main menu")
            return
        print(type(items))
        item_bundle.insert(0, items)
        # print(items)
        print(("*") * 10)

    # print(item_bundle)
    for items in item_bundle:
        name = items["items"]
        lagos = items["lagos"]
        abuja = items["abuja"]
        print(f"{name}: \n{lagos} Naira in lagos \n{abuja} Naira in abuja")


# get_user_input()


search_multiple_items()
