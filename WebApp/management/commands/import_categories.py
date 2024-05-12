from django.core.management.base import BaseCommand
from WebApp.models import Categories  # Make sure the import matches the app name and model location

class Command(BaseCommand):
    help = 'Loads a list of categories and subcategories into the database'

    def handle(self, *args, **options):
        CATEGORIES = {
    'Electronics': [
        'Computers & Accessories',
        'Cell Phones & Accessories',
        'Television & Video',
        'Camera & Photo',
        'Portable Audio & Video',
        'Car Electronics & GPS',
        'Musical Instruments',
        'Wearable Technology',
        'Video Game Consoles & Accessories'
    ],
    'Clothing': [
        'Women',
        'Men',
        'Girls',
        'Boys',
        'Baby',
        'Shoes',
        'Jewelry',
        'Watches',
        'Handbags & Accessories'
    ],
    'Home & Kitchen': [
        'Kitchen & Dining',
        'Bedding',
        'Bath',
        'Furniture',
        'Home Decor',
        'Wall Art',
        'Lighting & Ceiling Fans',
        'Seasonal Decor',
        'Event & Party Supplies',
        'Heating, Cooling & Air Quality',
        'Irons & Steamers',
        'Vacuums & Floor Care',
        'Storage & Organization'
    ],
    'Beauty & Personal Care': [
        'Makeup',
        'Skin Care',
        'Hair Care',
        'Fragrance',
        'Foot, Hand & Nail Care',
        'Tools & Accessories',
        'Shave & Hair Removal',
        'Personal Care',
        'Oral Care'
    ],
    'Books': [
        'Books',
        'Magazines',
        'Textbooks',
        'Children\'s Books',
        'Comics & Graphic Novels'
    ],
    'Sports & Outdoors': [
        'Outdoor Recreation',
        'Sports & Fitness',
        'Hunting & Fishing',
        'Athletic Clothing',
        'Boating & Water Sports',
        'Cycling',
        'Climbing'
    ],
    'Toys & Games': [
        'Arts & Crafts',
        'Baby & Toddler Toys',
        'Building Toys',
        'Dolls & Accessories',
        'Puzzles',
        'Games',
        'Hobbies',
        'Kids\' Electronics'
    ],
    'Health & Wellness': [
        'Vitamins & Dietary Supplements',
        'Household Supplies',
        'Health Care',
        'Sports Nutrition',
        'Baby & Child Care',
        'Medical Supplies & Equipment'
    ],
    'Automotive': [
        'Automotive Parts & Accessories',
        'Tools & Equipment',
        'Car Electronics & GPS',
        'Tires & Wheels',
        'Motorcycle & Powersports',
        'RV Parts & Accessories'
    ],
    'Others': [
        'Pet Supplies',
        'Office Products',
        'Luggage & Travel Gear',
        'Appliances',
        'Lawn & Garden',
        'Tools & Home Improvement',
        'Grocery & Gourmet Food',
        'Industrial & Scientific',
        'Handmade Products',
        'Collectibles & Fine Art'
    ]
}

        for main_category, subcategories in CATEGORIES.items():
            main_cat_obj, created = Categories.objects.get_or_create(name=main_category)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added main category: {main_category}'))
            else:
                self.stdout.write(self.style.WARNING(f'Main category already exists: {main_category}'))

            for subcategory in subcategories:
                sub_cat_obj, created = Categories.objects.get_or_create(
                    name=subcategory, 
                    parent=main_cat_obj  # Assign the parent category
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added subcategory: {subcategory} under {main_category}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Subcategory already exists: {subcategory} under {main_category}'))

        self.stdout.write(self.style.SUCCESS('Finished importing categories and subcategories'))
