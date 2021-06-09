import requests
from bs4 import BeautifulSoup
import concurrent.futures


def recipe_extractor(url):
    print(f"Current: {url}")
    category = url.split(':')[2]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find("ul", {"class": "category-page__members-for-char"})
    for ultag in soup.find_all("ul", {"class": "category-page__members-for-char"}):
        for litag in ultag.find_all('li', {"class": "category-page__member"}):
            name = litag.text.strip()
            link = litag.find('a')
            if name[:8] != "Category" and name[:9] != 'User blog':
                foodlink = "https://recipes.fandom.com" + link['href']
                category = category.replace('_Recipes', '')
                yield "{" + f'"category" : "{category}", "Name" : "{name}", "Link": "{foodlink}"' + "},\n"


def ingredient_extractor(url):


def main():

    urls = ["https://recipes.fandom.com/wiki/Category:Antipasto_Recipes",
            "https://recipes.fandom.com/wiki/Category:Bread_appetizer_Recipes"]
    # "https://recipes.fandom.com/wiki/Category:Canap%C3%A9_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Cheese_appetizer_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Chicken_wing_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Chilean_Appetizers",
    # "https://recipes.fandom.com/wiki/Category:Dip_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Ethnic_and_Regional_Appetizers",
    # "https://recipes.fandom.com/wiki/Category:Fondue_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Healthy_Appetizers",
    # "https://recipes.fandom.com/wiki/Category:Meat_appetizer_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Pastry_appetizer_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Pizza_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Quick_and_Easy_Appetizers",
    # "https://recipes.fandom.com/wiki/Category:Seafood_appetizer_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Sweet_appetizer_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Vegan_appetizer_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Vegetarian_appetizer_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Budget_Friendly_Main_Dish_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Fondue_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Frittata_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Healthy_Main_Dishes",
    # "https://recipes.fandom.com/wiki/Category:Main_Dish_Meat_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Main_Dish_Pasta_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Main_Dish_Poultry_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Main_Dish_Salad_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Main_Dish_Seafood_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Pizza_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Pot_pie_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Quiche_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Quick_and_Easy_Main_Dishes",
    # "https://recipes.fandom.com/wiki/Category:Saudi_Arabian_Meat_Dishes",
    # "https://recipes.fandom.com/wiki/Category:Vegan_Main_Dish_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Vegetarian_Main_Dish_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Baked_bean_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Breadstick_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Chutney_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Cornbread_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Cranberry_sauce_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Dumpling_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Garlic_bread_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Guacamole_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Kugel_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Pizza_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Pudding_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Quick_and_Easy_Side_Dishes",
    # "https://recipes.fandom.com/wiki/Category:Relish_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Roll_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Salad_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Salsa_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Side_Dish_Fruit_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Side_Dish_Meat_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Side_Dish_Pasta_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Side_Dish_Poultry_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Side_Dish_Rice_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Side_Dish_Seafood_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Side_Dish_Vegetable_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Slaw_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Soup_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Stuffed_Biscuit_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Stuffing_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Vegan_Side_Dish_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Vegetarian_Side_Dish_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Atkins_Desserts",
    # "https://recipes.fandom.com/wiki/Category:Cake_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Cheesecake_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Chilean_Desserts",
    # "https://recipes.fandom.com/wiki/Category:Christmas_Desserts",
    # "https://recipes.fandom.com/wiki/Category:Cobbler_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Crisp_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Custard_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Dessert_fondue_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Dessert_loaf_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Dessert_Salad_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Desserts_with_Rum",
    # "https://recipes.fandom.com/wiki/Category:Ethnic_and_Regional_Desserts",
    # "https://recipes.fandom.com/wiki/Category:Frozen_dessert_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Fruit_Desserts",
    # "https://recipes.fandom.com/wiki/Category:Healthy_Desserts",
    # "https://recipes.fandom.com/wiki/Category:Ice_cream_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Lindas_Busy_Kitchen_Desserts",
    # "https://recipes.fandom.com/wiki/Category:Malawian_Desserts",
    # "https://recipes.fandom.com/wiki/Category:No-bake_dessert_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Passover_Desserts",
    # "https://recipes.fandom.com/wiki/Category:Pie_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Pudding_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Sherbet_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Strawberry_Desserts",
    # "https://recipes.fandom.com/wiki/Category:Stuffed_Biscuit_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Torte_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Trifle_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Uruguayan_Appetizers",
    # "https://recipes.fandom.com/wiki/Category:Valentine%27s_Day_Desserts",
    # "https://recipes.fandom.com/wiki/Category:Vegan_dessert_Recipes",
    # "https://recipes.fandom.com/wiki/Category:Vegetarian_Dessert_Recipes"]

    with open("recipes.json", 'w') as f:
        f.write('{ "Recipes": [ \n')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            recipeLists = executor.map(recipe_extractor, urls)

        #     for recipes in recipeLists:
        #         for recipe in recipes:
        #             f.write(recipe)
        # f.write(']}')


if __name__ == '__main__':
    main()
