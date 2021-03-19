# General Features

This document presents the ***basic features*** of MealPlan. Coders are expected to select which features are to be included in the MVP.

In very general terms, MealPlan is a **GUI software** that can **run on different OS**, which **executes the following tasks**: First, it will *produce a periodical meal plan* based on (0) culinary ability, (1) time constraints, (2) nutritional needs, (3) budget constraints and stocks, and (4) personal preferences. Second, MealPlan will *suggest a shopping list* of required ingredients according to the plan. Finally, MealPlan will *incorporate the meal plan into Google Calendar* for users to keep track of their plan. 

The table below specifies in detail what the 5 "considerations" are. They will be presented according to the 3 primary tasks above. Most of the considerations are related to the first task. Hence, if there is no mentioning of the other two in a "consideration", it is because they are unnecessary. 

Keep in mind that this is **NOT a function specification.** 

[URL Notion General Features](https://www.notion.so/0a148398432a4650a6c05cd2ec03ba30)

# I. Culinary ability
Description: 
1. The meal plan must suggest only dishes that the users know how to cook. MealPlan itself will offer a list of common dishes for users to choose from and users can also insert what other dishes they can cook.

2. MealPlan must be able to accept recipes inserted by the user. The user, when inserting their own recipes, must also specify what ingredients are required and how much time the recipes need. 

# II. Time constraints
Description: 
1. The meal plan is periodical. This means that it may be weekly, bi-weekly, monthly, etc,. The user decides this by inserting their preference.

2. The meal plan must suggest only dishes that the user can cook during the free time committed to cooking. This means that the amount of time required to cook must fit the free time slots. 

3. MealPlan may retrieve the free time slots from Google Calendar or the user can insert themselves. 

4. When incorporated into Google Calendar, the dishes must be put in the right free time slots. 

# III. Nutritional needs
Description: 
1. The dishes must satisfy basic nutritional needs of an average person, which are determined by MealPlan. MealPlan will base them on valid scientific research. 
2. The dishes must also satisfy personal nutritional needs, which is inserted by the user. For instance, for a person who is on a diet or for an athlete. 

# IV. Budget constraints and stocks
Description: 
1. The meal plan must be affordable given the budget of the user, which is inserted by the user. This means that the total amount of money must not exceed the budget.

2. MealPlan, when suggesting the shopping list, in addition to affordability, must also take into account what ingredients remain in stocks, which are inserted by the user. If there are foods remaining that can be used for the plan, they must be excluded from the suggested shopping list.

3. The prices of the food are taken from nearby supermarkets. For instance, BigC. 
# V. Personal Preferences
Description: 
1. The meal plan must satisfy users' requirement of diversity, which is inserted by the user. For instance, a user does not like to eat the same dish two days in a row. 

2. The meal plan must satisfy users' requirement of "tradition", which is inserted by the user. For instance, on Sunday, the user only wants to cook dinner. 

3. The meal plan must satisfy users' preferences of the number of meals daily, which is inserted by the user. For instance, person A may want to eat 3 times a day and person B may want to eat only 2 times a day. 

V4. The meal plan can be modified by the users to best serve their preference in that a specific day in the period.

V5. The meal plan must avoid dishes that the users are allergic to, which are inserted by the user. For instance, a person may be allergic to peanut. 

V6. MealPlan must allow users to pick which dishes they want to cook from the default list of dishes. Only those dishes are included in the final meal plan. 

IV7. MealPlan must allow users to insert their pre-cooked meals. This means that these pre-cooked meals must be included in the final meal plan. 

IV8. MealPlan must allow users to change some meals in the final meal plan as long as the nutrient needs are still satisfied. 